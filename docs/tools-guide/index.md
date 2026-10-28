---
icon: material/tools
---

<div style="display: none;"><h1>Overview</h1></div>

<div markdown="1" align="center">

```{.text .tools-banner}
▀▀▀▀██▀▀▀▀   ▄▄▀▀▀▀▀▀▄▄   ▄▄▀▀▀▀▀▀▄▄   ██           ▄▄▀▀▀▀▀▀▀▀
    ██       ██      ██   ██      ██   ██             ▀▀▀▀▀▀▄▄
    ██       ▀▀▄▄▄▄▄▄▀▀   ▀▀▄▄▄▄▄▄▀▀   ██▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▀▀
```

</div>


### `Tools:`{.green} A searchable memory for the `Terminal Tools`{.skyblue} you  installed. { .centered }


!!! desc "Tools"

    - `tools`{.green} (The command is `mytools`{.green}, with `alias tools=mytools`{.green} in `~/.zshrc`{.green} ) is a small fzf-based browser for the command-line and TUI programs you chose to install on Arch Linux. It lists them with their descriptions, lets you search by name or by description, and puts four kinds of help one key away.
    
    - It exists because a year after a clean Arch install you can no longer remember what you added. This set of pages records how it was found, built, wired together and finished, including the mistakes along the way.
    
!!! info "Built over four days"

    22 to 26 October 2026, on Arch Linux with GNOME on Wayland, in Tilix with zsh. Everything is plain bash plus tools that are already on the machine. No daemons, no services, nothing runs in the background.
    
## What it does.

!!! recommendation "What it does"

    | Key | Action |
    |-----|--------|
    | type | Filter the list. fzf searches the name **and** the description, so `monitor` or `audio` finds tools whose names don't contain those words. |
    | **Enter** | Open the tool in [mandible](https://terminaltrove.com/mandible/), an interactive TUI reference for any command's flags and subcommands. |
    | **Ctrl+T** | Show the tldr page (short practical examples). |
    | **Ctrl+E** | Show the cheat sheet from `cheat` (your own sheets live in `~/cheat/personal`). |
    | **Ctrl+O** | Show the man page in colour, or the colour `--help` if the tool has no man page. |
    | **Esc** | Clear the search text. If the search box is already empty, quit. |
    
    Packages that install several commands (`bind` installs 29, none of them called `bind`) show a small picker so you choose which command you mean.
    
## What is in the list?

!!! abstract "What is in the list?"

    <div class="steps" markdown>
    
    - Every package you installed **on purpose** (native, chaotic-aur and AUR), after removing group members, libraries, fonts and similar plumbing.
    - Only packages that put a program in `/usr/bin` **and** have no desktop launcher, so GUI apps stay out.
    - 33 everyday admin commands (`systemctl`, `journalctl`, `sed`, `dig`, `ip` and so on) from an editable text file, marked `[admin]`.
    
    </div>
    
    At the end of the project the audit counted 255 entries: 200 single-command tools and 55 multi-command packages. For the 200, **156 have a man page, a tldr page and a cheat sheet**. The other 44 are covered by the colour `--help` fallback for man, plus a handful of obscure tools that were deliberately left alone.
    
## The Pages.

!!! assumption "The Pages"

    <div class="steps" markdown>
    
    1. [The problem, and what mandible does and doesn't do](01-the-problem-and-mandible.md)
    2. [Building the first version](02-building-the-list.md)
    3. [Wiring in mandible, tldr, cheat and man](03-wiring-in-the-help-keys.md)
    4. [Admin commands, the preview pane and Esc](04-admin-commands-and-polish.md)
    5. [Filling the gaps: cheat sheets and tldr pages](05-filling-the-gaps.md)
    6. [Lessons, pitfalls and troubleshooting](06-lessons-and-troubleshooting.md)
    
    </div>
    
## Files at a glance

!!! education "Files at a glance"

    | File | Purpose |
    |------|---------|
    | `~/.local/bin/mytools` | The main fzf list and key bindings. |
    | `~/.local/bin/mytools-bin` | Works out which command a package really installs, or asks when there are several. |
    | `~/.local/bin/mytools-help` | Runs mandible, tldr, cheat or man for the chosen entry. |
    | `~/.local/bin/mytools-extras` | Builds the `[admin]` lines from the text file below. |
    | `~/.local/bin/mytools-preview` | Text for the right-hand preview pane. |
    | `~/.local/bin/mytools-audit` | Read-only report of which tools lack man, tldr or cheat coverage. |
    | `~/.config/mytools/extras.txt` | The editable list of admin commands. |
    | `~/cheat/personal/` | Your cheat sheets, one file per command. |
    | `~/.local/share/mytools/tldr/` | Your own tldr-style pages, checked before the official ones. |
    | `~/mk-tldr.sh` | One-off generator that builds tldr pages from the cheat sheets. |
    
## Requirements

!!! decision "Requirements"

    `pacman`{.red}, `fzf`{.green}, `bat`{.red}, `man-db`{.green} (for `whatis`{.red} ), `column`{.green} (util-linux), `tldr`{.red} (the Python client), `cheat`{.skyblue} and `mandible`{.green} (installed here as the AUR package `mandible-bin`{.green}<!-- --> ).
    
## Rebuilding from scratch.

!!! desc "Rebuilding from scratch"

    Install the requirements, then create the files in this order. Each page shows the final code for its part.
    
    <div class="steps" markdown>
    
    1. `~/.local/bin/mytools-bin`{.green}, `mytools-help`{.green}, `mytools-extras`{.green}, `mytools-preview`{.green} [Page 3](03-wiring-in-the-help-keys.md) and [Page 4](04-admin-commands-and-polish.md).
    2. `~/.config/mytools/extras.txt`{.green} [Page 4](04-admin-commands-and-polish.md).
    3. `~/.local/bin/mytools`{.green} [Page 4](04-admin-commands-and-polish.md) shows the final version).
    4. Make them executable with `chmod +x ~/.local/bin/mytools*`{.green}.
    5. Add `alias tools=mytools`{.green} to `~/.zshrc`{.green}<!-- -->.
    6. Optional: `mytools-audit`{.green}, your cheat sheets and `mk-tldr.sh`{.green} [Page 5](05-filling-the-gaps.md)
    
    </div>
    
