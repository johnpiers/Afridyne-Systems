---
tags:
  - CriticMarkup
  - Code Block Conflict
  - Troubleshooting
  - pymdownx.critic
  - extension

icon: material/computer-desktop-repair-icon
---

<div style="display: none;"><h1>CriticMarkup</h1></div>

![](imgs/20260821-151644.png){: style="display: block; margin: 0 auto"}

<H2 style="text-align: center;">Case Study: Solving the CriticMarkup Code Block Conflict in MkDocs</H2>
 

## 1. The Core Problem 

!!! desc "The Core Problem"
    
    When the `pymdownx.critic` extension is enabled globally, it runs at the absolute beginning of the MkDocs build pipeline as a text preprocessor. 
    
    Because it operates at stage zero, it aggressively scans the entire file line-by-line. If it detects raw token structures like `{<span></span>--` or `{<span></span>++`, it instantly intercepts them and parses them into live HTML tags. 
    
    This behavior completely broke the copyable code containers:
    
    * It rendered live color blocks *inside* the code boxes instead of showing raw text syntax.
    
    * It corrupted the strings copied to the clipboard by stripping trailing sequential symbols (e.g., matching `{<span></span>--deleted--}` into a broken `{<span></span>--deleted-}`).
    
    * Standard Markdown fences (`` `text ``), backslash escaping (`\`), external text file snippets (`--8<pre><code>`) combined with an empty `<span></span>` tag inserted directly between the opening bracket and the syntax character.
    
    ```markdown
    <div class="highlight"><span class="filename">Text with suggested changes</span><pre><code>Text can be {<span></span>--deleted--} and replacement text {<span></span>++added++}. This can also be combined into {<span></span>~~one~>a single~~} operation. {<span></span>==Highlighting==} is also possible {<span></span>>>and comments can be added inline<<}.
    
    {<span></span>==
    
    Formatting can also be applied to blocks by putting the opening and closing tags on separate lines and adding new lines between the tags and the content.
    
    ==}</code></pre></div>
    ```

### Why This Architecture Works Flawlessly

!!! desc "Why This Architecture Works Flawlessly"
    
    1. **Blinds the Preprocessor:** Because the build engine reads `{<span></span>--`, the sequential token matching pattern is broken. Critic completely ignores the box during its initial pass.
    
    2. **Invisible to the Browser:** When the browser compiles the code frame, empty span tags vanish completely, displaying a pristine `{--deleted--}` syntax string inside your theme viewport.
    
    3. **Pristine Clipboard Copies:** Because the span structure has no visible text properties, the clipboard copies the 100% correct raw markdown characters with both symbols perfectly intact.
    
    4. **Natural Execution:** When a user copies code out of that box and inserts it out in the open on a Critic-enabled site, it natively lights up into clean, visual deletions, additions, and paragraph blocks.

