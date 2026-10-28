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

# Admin commands, the preview pane and Esc. { .centered }


!!! desc "Tools" 

    `tools` only listed packages you installed on purpose. That left out the commands you use constantly but never installed, because they arrived with the base system: `systemctl`, `sed`, `awk`, `dig`, `ip`. Those belong to packages like systemd, coreutils and gawk. They are the commands most worth having a quick tldr or cheat sheet for, so they got their own list.
    
## An editable list

!!! desc "An editable list"

    The list is a plain text file, one command per line. Lines starting with `#` are ignored. Add or remove commands whenever you like. A `# Heading` line starts a new group:

    ```text
    # Network
    ip
    ss
    curl
    ```

    The 33 commands in the file, by group:

    <div class="no-sort" markdown>
    
    | Group | Commands |
    |-------|----------|
    | Your list | `systemctl` `journalctl` `sed` `awk` `grep` `tr` `sort` `uniq` `tee` `dig` |
    | Text and files | `find` `xargs` `cut` `wc` `head` `tail` `diff` `less` `tar` |
    | System | `lsblk` `dmesg` `systemd-analyze` `loginctl` |
    | Network | `ip` `ss` `curl` `ping` `ssh` `rsync` `nmcli` |
    | Permissions | `chmod` `chown` `stat` |
    
    </div>

    The file has **33** commands. Five more that were first suggested (`ps`, `kill`, `lsof`, `df`, `du`) were cut, and `ed` was dropped too.
    
## Descriptions from the man page database.

!!! desc "Descriptions from the man page database"

    `whatis` gives a one-line description for each command, but the first attempt returned the wrong pages for three of them:
    
    | Command | Wrong page picked | Why |
    |---------|-------------------|-----|
    | `head` | a C++ library page (`__gnu_pbds::...`) | same name, section 3 |
    | `ip` | `ip (7)`, the kernel IPv4 page | the command is `ip (8)` |
    | `awk` | `awk (1p)`, the POSIX page | Arch's awk is gawk |
    
    Two rules fixed it:
    
    1. Accept only an **exact name match** in **section 1 or 8** (the command sections).
    2. If a command has no page of its own, look up the page under the name its symlink points to. `awk` is a link to `/usr/bin/gawk`, so it uses gawk's description.
    
    ```bash
    #!/bin/bash
    # mytools-extras - print "name<TAB>description" for each command in ~/.config/mytools/extras.txt
    file="${MYTOOLS_EXTRAS:-$HOME/.config/mytools/extras.txt}"
    [ -f "$file" ] || exit 0
    look() { whatis "$1" 2>/dev/null | awk -v c="$1" '$1==c && $2 ~ /^\((1|8)\)$/ {sub(/^.*\([0-9a-z]+\) +- +/, ""); print; exit}'; }
    grep -v '^[[:space:]]*#\|^[[:space:]]*$' "$file" | while read -r c; do
      command -v "$c" >/dev/null || continue
      d=$(look "$c")
      [ -z "$d" ] && d=$(look "$(basename "$(readlink -f "$(command -v "$c")")")")
      printf '%s\t%s\n' "$c" "[admin] ${d:-everyday command}"
    done
    ```
    
    Each line comes out as `name<TAB>[admin] description`. The `[admin]` tag is part of the description, so you can type `admin` in `tools` to see just this group.
    
## Merging the lists.

!!! desc "Merging the lists"

    `mytools` adds the extras to the package list and removes duplicates by name (`awk -F'\t' '!seen[$1]++'`), so a command that is also an installed package appears once. This is the final `mytools`, including the Esc behaviour described below:
    
    ```bash
    #!/bin/bash
    explicit=$(comm -23 <(pacman -Qeq | sort) <(pacman -Qg | awk '{print $2}' | sort -u) \
      | grep -Ev '^(lib|lib32-|python-|perl-|ruby-|ttf-|otf-|xorg-|gst-|qt[0-9]|gtk[0-9]?-)|-libs$|-docs?$')
    bins=$(pacman -Ql $explicit | awk '{ if ($2 ~ /^\/usr\/bin\/[^\/]+$/) b[$1]=1; if ($2 ~ /\.desktop$/) d[$1]=1 } END { for (p in b) if (!(p in d)) print p }')
    pk=$(pacman -Qi $bins | awk '/^Name/ {n=$3} /^Description/ {sub(/^Description *: /,""); print n "\t" $0}')
    { printf '%s\n' "$pk"; mytools-extras; } | awk -F'\t' '!seen[$1]++' | sort \
    | column -t -s $'\t' \
    | fzf --header 'Enter: mandible | ^T: tldr | ^E: cheat | ^O: man' \
          --bind 'enter:execute(mytools-help mandible {1})' \
          --bind 'ctrl-t:execute(mytools-help tldr {1})' \
          --bind 'ctrl-e:execute(mytools-help cheat {1})' \
          --bind 'ctrl-o:execute(mytools-help man {1})' \
          --bind 'esc:transform:[[ -n $FZF_QUERY ]] && echo clear-query || echo abort' \
          --preview 'mytools-preview {1}' --preview-window=right:40%
    ```
    
## The preview pane.

!!! desc "The preview pane"

    The original preview asked pacman about a package called `ip`, which does not exist (the command belongs to `iproute2`), so almost every `[admin]` entry showed a pacman error. A small helper now decides what to show:
    
    - **A package:** install size, install date and the commands it installs.
    - **A plain command:** where it lives, where a symlink leads, and which package owns it.
    
    ```bash
    #!/bin/bash
    # mytools-preview <name> - preview pane text for a package or a plain command
    n="$1"
    if pacman -Qi "$n" >/dev/null 2>&1; then
      pacman -Qi "$n" | grep -E "^(Installed Size|Install Date)"
      echo
      pacman -Ql "$n" | grep " /usr/bin/." | awk '{print $2}'
    else
      p=$(command -v "$n")
      [ -z "$p" ] && { echo "not found on PATH"; exit 0; }
      r=$(readlink -f "$p")
      echo "Command: $p"
      [ "$r" != "$p" ] && echo "Links to: $r"
      owner=$(pacman -Qoq "$r" 2>/dev/null)
      [ -n "$owner" ] && echo "Package: $owner"
    fi
    ```
    
    For example `ip` shows `Command: /bin/ip`, `Links to: /usr/bin/ip` and `Package: iproute2`.
    
## Esc: Clear first, then quit.

!!! desc "Clear first, then quit"

    In the main list, Esc used to leave `tools` straight away, even in the middle of typing a search. In the multi-command picker it only closes the picker, which is why the two felt different. They are different windows: the picker is a second fzf on top of the main list, while typing a filter never opens anything.
    
    Since Esc is muscle memory, the main list now uses fzf's `transform` action:
    
    ```bash
    --bind 'esc:transform:[[ -n $FZF_QUERY ]] && echo clear-query || echo abort'
    ```
    
    If there is text in the search box, Esc clears it. If the box is already empty, Esc quits. This needs a reasonably recent fzf (0.74.5 here).
    
## Making the keys work on admin commands.

!!! desc "Making the keys work on admin commands"

    After the extras were added, pressing Ctrl+T on `dig` flashed the screen and returned to the list with nothing shown. The helper's first line asks `mytools-bin` which command to use. `mytools-bin` asked pacman for a package called `dig`. There is no such package (the command comes from `bind`), so it printed an empty line and the helper quietly exited.
    
    The fix is one line near the top of `mytools-bin`: if pacman knows no package of that name but the name is a command you can run, use the name itself.
    
    ```bash
    if [ -z "$bins" ] && command -v "$pkg" >/dev/null 2>&1; then echo "$pkg"; exit 0; fi
    ```
    
    It was added with `sed -i.bak '/^bins=/a ...'`, which keeps the old version as `mytools-bin.bak`. After that, Ctrl+T, Ctrl+E and Ctrl+O all work on the admin entries.
    
!!! tip "How it was found"

    Running the helper directly, outside `tools`, was the quickest test: `mytools-help tldr dig` printed nothing and returned to the prompt. A silent exit points at the first step, and the first step is the command lookup. Running a helper by itself removes fzf from the picture.
    
The [**next**](05-filling-the-gaps.md) page covers **filling the gaps**{.skyblue}, `cheat sheets`{.green}, and `tldr pages`{.green}.