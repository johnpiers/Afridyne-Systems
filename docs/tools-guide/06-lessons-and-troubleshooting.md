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

# Lessons, pitfalls and troubleshooting. { .centered }

## What worked.

!!! desc "What worked"

    <div class="steps" markdown>
    
    - **Ask the package manager, not the filesystem.** `pacman -Qe` plus a few filters knows exactly what you chose. Scanning `/usr/bin` can't.
    - **Hand off to a specialist.** Mandible already parses help text better than a shell script could. `tools` only finds the tool; mandible shows it.
    - **Run the pieces by hand.** Every helper can be run on its own (`mytools-bin bind`, `mytools-help tldr dig`, `mytools-preview ip`). When something broke, running the small piece outside fzf found the fault in one step.
    - **Change one thing, then test.** The keys were connected one at a time. Rewriting several things at once cost more time than it saved.
    - **Generate content from the tool's real help.** It keeps sheets accurate, and the audit shows what is still missing.
    
    </div>
    
## What went wrong, and why.

| Symptom | Cause | Fix |
|---------|-------|-----|
| Sudo password prompt and lockout in a script that has no `sudo` | `~/.zshrc` aliased `pacman` to `sudo pacman --color auto` (ArcoLinux template). Interactive zsh used it; the bash script did not. | Comment out the alias; verify with `zsh -ic 'type pacman'` in a fresh shell. |
| "bash says no wrapper" test passed but alias existed | `bash -c 'type -a pacman'` cannot see zsh aliases. | Test in the shell that has the problem. |
| Typing `monitor` or `audio` found nothing | list held only names | add descriptions as a second column so fzf matches them |
| Ragged description column | tabs don't align | `column -t -s $'\t'` |
| Ctrl+T, Ctrl+E, Ctrl+O looked plain and sat at the bottom | output piped into `less`; tools drop colour in a pipe | run tools directly; set `MANPAGER` inside the helper |
| Enter on `bind` opened `arpaname` | helper took the first command alphabetically | picker for multi-command packages |
| Cancelling the picker printed errors | empty name passed on | `[ -z "$cmd" ] && exit 0` |
| Short man pages flashed and vanished | `bat` exits at once when output fits on screen | wait for a keypress when the page is shorter than the terminal |
| Preview pane showed an error for `[admin]` entries | preview asked pacman about a non-package | `mytools-preview` |
| `whatis` picked wrong pages (`head`, `ip`, `awk`) | took the first match | exact name, section 1 or 8, fall back to the symlink target |
| Ctrl+T on `dig` flashed and did nothing | `mytools-bin` found no package called `dig` and printed an empty line | fall back to the name itself when it is a runnable command |
| Audit still said 63 tldr pages missing after 55 were written | audit only searched the official cache | add `~/.local/share/mytools/tldr` to the audit |
| `zsh: correct 'page' to 'pg' [nyae]?` | a script was **pasted into** zsh instead of being run with `bash`; zsh's spelling correction saw a function called `page` | answer `a` (abort), then save the file and run it with `bash file.sh` |

## Habits that kept it safe.

!!! desc "Habits that kept it safe"

    <div class="steps" markdown>
    
    - Nothing was run that could start a service, and nothing destructive ran without a visible warning.
    - `.zshrc` aliases were commented out with `#`, not deleted.
    - The safe writer `w()` and the "never overwrite" rule in `mk-tldr.sh` make every generating script safe to run twice.
    - Helper edits that change an existing file use `sed -i.bak`, which keeps the previous version beside it.
    - `ls` is aliased to `colorls` on this machine, so commands in these pages avoid it.
    
    </div>
    
## Troubleshooting a key that does nothing.

!!! desc "Troubleshooting a key that does nothing"

    <div class="steps" markdown>
    
    1. Run the helper directly: `mytools-help tldr <name>`. If that prints nothing and returns to the prompt, the command lookup failed.
    2. Run `mytools-bin <name>`. It should print one command name, or open the picker.
    3. Run the underlying tool by hand: `tldr <command>`, `cheat <command>`, `man <command>`.
    4. If a page flashes and disappears, it was shorter than the terminal; check the `pause` logic in `mytools-help`.
    5. If the list is empty or slow, run the first lines of `mytools` on their own. Each step prints something you can check.
    
    </div>
    
## Maintenance.

!!! desc "Maintenance"

    <div class="steps" markdown>
    
    - **Add or remove admin commands:** edit `~/.config/mytools/extras.txt`. It is read every time `tools` starts.
    - **Check coverage:** run `mytools-audit`. It is read-only.
    - **New tool installed:** it appears in the list on its own. To give it a sheet, write one in `~/cheat/personal/` and, optionally, run `bash ~/mk-tldr.sh --show <command>` to see a tldr page built from it.
    - **Mandible oddities:** `mandible --report <tool>` prints a ready-made bug report for the project.
    
    </div>
    
