---
status: new
icon: material/tools
---


<div markdown="1" align="center">

```{.text .tools-banner}
▀▀▀▀██▀▀▀▀   ▄▄▀▀▀▀▀▀▄▄   ▄▄▀▀▀▀▀▀▄▄   ██           ▄▄▀▀▀▀▀▀▀▀
    ██       ██      ██   ██      ██   ██             ▀▀▀▀▀▀▄▄
    ██       ▀▀▄▄▄▄▄▄▀▀   ▀▀▄▄▄▄▄▄▀▀   ██▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▀▀
```

</div>

# Building the 1st Version. { .centered }

!!! desc "First Version"

    The first version took one evening. Most of it was narrowing down what counts as `"a tool I installed"`{.green}, and one detour caused by a shell alias.
    
## Step 1: What did I install on purpose?

!!! desc "What did I install on purpose?"

    - `pacman -Qe`{.red} lists explicitly installed packages. On this machine it printed **673**, far too many to read.
    
    - Package groups explain part of that. Installing a group such as `gnome`{.green} or `base-devel`{.green} marks every member as explicit.
    
    Removing group members:
    
    ```bash
    comm -23 <(pacman -Qeq | sort) <(pacman -Qg | awk '{print $2}' | sort -u) | wc -l
    ```
    
    gave **538**. Only 126 had dropped out, so groups weren't the main cause. Splitting off the foreign (AUR) packages with `pacman -Qemq | wc -l`{.green} gave **53**, which is where most of the forgotten programs were: amdtop, aurdex, golazo, updo, rmlint and similar.
    
!!! tip "Useful pacman queries"
    
    <div class="steps" markdown>
    
    - `pacman -Qe`{.green}: explicitly installed.
    - `pacman -Qem`{.green}: explicitly installed and foreign (AUR).
    - `pacman -Qg`{.green}: members of groups.
    - `pacman -Ql <pkg>`{.green}: files a package installed.
    - `pacman -Qi <pkg>`{.green}: details, including description, size and install date.
    
    </div>

## Step 2: Keep only terminal tools.

!!! desc "Keep only terminal tools"

    Three filters turn `"explicitly installed"`{.skyblue} into `"a tool I might want to look up"`{.green}:
    
    <div class="steps" markdown>
    
    1. **Not a group member** (the `comm -23`{.red} above).
    2. **Not plumbing.** Names starting with `lib`{.red}, `python-`{.red}, `perl-`{.red}, `ruby-`{.red}, `ttf-`{.red}, `otf-`{.red}, `xorg-`{.red}, `gst-`{.red}, `qt5`{.red}, `gtk3-`{.red} and so on, plus anything ending `-libs`{.red} or `-doc`{.red}/`-docs`{.red}<!-- -->.
    3. **Installs a program in `/usr/bin`{.red} and has no `.desktop`{.red} launcher.** A desktop launcher means a GUI app, so it is left out.
    
    </div>
    
## Step 3: A first script.

!!! desc "A first script"

    The first script ran the filter in a loop and piped the result into fzf with a preview pane. It worked, but it called `pacman -Ql` once per package and was slow:
    
    ```bash
    #!/bin/bash
    # mytools - browse the CLI/TUI tools I explicitly installed
    comm -23 <(pacman -Qenq | sort) <(pacman -Qg | awk '{print $2}' | sort -u) \
    | grep -Ev '^(lib|lib32-|python-|perl-|ruby-|ttf-|otf-|xorg-|gst-|qt[0-9]|gtk[0-9]?-)|-libs$|-docs?$' \
    | while read -r p; do
        files=$(pacman -Ql "$p")
        grep -q ' /usr/bin/.' <<<"$files" && ! grep -q '\.desktop$' <<<"$files" && echo "$p"
      done \
    | fzf --preview 'pacman -Qi {} | grep -E "^(Description|Installed Size|Install Date)"; echo; pacman -Ql {} | grep " /usr/bin/." | awk "{print \$2}"' --preview-window=right:60%
    ```
    
    It is saved as `~/.local/bin/mytools`{.green} so it can be run from any terminal (Tilix, Ghostty, anything), with `~/.local/bin`{.green} on `PATH`{.green}<!-- -->.
    
## The Detour: A sudo prompt that should not exist.

!!! desc "A sudo prompt that should not exist"

    <div class="steps" markdown>
    
    - The first time the long loop was run as a one-liner it churned for about five minutes and then asked for a **sudo password**, which locked the account after three failed attempts (a `pam_faillock`{.green} lockout; it expires after about ten minutes or on reboot). Nothing in the command used sudo.
    
    - The cause was in `~/.zshrc`{.green}, line 248, from an old ArcoLinux template:
    
    ```bash
    alias pacman="sudo pacman --color auto"
    ```
    
    - In an interactive zsh, every `pacman`{.green} in the one-liner became `sudo pacman`{.green}. A script run as `mytools`{.green} uses `#!/bin/bash`{.green}, which does **not** load zsh aliases, so the saved script was never affected.
    
    </div>
    
!!! warning "A wrong turn worth recording"
    
    <div class="steps" markdown>
    
    - An early test, `bash -c 'type -a pacman'`{.green}, showed nothing unusual, and that was taken as proof there was no wrapper. It proved nothing: bash cannot see zsh aliases. The clue was a trace of the loop showing the real command being run: `sudo pacman --color auto -Qenq`{.green}.
    
    - The fix was to comment out the alias (and a few of its neighbours from the same template) with a `#`{.green}, not to delete anything:
    
    | Line(s) | What it was |
    |---------|-------------|
    | 248 | the `pacman` alias that caused it |
    | 290 to 295 | display-manager switcher aliases |
    | 371 | a `cleanup` alias that removes orphans without asking |
    
    - Because zsh only reads `.zshrc`{.green} when it starts, an already-open terminal keeps the old alias. A brand new shell confirms the edit:
    
    ```bash
    zsh -ic 'type pacman'
    ```
    
    - It should print `pacman is /usr/bin/pacman`{.green}. With the alias gone the script ran with no prompt and listed **207** tools.
    
    </div>
    
## Step 4: AUR included, searchable by description.

!!! desc "AUR included, searchable by description"

    The first list only matched package **names**, so typing `monitor`{.skyblue} or `audio`{.skyblue} found nothing. The second version asks pacman for descriptions and shows them as a second column, so fzf matches both. It also queries `pacman -Ql`{.green} once for all packages instead of once per package, which is much faster:
    
    ```bash
    cat > ~/.local/bin/mytools <<'EOF'
    #!/bin/bash
    # mytools - browse the CLI/TUI tools I explicitly installed (native + AUR), searchable by name and description
    explicit=$(comm -23 <(pacman -Qeq | sort) <(pacman -Qg | awk '{print $2}' | sort -u) \
      | grep -Ev '^(lib|lib32-|python-|perl-|ruby-|ttf-|otf-|xorg-|gst-|qt[0-9]|gtk[0-9]?-)|-libs$|-docs?$')
    bins=$(pacman -Ql $explicit | awk '{ if ($2 ~ /^\/usr\/bin\/[^\/]+$/) b[$1]=1; if ($2 ~ /\.desktop$/) d[$1]=1 } END { for (p in b) if (!(p in d)) print p }')
    pacman -Qi $bins | awk '/^Name/ {n=$3} /^Description/ {sub(/^Description *: /,""); print n "\t" $0}' | sort \
    | fzf --delimiter '\t' --preview 'pacman -Qi {1} | grep -E "^(Installed Size|Install Date)"; echo; pacman -Ql {1} | grep " /usr/bin/." | awk "{print \$2}"' --preview-window=right:40%
    EOF
    ```
    
    The count went from 207 to **224**, now including the AUR tools.
    
## Step 5: Tidy columns and a short name.

!!! desc "Tidy columns and a short name"

    The tab-separated columns didn't line up. Piping through `column -t -s $'\t'`{.green} pads each name so every description starts in the same place. The `{1}`{.green} in the preview command still refers to the first column, the package name.
    
    ```bash
    | column -t -s $'\t' \
    | fzf --preview '...' --preview-window=right:40%
    ```
    
    Finally, a short alias in `~/.zshrc`{.green}:
    
    ```bash
    alias tools=mytools
    ```
    
!!! info "Housekeeping done along the way"
    - A leftover `~/.fzf`{.green} folder from fzf's git installer was removed. The system fzf is on `PATH`{.green} first, so the old copy never ran, and the key bindings come from `source <(fzf --zsh)`{.green}.
    
    - At this point `tools`{.green} was a good, fast list. The next page connects it to mandible and the other help sources.
    
The [**next**](03-wiring-in-the-help-keys.md) page covers **wiring**{.skyblue} in `Mandible`{.green}, `tldr`{.green}, `cheat`{.green} and `man`{.green}.