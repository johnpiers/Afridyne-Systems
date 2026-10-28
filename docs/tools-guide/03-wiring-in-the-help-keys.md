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

# Wiring in mandible, tldr, cheat and man. { .centered }

!!! desc "More than a list!"

    With the list working, the next idea was to make it more than a list. The first thought was to imitate mandible's detailed view inside the script. That was rejected.
    
!!! note "Why not copy Mandible"

    Mandible's USAGE, POSITIONALS and FLAGS panes come from parsing `--help` output across many help-text frameworks. That parser **is** the project. Rebuilding it in shell would be fragile and would never match the real thing. Mandible is already installed, so the cheaper and better route is to hand off to it.
    
    The design: pressing a key on a highlighted tool runs a small helper, and fzf gives the whole terminal to the helper until it ends.
    
    | Key | Source |
    |-----|--------|
    | Enter | `mandible <command>` |
    | Ctrl+T | `tldr <command>` |
    | Ctrl+E | `cheat <command>` |
    | Ctrl+O | `man <command>`, in colour |
    
## Problem 1: A package name is not a command name.

!!! desc " A package name is not a command name"

    The list is made of **package** names, but mandible, tldr, cheat and man need a **command** name. The `7zip` package installs `7z`. The `bind` package installs 29 commands and none is called `bind`.
    
    `mytools-bin` takes a package name and prints the command to use:
    
    1. If the package installs a command with the same name, use it (`atop`, `bat`).
    2. If it installs exactly one command, use that (`7zip` gives `7z`).
    3. Otherwise show a small fzf **picker** of its commands, so you choose (`bind`).
    
    ```bash
    #!/bin/bash
    # mytools-bin <package> - print the main command a package installs in /usr/bin (ask if there are several)
    pkg="$1"
    bins=$(pacman -Ql "$pkg" 2>/dev/null | awk '$2 ~ /^\/usr\/bin\/[^\/]+$/ {n=split($2,a,"/"); print a[n]}')
    if [ -z "$bins" ] && command -v "$pkg" >/dev/null 2>&1; then echo "$pkg"; exit 0; fi
    if grep -qx "$pkg" <<<"$bins"; then
      echo "$pkg"
    elif [ "$(grep -c . <<<"$bins")" -le 1 ]; then
      echo "$bins"
    else
      fzf --header "$pkg has several commands: type to filter, Enter to choose, Esc to cancel" <<<"$bins"
    fi
    ```

!!! info "The line near the top"

    The `if [ -z "$bins" ] ...` line was added later, for the admin commands described on page 4. It handles names that are commands but not packages.
    
    The first version of this helper picked the first command alphabetically when nothing matched. For `bind` that opened `arpaname`, a tiny tool, and mandible showed an almost empty page with low confidence: 0% parsed`. That was the helper being wrong, not mandible. The picker fixed it. If you press Esc in the picker, the helper prints nothing, and the caller exits quietly (`[ -z "$cmd" ] && exit 0`), so cancelling never produces an error.
    
## Problem 2: Colour is lost in a pipe.

!!! desc "Colour is lost in a pipe"

    The first attempt piped tldr, cheat and man into `less`. All three looked sparse and plain, and the text hugged the bottom of the screen.
    
    The reason is that these tools only colour their output when writing straight to a terminal. In a pipe they turn colour off, and `man` also skips `MANPAGER` entirely. In this setup coloured man pages come from:
    
    ```bash
    export MANPAGER="sh -c 'col -bx | bat -l man -p'"
    ```
    
    plus an oh-my-zsh `man` function that only exists in an interactive zsh. A script can't see a shell function.
    
    The fix is to **run each tool directly**, not through a pipe, and to set `MANPAGER` inside the helper so it doesn't depend on the zsh setup.
    
## Problem 3: Pages that flash and vanish.

!!! desc "Pages that flash and vanish"

    Short man pages (`arpaname`'s is a few lines) flashed up and disappeared. `bat` prints a page that fits on one screen and exits immediately, and fzf then redraws the list over it. Pages longer than a screen are fine because the pager waits.
    
    The helper therefore counts the lines. If the page is shorter than the terminal, it waits for a keypress; if it is longer, the pager's own `q` is enough:
    
    ```bash
    n=$(man "$cmd" 2>/dev/null | wc -l)
    man "$cmd"
    [ "$n" -lt "$(tput lines)" ] && pause
    ```
    
## The helper, final version.

!!! desc "The helper, final version"

    This is the finished `mytools-help`. Compared with the first one it also does two things added later in the project:
    
    - If a command has **no man page**, it shows the tool's colour `--help` instead (not for three tools that should not be run blindly).
    - For tldr it **checks your own pages first**, in `~/.local/share/mytools/tldr/`, then falls back to the official tldr cache. Page 5 explains why.
    
    
    ```bash
    #!/bin/bash
    # mytools-help <tldr|cheat|man|mandible> <package> - show help for a package's main command
    cmd=$(mytools-bin "$2")
    [ -z "$cmd" ] && exit 0
    export MANPAGER="sh -c 'col -bx | bat -l man -p'"
    pause() { read -n1 -s -r -p $'\n[press any key to return]'; }
    case "$1" in
      man)
        if man -w "$cmd" >/dev/null 2>&1; then
          n=$(man "$cmd" 2>/dev/null | wc -l)
          man "$cmd"
          [ "$n" -lt "$(tput lines)" ] && pause
        else
          case "$cmd" in
            set-wireless-regdom|os-prober|text-engine-demo)
              echo "No man page for $cmd (not running it to find out more)"; pause ;;
            *)
              out=$({ echo "No man page for $cmd - showing its --help instead"; echo; "$cmd" --help 2>&1; })
              printf '%s\n' "$out" | bat -l help -p --paging=always
              [ "$(printf '%s\n' "$out" | wc -l)" -lt "$(tput lines)" ] && pause ;;
          esac
        fi ;;
      tldr)
        mine="$HOME/.local/share/mytools/tldr/$cmd.md"
        if [ -f "$mine" ]; then tldr -r "$mine"; else tldr "$cmd"; fi
        pause ;;
      cheat)    cheat "$cmd"; pause ;;
      mandible) mandible "$cmd" ;;
    esac
    ```
    
## The main script, wired to the helper.

!!! desc "The main script, wired to the helper"

    The key bindings in `mytools` call the helper with the package name from the first column (`{1}`):
        
    ```bash
    --bind 'enter:execute(mytools-help mandible {1})' \
    --bind 'ctrl-t:execute(mytools-help tldr {1})' \
    --bind 'ctrl-e:execute(mytools-help cheat {1})' \
    --bind 'ctrl-o:execute(mytools-help man {1})' \
    ```
    
    Mandible quits with `Ctrl+C` or `Esc` and returns to the `tools` list exactly where you left it. The `execute` action is what lets a full-screen program take over the terminal and then hand it back.
    
!!! warning "Tested key by key"
    The keys were connected one at a time and each was tested before moving on. An early attempt changed several things at once and had to be walked back. The order that worked: write the helper, test it by hand (`mytools-help man bat`), then wire in a single key, test, and repeat.

## Searching inside Mandible.

!!! important "Searching inside Mandible"

    A natural question was whether `/` in Mandible searches across all your tools. It does not. Search is scoped to the tool you opened, so searching for `git` while viewing `bat` finds nothing. That is how mandible is designed and not a fault in the integration. Cross-tool search is what `tools` itself provides, with the description text.
    
The [**next**](04-admin-commands-and-polish.md) page covers **admin cmds**{.skyblue}, the `preview pane`{.green}, and `Esc`{.green}.