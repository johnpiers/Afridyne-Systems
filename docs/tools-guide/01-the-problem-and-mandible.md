---
status: new
icon: material/tools
---

<div style="display: none;"><h1>1. Problem and Mandible</h1></div>

<div markdown="1" align="center">

```{.text .tools-banner}
▀▀▀▀██▀▀▀▀   ▄▄▀▀▀▀▀▀▄▄   ▄▄▀▀▀▀▀▀▄▄   ██           ▄▄▀▀▀▀▀▀▀▀
    ██       ██      ██   ██      ██   ██             ▀▀▀▀▀▀▄▄
    ██       ▀▀▄▄▄▄▄▄▀▀   ▀▀▄▄▄▄▄▄▀▀   ██▄▄▄▄▄▄▄▄   ▄▄▄▄▄▄▄▄▀▀
```

</div>

## The problem, and what `Mandible`{.green} does and does not do! { .centered }

## The starting point.

!!! desc "The starting point"

    - A fresh Arch install is clean and minimal. Then, over months, you add terminal programs: monitors, TUIs, converters, little utilities found on sites like [Terminal Trove](https://terminaltrove.com/). A year later you can remember perhaps a third of them. Some were fun, some turned out to be genuinely handy, and all of them are invisible, because nothing on the system says "here is what you chose to add".
    
    - The idea was a **listing**: every tool I installed on purpose, with a one-line description, that I can scroll or search.
    
## Finding Mandible.

!!! pied-piper "Finding Mandible"

    - While browsing Terminal Trove I found [**mandible**](https://terminaltrove.com/mandible/) (project: [AS-FOSS/mandible](https://github.com/AS-FOSS/mandible)). It is a TUI reference for command-line tools, and it is a good one. Run `mandible git` and you get an explorable tree of every git command and subcommand, with descriptions, usage, positionals and flags for whatever is highlighted.
    
    - Its design point is that nothing is written by hand. Mandible runs the tool's own `--help` and parses the result, with parsers for the common help formats (clap, cobra, argparse and others), so it learns **frameworks** rather than individual tools. It was installed here from the AUR as `mandible-bin`.
    
!!! tip "What `Mandible`{.green} is good at"

    Reading one tool in depth. For a tool with a large command tree, such as `git`, `docker` or `cargo`, it is far nicer than scrolling `--help`.
    
## Where it stops short of the original problem.

!!! desc "Where it stops short of the original problem"

    The original goal was "show me what I have installed", and mandible is not built for that.
    
    | What I wanted | What Mandible does |
    |---------------|--------------------|
    | A list of tools on this machine | It always needs a tool name: `mandible <tool>`. With no name there is nothing to browse. |
    | To search across all my tools | Search works inside the tool you opened. The README describes two modes (`/` toggles between searching command **names** and searching **everything**), but both are scoped to that one tool. Searching for `git` while viewing `bat` finds nothing, by design. |
    | A way to remember what exists | It cannot help if you can't remember the name to give it. |
    
!!! info "A search misunderstanding, corrected"

    During testing I assumed Mandible's search only filtered the list on the left. It actually searches the loaded tool's own documentation in the right-hand pane. Neither guess was a fault: it simply has no cross-tool search.
    
    Two cosmetic quirks turned up too. Both are mandible's parser meeting an unusual help layout, not anything in the setup built here:
    
    <div class="steps" markdown>
    
    - **7-Zip** (`7z`): the help is laid out as `a : Add files to archive`, so mandible found the command letters but not their descriptions, and the left pane looked bare.
    - **`ddns-confgen`**: it does not accept `--help`. It prints an error followed by its usage, and mandible took that first error line as the description.
   
   </div>
    
    If either bothers you, `mandible --report <tool>` prints a paste-ready bug report for the project.
    
## A first attempt with the tools at hand.

!!! ex " A first attempt with the tools at hand"

    My first try was to feed mandible a filtered list of binaries:
    
    ```bash
    mandible $(find /usr/bin -maxdepth 1 -type f -size +1M -size -150M -not -name "*.*" -exec basename {} \; | sort -u | fzf)
    ```
    
    This scans every large binary in `/usr/bin`, which includes everything the system and its dependencies installed. It does not separate "what I chose" from "what came along", so it was not much help.
    
## The Decision.

!!! decision "The Decision"

    The package manager already knows exactly what was installed on purpose. So the plan became:
    
    <div class="steps" markdown>
    
    1. Ask **pacman** what was explicitly installed.
    2. Strip out what isn't a terminal tool.
    3. Show the rest in **fzf**, with descriptions.
    4. Hand off to **mandible** for the deep view, and add other sources of help (tldr, cheat, man) on other keys.
    
    </div>
    
    The [**next**](02-building-the-list.md) page covers steps [1](02-building-the-list.md/#step-1-what-did-i-install-on-purpose), [2](02-building-the-list.md/#step-2-keep-only-terminal-tools) and [3](02-building-the-list.md/#step-3-a-first-script).
    
