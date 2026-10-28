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


# Filling the gaps: cheat sheets and tldr pages. { .centered }

!!! desc "Four Help `keys`"

    With four help keys in place, the obvious next question was: how many tools actually have something to show? A key that opens "No page found" is not much use. The goal became **every entry has a man page, a tldr page and a cheat sheet**, kept short.
    
## Step 1: 

!!! desc "Measure, with a read-only audit"

    `mytools-audit` walks the same list as `tools` and checks each entry in three places. It changes nothing and writes a tab-separated report to `~/.cache/mytools/audit.tsv` (columns: package, command, man y/n, tldr y/n, cheat y/n). Packages with several commands are marked `MULTI` and skipped.
    
!!! desc "mytools-audit"

    ```bash
    #!/bin/bash
    # mytools-audit - report which tools lack a man page, tldr page or cheat sheet (read-only)
    out="${1:-$HOME/.cache/mytools/audit.tsv}"
    mkdir -p "$(dirname "$out")"
    explicit=$(comm -23 <(pacman -Qeq | sort) <(pacman -Qg | awk '{print $2}' | sort -u) \
      | grep -Ev '^(lib|lib32-|python-|perl-|ruby-|ttf-|otf-|xorg-|gst-|qt[0-9]|gtk[0-9]?-)|-libs$|-docs?$')
    pkgs=$(pacman -Ql $explicit | awk '{ if ($2 ~ /^\/usr\/bin\/[^\/]+$/) b[$1]=1; if ($2 ~ /\.desktop$/) d[$1]=1 } END { for (p in b) if (!(p in d)) print p }')
    cheats=$(cheat -l 2>/dev/null | awk 'NR>1 {print $1}' | sort -u)
    tldrs=$(find ~/.cache/tldr/pages/common ~/.cache/tldr/pages/linux ~/.local/share/mytools/tldr -name '*.md' 2>/dev/null | sed 's|.*/||; s|\.md$||' | sort -u)
    { printf '%s\n' $pkgs; grep -v '^[[:space:]]*#\|^[[:space:]]*$' ~/.config/mytools/extras.txt; } | sort -u | while read -r n; do
      list=$(pacman -Ql "$n" 2>/dev/null | awk '$2 ~ /^\/usr\/bin\/[^\/]+$/ {k=split($2,a,"/"); print a[k]}')
      if [ -z "$list" ]; then cmd="$n"
      elif grep -qx -- "$n" <<<"$list"; then cmd="$n"
      elif [ "$(grep -c . <<<"$list")" -eq 1 ]; then cmd="$list"
      else cmd="MULTI"; fi
      if [ "$cmd" = MULTI ]; then m=-; t=-; c=-; else
        man -w "$cmd" >/dev/null 2>&1 && m=y || m=n
        grep -qx -- "$cmd" <<<"$tldrs" && t=y || t=n
        grep -qx -- "$cmd" <<<"$cheats" && c=y || c=n
      fi
      printf '%s\t%s\t%s\t%s\t%s\n' "$n" "$cmd" "$m" "$t" "$c"
    done > "$out"
    echo "tldr pages found: $(grep -c . <<<"$tldrs"), cheat sheets found: $(grep -c . <<<"$cheats")"
    awk -F'\t' '{n++} $2=="MULTI" {multi++; next} {s++; if($3=="n")nm++; if($4=="n")nt++; if($5=="n")nc++; if($3=="y"&&$4=="y"&&$5=="y")all++} END {printf "entries: %d (multi-command packages skipped: %d)\nchecked: %d\nno man page: %d\nno tldr page: %d\nno cheat sheet: %d\nall three present: %d\n", n, multi, s, nm, nt, nc, all}' "$out"
    ```
    
    ---
    
    The first run showed where the gaps were:
    
    | Checked | First run | Final run |
    |---|---|---|
    | Entries | 255 | 255 |
    | Multi-command packages (skipped) | 55 | 55 |
    | Checked | 200 | 200 |
    | No man page | 42 | 42 |
    | No tldr page | 63 | 4 |
    | No cheat sheet | about 150 | 4 |
    | All three present | not counted | **156** |
    
!!! info "Where the tldr pages are looked up"
    - The audit searches tldr's own cache (`~/.cache/tldr/pages/common` and `/linux`) **and** `~/.local/share/mytools/tldr`. The second folder was added to the audit after the custom pages were created, which is why "No tldr page" first still read 63 and then dropped to 8. The pages existed; the audit just wasn't looking there.
    
    - The 42 with no man page are not a problem: `Ctrl+O` shows the tool's colour `--help` for them instead.
    
## Where each kind of page lives.

!!! desc "Where each kind of page lives"

    | Kind | Location | Notes |
    |------|----------|-------|
    | man | the system | nothing to write. |
    | cheat | `~/cheat/personal/<command>` | one plain-text file per command, read by `cheat`. |
    | tldr | official cache, plus `~/.local/share/mytools/tldr/<command>.md` | the second folder holds your own pages and is checked first by `mytools-help`. |
    
    !!! warning "Why custom tldr pages are not in ~/.cache"
    
        `tldr -u` and `tldr -k` rewrite or clear `~/.cache/tldr`. A page placed there could vanish on the next update, so your own pages live under `~/.local/share` instead. `tldr -r <file>` renders a local Markdown file with the normal tldr colours.
        
## Step 2: Cheat sheets, generated from real help output.

!!! desc "Cheat sheets, generated from real help output"

    - A cheat sheet is a short file: a small header, then a `#`{.green} comment line followed by the command it describes. Placeholders sit in `<angle brackets>`{.green}. For example `~/cheat/personal/dig`{.green}:
        
    ```text
    ---
    syntax: bash
    tags: [ linux, dns, network ]
    ---
    # dig does not understand --help; use dig -h for the full option list
    # Usage: dig [@global-server] [domain] [q-type] [q-class] {q-opt}
    
    # Look up a domain
    dig <domain>
    
    # Ask a specific server
    dig @<server> <domain>
    
    # Ask for a specific record type
    dig <domain> <MX>
    ```
    
    ---
    
    - The rule for content was: **only what the tool's own help says**. Writing flags from memory invites invented options. The workflow ran in batches of about ten tools:
    
    <div class="steps" markdown>
    
    1. A command on the machine picks the next ten tools that still have no cheat sheet and saves each one's `--help`{.green} to a text file.
    2. That file was attached to the chat, and the sheets were written from it.
    3. The sheets arrived as one script, `batchN.sh`{.green}, run with `bash`{.green}, which wrote the files and then printed `cheat -l`{.green} for those names so each batch could be confirmed.
    
    </div>
    
    The command that picked the batch:
    
    ```bash
    mytools-audit >/dev/null
    awk -F'\t' '$5=="n" && $2!="MULTI" && $2!~/aarch64|^(aur|expect|gpm|audispd-zos-remote|clonezilla|iptraf-ng|inxi|mpc|os-prober|qbootctl)$/ {print $2}' ~/.cache/mytools/audit.tsv | head -10 > ~/next10.txt
    for c in $(cat ~/next10.txt); do
      echo "=== $c ==="
      timeout 5 $c --help </dev/null 2>&1 | head -40
    done | sed 's/\x1b\[[0-9;]*m//g' > ~/sheets.txt
    cat ~/next10.txt
    ```
    
    - `timeout 5`{.green} stops anything that waits for input, `</dev/null`{.green} stops it reading the terminal, and the `sed`{.skyblue} removes colour codes so the file stays readable. Names in the `$2!~`{.green} list were skipped on purpose (see below).
    
### The safe writer.

!!! desc "The safe writer"

    Every batch script began with a small function that **refuses to overwrite** an existing sheet:
    
    ```bash
    w() { if [ -e "$HOME/cheat/personal/$1" ]; then echo "exists, skipped: $1"; cat >/dev/null; else cat > "$HOME/cheat/personal/$1"; fi; }
    ```
    
    That kept the two sheets written by hand earlier (`aurdex`{.skyblue} and `tar`{.skyblue}) untouched, and made it safe to re-run a batch.
    
### Rules that kept the sheets safe and honest.

!!! desc "Rules that kept the sheets safe and honest"

    - A `# WARNING:`{.red} comment sits above every command that destroys or overwrites data (`mkfs`{.red}, `dd`{.red}, partition tools, mirrorlist writers, restore commands).
    - Commands that rewrite the system (`pacman -Rns`{.red}, mirrorlist replacement) are shown in their print-only form first.
    - If the tool printed help that was cut short, or only a usage line, the sheet says so and points at `--help`{.green} rather than guessing.
    - Options that came from general knowledge, not the tool's help, are labelled as such at the top of the sheet.
    - Tools that need root or open an interactive screen were not run to find out more.
    
### Surprises while collecting help.

!!! desc "Surprises while collecting help"

    | Tool | What happened |
    |------|---------------|
    | `dig`, `nginx`, `nmon`, `lostfiles` | do not understand `--help`; their usage still printed. |
    | `sl` | `sl --help` simply runs the steam locomotive. Harmless, but it filled the capture file with terminal escape codes. |
    | `lolcat` | its help came out in rainbow colour codes, hence the `sed` colour strip. |
    | `inxi` | refuses to print help when its input isn't a terminal, so `</dev/null` broke it. Running it plainly worked. |
    | `os-prober`, `clonezilla`, `iptraf-ng`, `qbootctl` | only run as root, so nothing useful printed. |
    
## Step 3: tldr pages, generated from the cheat sheets.

!!! desc "tldr pages, generated from the cheat sheets"

    Rather than repeat the whole process for tldr, a small script builds each missing page **from the cheat sheet that already exists**. Each page gets:
    
    <div class="steps" markdown>
    
    - a one-line description from `whatis`{.green} (or the sheet's first comment if there is none);
    - up to eight examples, one command per comment;
    - `<placeholder>`{.green} rewritten as `{{placeholder}}`{.green}, which is tldr's format;
    - nothing from a `WARNING`{.red} block, so destructive commands never become examples.
    
    </div>
    
    Run `bash ~/mk-tldr.sh --show dig` to print one page without writing anything. Run `bash ~/mk-tldr.sh` to write all the pages that are missing. It never overwrites an existing page.
    
    ```bash
    #!/bin/bash
    # mk-tldr.sh - builds short tldr-style pages from your cheat sheets
    #   bash mk-tldr.sh --show <cmd>   print one page on screen (writes nothing)
    #   bash mk-tldr.sh                write pages for every command whose tldr page is missing
    # Pages go to ~/.local/share/mytools/tldr/<cmd>.md ; existing pages are never overwritten.
    cheatdir="$HOME/cheat/personal"
    outdir="$HOME/.local/share/mytools/tldr"
    audit="$HOME/.cache/mytools/audit.tsv"

    page() {
      local cmd="$1" f="$cheatdir/$1" desc
      [ -f "$f" ] || return 1
      desc=$(whatis -s 1,8 "$cmd" 2>/dev/null | awk -v c="$cmd" '$1==c {sub(/^[^-]*- */,""); print; exit}')
      [ -z "$desc" ] && desc=$(awk '/^---$/ {n++; next} n>=2 && /^# / {sub(/^# */,""); print; exit}' "$f")
      desc="${desc%%. Usage*}"; desc="${desc%% Usage:*}"; desc="${desc%.}"
      printf '# %s\n\n> %s.\n' "$cmd" "$desc"
      awk '
        /^---$/ { fm++; next }
        fm < 2 { next }
        /^#/ { d=$0; sub(/^# */,"",d); next }
        /^[[:space:]]*$/ { next }
        {
          if (d == "" || n >= 8) next
          if (d ~ /^(Usage|Note|WARNING|Options|Help|Version|The |Only |These )/ || d ~ /WARNING|Usage:/) { d=""; next }
          sub(/[.:]$/,"",d)
          sub(/[[:space:]]+#.*$/,"")
          printf "\n- %s:\n\n`%s`\n", d, $0
          n++; d=""
        }
      ' "$f" | sed -E 's/<([^<> ]+)>/{{\1}}/g'
    }

    if [ "$1" = "--show" ]; then page "$2"; exit; fi

    mkdir -p "$outdir"
    made=0; skipped=0
    while IFS=$'\t' read -r pkg cmd man tldr cheat; do
      [ "$tldr" = "n" ] || continue
      [ -n "$cmd" ] && [ "$cmd" != "MULTI" ] && [ "$cmd" != "cmd" ] || continue
      [ -e "$outdir/$cmd.md" ] && continue
      if page "$cmd" > "$outdir/$cmd.md.tmp" 2>/dev/null && [ -s "$outdir/$cmd.md.tmp" ]; then
        mv "$outdir/$cmd.md.tmp" "$outdir/$cmd.md"; made=$((made+1))
      else
        rm -f "$outdir/$cmd.md.tmp"; echo "no cheat sheet for: $cmd"; skipped=$((skipped+1))
      fi
    done < "$audit"
    echo "pages written: $made, skipped: $skipped"
    ```
    
    ---
    
    A generated page looks like this:
    
    ```bash
    # dig
    
    > DNS lookup utility.
    
    - Look up a domain:
    
    `dig {{domain}}`
    
    - Ask a specific server:
    
    `dig @{{server}} {{domain}}`
    ```
    
    The first run wrote **55** pages. Seven were skipped because those tools have no cheat sheet to build from.
    
## Skipped on purpose.

A handful of tools have neither a cheat sheet nor a tldr page, deliberately:

| Tool | Reason |
|------|--------|
| `aarch64-linux-gnu-gcc`{.green}<!-- --> | a cross compiler with a huge option list. |
| `audispd-zos-remote`{.green}<!-- --> | printed nothing. |
| `qbootctl`{.green}<!-- --> | root only, obscure. |
| `set-wireless-regdom`{.green}<!-- --> | printed nothing. |

For five more that couldn't be probed ( `expect`{.green}, `iptraf-ng`{.green}, `os-prober`{.green}, `clonezilla`{.green}, `aur`{.green} ) short sheets were written from general knowledge, each labelled as such at the top.

## Still open.

!!! desc "Still open"

    - The 55 **multi-command packages** (like `bind`{.skyblue}, with 29 commands) are not covered by the audit. Most of them have man pages, and the picker lets you reach each command's pages one at a time.
    
    - If they are ever tackled, the natural way is to audit each command in each package rather than the package as a whole.
    
The [**next**](06-lessons-and-troubleshooting.md) page covers **lessons**{.skyblue}, `pitfalls`{.red}, and `troubleshooting`{.green}.