---
icon: material/alert-outline
---

<div style="display: none;"><h1>Header</h1></div>

![](imgs/20260723-212259.png){: style="display: block; margin: 0 auto"}

<H2 style="text-align: center;"> LunarVim (LVIM) Quickstart & Cheat Sheet.</H2>

!!! desc "LunarVim"

    LunarVim is a pre-configured IDE layer built on top of Neovim. It brings the power and speed of a terminal editor while providing modern features like code completion, file trees, and language analysis right out of the box.
    
    !!! important "The Golden Rule of LVIM Configuration"
        Never modify files in `~/.local/share/lunarvim`.
        Always make your custom tweaks inside `~/.config/lvim/config.lua`.
        
    
---

### 🧭 Essential Core Shortcuts

!!! recommendation "Essential Core Shortcuts"
    LunarVim relies heavily on the **`<Space>`** key as the "Leader" key. Pressing space opens up a quick interactive menu at the bottom of your screen.
    
### 📁 General Navigation & UI

| Keystrokes | Action | Description |
| :--- | :--- | :--- |
| `<Space> + e` | Toggle File Explorer | Opens/closes the `NvimTree` side panel |
| `<Space> + f` | Find File | Search files globally using `Telescope` fuzzy finder |
| `<Space> + t` | Find Text | Search for specific words across your entire project |
| `<Space> + c` | Close Buffer | Safely closes the current open file tab |
| `j + k` | Exit Insert Mode | The custom shortcut we set to leave typing mode quickly |

### 🛠️ Code Editing & LSP Power Actions

| Keystrokes | Action | Description |
| :--- | :--- | :--- |
| `K` | Hover Info | Shows documentation/types for the word under cursor |
| `g + d` | Go to Definition | Jumps straight to where a variable/function is defined |
| `<Space> + l + r` | Rename Variable | Renames a variable safely across your whole project |
| `<Space> + l + f` | Format File | Manually trigger your formatter (Black/Prettier) |

---

### 📝 Markdown & HTML Workflow Pointers

!!! instruction "Markdown & HTML"
    Now that your configuration is running silently, here is exactly how to utilize your new IDE features for web development and note-taking.
    
    
    !!! dollar "Automatic Formatting"
        Every time you type `:w` to save, `python-black` handles your Python spacing, while `prettier` automatically cleans up and indents your HTML tags and Markdown columns.
        
    
### 🌐 Working with HTML

!!! deep-dive  "🌐 Working with HTML"

    * **Auto-Closing Tags:** Type an HTML tag like `<div>` and hit enter. The editor automatically generates `</div>` and balances your cursor in the middle.
    
    * **Tag Renaming:** If you change an opening tag from `<div>` to `<section>`, the matching closing tag will dynamically update itself.
    
### 📉 Working with Markdown

!!! grey "📉 Working with Markdown"
    * **Live Browser Preview:** When you have a `.md` file active, open the command line and run the plugin we added:
    
    ```vim
    :MarkdownPreview
    ```
    
    This spins up a localized server and launches a live-scrolling preview in your default web browser.
    
    * **Stop Preview:** When done, type:
    
    ```vim
    :MarkdownPreviewStop
    ```
    
---

### 🔗 Useful Documentation Links

!!! git "Useful Documentation Links"

    - [Official LunarVim Documentation](https://www.lunarvim.org/docs/installation) — The core manual for custom configuration profiles.
    
    - [LunarVim Keybindings Guide](https://www.lunarvim.org/docs/features/core-plugins-list) — Comprehensive map of every default keystroke available.
    
    - [Lazy.nvim GitHub Profile](https://github.com/folke/lazy.nvim) — Understand how your newly installed plugin architecture coordinates packages.
    
    - [Marksman LSP Manual](https://github.com/artempyanykh/marksman) — Learn about the advanced Markdown link, reference, and header completions active in your workspace.
    

