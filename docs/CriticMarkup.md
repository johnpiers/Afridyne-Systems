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
    
    * Standard Markdown fences (` ```text `), backslash escaping (`\`), and external text file snippets (`--8<span></span><--`) all fail because Critic processes the raw characters before standard layout engines can shield them.
    
    ```markdown
    <div class="highlight"><span class="filename">Text with suggested changes</span><pre><code>Text can be {<span></span>--deleted--} and replacement text {<span></span>++added++}. This can also be combined into {<span></span>~~one~>a single~~} operation. {<span></span>==Highlighting==} is also possible {<span></span>>>and comments can be added inline<<}.
    
    {<span></span>==
    
    Formatting can also be applied to blocks by putting the opening and closing tags on separate lines and adding new lines between the tags and the content.
    
    ==}</code></pre></div>
    ```

<div class="highlight"><span class="filename">Text with suggested changes</span><pre><code>Text can be {<span></span>--deleted--} and replacement text {<span></span>++added++}. This can also be combined into {<span></span>~~one~>a single~~} operation. {<span></span>==Highlighting==} is also possible {<span></span>>>and comments can be added inline<<}.

{<span></span>==

Formatting can also be applied to blocks by putting the opening and closing tags on separate lines and adding new lines between the tags and the content.

==}</code></pre></div>

Text can be {--deleted--} and replacement text {++added++}. This can also be combined into {~~one~>a single~~} operation. {==Highlighting==} is also possible {>>and comments can be added inline<<}.

{==

Formatting can also be applied to blocks by putting the opening and closing tags on separate lines and adding new lines between the tags and the content.

==}

### Why This Architecture Works Flawlessly

!!! desc "Why This Architecture Works Flawlessly"
    
    1. **Blinds the Preprocessor:** Because the build engine reads `{<span></span>--`, the sequential token matching pattern is broken. Critic completely ignores the box during its initial pass.
    
    2. **Invisible to the Browser:** When the browser compiles the code frame, empty span tags vanish completely, displaying a pristine `{--deleted--}` syntax string inside your theme viewport.
    
    3. **Pristine Clipboard Copies:** Because the span structure has no visible text properties, the clipboard copies the 100% correct raw markdown characters with both symbols perfectly intact.
    
    4. **Natural Execution:** When a user copies code out of that box and inserts it out in the open on a Critic-enabled site, it natively lights up into clean, visual deletions, additions, and paragraph blocks.


### Highlighting Changes (Incorrect Method)

!!! desc "Highlighting Changes (Incorrect Method)"

    The same block of code below, but without the `<div class="highlight"><span class="filename">` wrapper and without the `{<span></span>--` protection that blinds `pymdownx.critic`, demonstrates the failure mode directly. Left as a plain fenced code block, Critic's preprocessor reads and renders the syntax before the fence has any chance to shield it — the "raw" content shown below is already fully processed.

    This defeats the entire purpose of the code box. A copy button is pointless if the text it copies isn't the raw syntax the reader actually needs — they'd have to manually retype the correct source from scratch, which is precisely the problem this case study set out to solve.

    Note: the specific corruption observed wasn't a single character dropping from the closing tag as first suspected during troubleshooting — Critic actually consumed forward past the missing closer, collapsing "deleted" and the entire next clause together before the run finally terminated.

    When [Critic] is enabled, [Critic Markup] can be used, which adds the ability to highlight suggested changes, as well as add inline comments to a document:

``` title="Text with suggested changes"
    Text can be {--deleted--} and replacement text {++added++}. This can also be combined into
    {~~one~>a single~~} operation. {==Highlighting==} is also possible and
    {>>comments can be added inline<<}.
    {==
    Formatting can also be applied to blocks by putting the opening and closing
    tags on separate lines and adding new lines between the tags and the content.
    ==}
```

[Critic]:https://github.com/jaywhj/mkdocs-materialx/blob/main/docs/setup/extensions/python-markdown-extensions.md#critic
[Critic Markup]:https://github.com/CriticMarkup/CriticMarkup-toolkit