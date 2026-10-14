---
icon: octicons/desktop-download-24
---

<div style="display: none;"><h1>ProperDocs-Part1-Setup</h1></div>

![](../imgs/properdocs-index.png){: style="display: block; margin: 0 auto"}

# ProperDocs-Part1-Setup. { .centered }


##  Adding ProperDocs to the Afridyne Systems site: Part 1, Setup and Copy { .centered }

!!! deep-dive "Adding ProperDocs"

    This is a step-by-step record of how the ProperDocs documentation was brought into the Afridyne Systems MaterialX site, without rebuilding a second website. The approach throughout was one small step at a time: look at the current state, paste the output, then change something.
    
    The write-up is in three parts:
    
    1. **Part 1 (this page):** inspect the download, prepare the build environment, copy the files, fix the includes and add the nav entry.
    2. **Part 2:** the first build, clearing every warning, the visual checks, the deploy routine and some later fixes.
    3. **Part 3:** the green social cards and the banner block on every page.
    
    !!! tip "Tip"
    
        **Tip:** in the shell used here, `ls` is aliased to `colorls`, which garbles the output. `find`, `grep` and `cat` give clean output, so most checks below use those.
        
## 1. Where everything lives

| What | Path |
|---|---|
| Working site (all editing happens here) | `/home/johnpc/AfridyneSystems/` |
| Git site (not loadable, receives a sync) | `/mnt/sdb/AfridyneSystems/` |
| Deploy script | `/home/johnpc/Deploy` |
| ProperDocs download | `/mnt/sdb/ProperDocs/properdocs-master` |
| Python venv | `/home/johnpc/.venv` |

!!! recommendation "Workflow"

    The flow is Working site, then `rsync` to the Git site, then `git push` to GitHub, then GitHub Actions builds the live site.
    
    The Deploy script does this:
    
    
    ```bash
    #!/usr/bin/env bash
    set -euo pipefail
    
    WORKING_DIR="/home/johnpc/AfridyneSystems/"
    GIT_DIR="/mnt/sdb/AfridyneSystems/"
    
    echo "Syncing Working Site -> Git Site..."
    rsync -av --delete --exclude='.git' --exclude='.cache' --exclude='/README.md' "$WORKING_DIR" "$GIT_DIR"
    
    cd "$GIT_DIR"
    git add -A
    
    if git diff --cached --quiet; then
        echo "No changes to commit. Exiting."
        exit 0
    fi
    
    read -rp "Commit message: " COMMIT_MSG
    git commit -m "$COMMIT_MSG"
    git push origin main
    ```
    
    ---
    
    !!! important "Important"
    
        **Important:** plain `mkdocs` in a fresh terminal can be the system copy (`/bin/mkdocs`), which has no `material` module. Activate the venv, or call `/home/johnpc/.venv/bin/mkdocs` by its full path.
        
## 2. The goal

!!! decision "The goal"

    - Put the ProperDocs pages under `docs/properdocs/`.
    - Add them to the nav inside the **Home** section, next to the existing "MkDocs Start Page" and "Get Started-MkDocs" entries.
    - Bring across only the documentation, not their site.
    
## 3. Step 1: look at the download

!!! ex "Step 1: Look at the download"

    ```bash
    ls /mnt/sdb/ProperDocs/properdocs-master
    ls /mnt/sdb/ProperDocs/properdocs-master/docs
    ```
    
    The docs live in `docs/`, with their config in `properdocs.yml`. Three things in `docs/` belong to their own website and are left behind: `CNAME`, `hooks.py` and the `css/` folder.
    
## 4. Step 2: Read their nav and page lists

!!! instruction "Step 2: Read their nav and page lists"

    ```bash
    sed -n '/^nav:/,$p' /mnt/sdb/ProperDocs/properdocs-master/properdocs.yml
    cd /mnt/sdb/ProperDocs/properdocs-master/docs
    find . -type f \( -name '*.md' -o -path './img/*' \) | sort
    cat user-guide/README.md
    echo "-----"
    cat dev-guide/README.md
    ```
    
    Their nav lists `user-guide/` and `dev-guide/` as folders. The `literate-nav` plugin builds those page lists from the `README.md` file in each folder, so the real page order is inside those two files:
    
    | Section | Pages, in order |
    |---|---|
    | User Guide | installation, writing-your-docs, choosing-your-theme, customizing-your-theme, localizing-your-theme, configuration, cli, deploying-your-docs |
    | Developer Guide | themes, translations, plugins, api |
    | About | release-notes, contributing, license, who-we-are |
    
    The download has 20 pages and 11 images (ten PNGs and one SVG), 31 files in all.
    
## 5. Step 3: Check for special syntax before copying

!!! education "Step 3: Check for special syntax before copying"

    Their config uses extensions that your site may not have. This finds out which ones the pages actually use:
    
    ```bash
    cd /mnt/sdb/ProperDocs/properdocs-master/docs
    echo "== mkdocstrings / mkdocs-click =="; grep -rn '^\s*:::' . --include='*.md'
    echo "== snippets =="; grep -rn -e '--8<--' . --include='*.md'
    echo "== callouts =="; grep -rn '\[!' . --include='*.md'
    echo "== gh links =="; grep -rnE '(^|\s)(#[0-9]+|@[A-Za-z0-9_-]+)' . --include='*.md'
    echo "== plugin-events refs =="; grep -rn 'plugin-events' . --include='*.md'
    ```
    
    What it found:
    
    | Syntax | Where | What it means |
    |---|---|---|
    | `:::` directives (mkdocstrings) | `dev-guide/api.md`, `plugins.md`, `themes.md` | about 70 directives that pull API docs from the `properdocs` Python package |
    | `::: mkdocs-click` | `user-guide/cli.md` | builds the command-line tables from the `properdocs` package |
    | `--8<--` snippet | `dev-guide/plugins.md` line 265 | includes `docs/img/plugin-events.svg`, so the path needs fixing |
    | `--8<--` snippet | `about/contributing.md` line 1 | includes `CONTRIBUTING.md` from the project root, which your site doesn't have |
    | callouts | none | the `callouts` extension isn't needed |
    | GitHub links | one harmless hit | `mdx_gh_links` isn't needed |
    
    Your config already had `mkdocstrings`, `autorefs`, `mkdocs-click` and `pymdownx.snippets`. The `redirects` and `literate-nav` plugins aren't needed, since the nav is written straight into your yaml.
    
## 6. Step 4: Prepare the build environment (local and CI)

!!! desc "Step 4: Prepare the build environment (local and CI)"

    The `:::` directives need the `properdocs` package importable in the same environment as the build. That means your venv **and** the GitHub Actions build.
    
    **Local venv.** If `pip list` prints nothing in a `uv`-created venv, use `uv`:
    
    ```bash
    uv pip list --python /home/johnpc/.venv/bin/python | grep -iE '^(properdocs|mkdocs|mkdocstrings|mkdocs-click|griffe)'
    ```
    
    Here it already had `properdocs 1.6.7`, `mkdocstrings`, `mkdocstrings-python`, `mkdocs-click` and `griffe`.
    
    **CI.** GitHub Actions installs from `requirements.txt`, so check what it lists and how the workflow installs it:
    
    ```bash
    cat /home/johnpc/AfridyneSystems/requirements.txt
    grep -nE 'python|pip|requirements|uv ' /home/johnpc/AfridyneSystems/.github/workflows/deploy.yml
    ```
    
    `properdocs` and `mkdocstrings-python` were missing from the file. The workflow uses `python-version: 3.x` and `uv pip install --system -r requirements.txt`, so no workflow changes are needed. Add the two lines:
    
    ```bash
    printf '\nmkdocstrings-python\nproperdocs==1.6.7\n' >> /home/johnpc/AfridyneSystems/requirements.txt
    tail -5 /home/johnpc/AfridyneSystems/requirements.txt
    ```
    
    `properdocs` is pinned to the version that works in the venv. The other line is left unpinned, like `mkdocstrings`.
    
## 7. Step 5: Copy the files

!!! recommendation "Step 5: Copy the files"

    Always dry-run first (`-n` lists the files without writing anything):
    
    ```bash
    ls -d /home/johnpc/AfridyneSystems/docs/properdocs 2>&1
    rsync -avn --exclude='hooks.py' --exclude='CNAME' --exclude='css/' --exclude='*.py' \
      /mnt/sdb/ProperDocs/properdocs-master/docs/ /home/johnpc/AfridyneSystems/docs/properdocs/
    ```
    
    The `ls` should report that the folder doesn't exist yet. The two trailing slashes matter. `*.py` also skips `img/plugin-events.py`, a helper script the docs don't need.
    
    When the list looks right, run the real copy (no `--delete`, so it can only add files):
    
    ```bash
    rsync -av --exclude='hooks.py' --exclude='CNAME' --exclude='css/' --exclude='*.py' \
      /mnt/sdb/ProperDocs/properdocs-master/docs/ /home/johnpc/AfridyneSystems/docs/properdocs/
    find /home/johnpc/AfridyneSystems/docs/properdocs -type f | wc -l
    ```
    
    The count should be **31** (20 pages and 11 images).
    
## 8. Step 6: Fix the two includes

### The plugin events diagram

!!! desc "The plugin events diagram"

    `dev-guide/plugins.md` line 265 includes the SVG by a path that no longer exists. Look at it first, then fix only that line:
    
    ```bash
    cd /home/johnpc/AfridyneSystems/docs/properdocs
    sed -n '263,267p' dev-guide/plugins.md
    sed -i '265s|"docs/img/plugin-events.svg"|"docs/properdocs/img/plugin-events.svg"|' dev-guide/plugins.md
    sed -n '263,267p' dev-guide/plugins.md
    ```
    
    The snippets extension resolves paths from the folder where `mkdocs` runs (the site root, locally and in CI), so this path works in both.
    
### The contributing page

!!! ex "The contributing page"

    `about/contributing.md` is a single line, `--8<-- "CONTRIBUTING.md"`, which includes a file from the ProperDocs project root. Your site has no such file, so copy the file's text over the page instead. Every link in it is an absolute `https://` URL, so none will break:
    
    ```bash
    cp /mnt/sdb/ProperDocs/properdocs-master/CONTRIBUTING.md \
       /home/johnpc/AfridyneSystems/docs/properdocs/about/contributing.md
    wc -l /home/johnpc/AfridyneSystems/docs/properdocs/about/contributing.md
    ```
    
    It should report 233 lines.
    
### A check for CriticMarkup

!!! desc "A check for CriticMarkup"

    Your site has `pymdownx.critic` enabled, which can mangle code blocks. This looks for its trigger sequences in the new pages:
    
    ```bash
    grep -rnE '\{(\+\+|--|~~|>>|==)' /home/johnpc/AfridyneSystems/docs/properdocs --include='*.md'
    ```
    
    It printed nothing, so nothing needed fixing.
    
## 9. Step 7: Add the nav entry

!!! ex "Step 7: Add the nav entry"

    Back up the yaml first, so you can undo with one command:
    
    ```bash
    cd /home/johnpc/AfridyneSystems
    cp mkdocs.yml mkdocs.yml.bak
    ```
    
    The new block goes inside `Home:`, directly after the `Get Started-MkDocs` line, at the same indent as that line (6 spaces). Everything below it is indented relative to
    
    `- ProperDocs:`:
    
    ```yaml
    nav:
      - Home:
          - index.md
          - MkDocs Start Page: MkDocs-Material-Start.md
          - Get Started-MkDocs: about.md
          - ProperDocs:
            - Home: properdocs/index.md
            - Getting Started: properdocs/getting-started.md
            - User Guide:
              - Overview: properdocs/user-guide/README.md
              - Installation: properdocs/user-guide/installation.md
              - Writing Your Docs: properdocs/user-guide/writing-your-docs.md
              - Choosing Your Theme: properdocs/user-guide/choosing-your-theme.md
              - Customizing Your Theme: properdocs/user-guide/customizing-your-theme.md
              - Localizing Your Theme: properdocs/user-guide/localizing-your-theme.md
              - Configuration: properdocs/user-guide/configuration.md
              - Command Line Interface: properdocs/user-guide/cli.md
              - Deploying Your Docs: properdocs/user-guide/deploying-your-docs.md
            - Developer Guide:
              - Overview: properdocs/dev-guide/README.md
              - Themes: properdocs/dev-guide/themes.md
              - Translations: properdocs/dev-guide/translations.md
              - Plugins: properdocs/dev-guide/plugins.md
              - API Reference: properdocs/dev-guide/api.md
            - About:
              - Release Notes: properdocs/about/release-notes.md
              - Contributing: properdocs/about/contributing.md
              - License: properdocs/about/license.md
              - Who We Are: properdocs/about/who-we-are.md
    
      - Get started:
    ```
    
    Check the placement and that nothing else changed:
    
    ```bash
    grep -n -B3 -A3 'ProperDocs:' mkdocs.yml
    diff mkdocs.yml.bak mkdocs.yml
    ```
    
    The diff should show only the 22 new lines. Once you're happy, delete `mkdocs.yml.bak`. The Deploy script syncs the whole folder, so a leftover backup would be committed.
    
    **Note:** a `README.md` page named in the nav (the two "Overview" entries) is treated as its section's own landing page. In the sidebar, clicking "User Guide" opens that page, and there is no separate "Overview" item. That's the tidier result.
    
    **Next:** Part 2 covers the first build and clearing every warning.
    
[Part 2](ProperDocs-Part2-Build-and-Fixes.md)