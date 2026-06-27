---
icon: simple/materialformkdocs
---

![](imgs/20260601-163710.png){ .center-image }

<H1 style="text-align: center;"> Icon & Emoji Reference Database</H1>

!!! desc "Official Master Catalog"

    To search through thousands of additional full-color emojis, FontAwesome brands, and native Material design vectors, use the official master catalog:

<a href="https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/" target="_self" class="md-button md-button--primary">👉 Open Official Icon Search Database</a>


<div class="grid cards cols-3" markdown>

-   <span style="color: #00A99A">:material-material-design:</span> **Material Design**
    [:octicons-arrow-right-24: Go to](https://pictogrammers.com/library/mdi/){ .md-button style="border-color: #00A99A; color: #00A99A" }

    :material-vector-square: Material Design Icons.

-   <span style="color: #00A99A">:fontawesome-brands-font-awesome:</span> **FontAwesome**
    [:octicons-arrow-right-24: Go to](https://fontawesome.com/search?m=free){ .md-button style="border-color: #00A99A; color: #00A99A" }

    :fontawesome-brands-font-awesome: Font Awesome Icons.

-   <span style="color: #00A99A">:octicons-mark-github-16:</span> **Octicons**
    [:octicons-arrow-right-24: Go to](https://octicons.github.com/){ .md-button style="border-color: #00A99A; color: #00A99A" }

    :octicons-mark-github-16: Octicons Icons.

-   <span style="color: #ED1B23">:simple-simpleicons:</span> **Simple Icons**
    [:octicons-arrow-right-24: Go to](https://simpleicons.org/){ .md-button style="border-color: #ED1B23; color: #ED1B23" }

    :simple-simpleicons: Simple Icons.

-   <span style="color: #ED1B23">:simple-lucide:</span> **Lucide**
    [:octicons-arrow-right-24: Go to](https://lucide.dev/){ .md-button style="border-color: #ED1B23; color: #ED1B23" }

    :simple-lucide: Lucide Icons.

-   <span style="color: #ED1B23">:material-arrow-u-left-top:</span> **MaterialX-MkDocs**
    [:octicons-arrow-right-24: Return to](index.md){ .md-button style="border-color: #ED1B23; color: #ED1B23" } 

    :material-arrow-u-left-top: MaterialX-MkDocs.

</div>

---

## [Search](https://squidfunk.github.io/mkdocs-material/reference/icons-emojis/)

<div class="mdx-iconsearch" data-mdx-component="iconsearch">
  <!-- Interactive Navigation Search Row Bar -->
  <div class="mdx-iconsearch__bar">
    <input class="md-input md-input--stretch mdx-iconsearch__input" placeholder="Search Icons Emojis" data-mdx-component="iconsearch-query" />
    <div class="mdx-iconsearch-result__meta" data-mdx-component="iconsearch-meta"></div>
    <select
      class="mdx-iconsearch-result__select"
      data-mdx-component="iconsearch-select"
    >
      <option value="all" selected>All</option>
      <option value="icons">Icons</option>
      <option value="emojis">Emojis</option>
    </select>
  </div>
  
  <!-- Content Results Area Box -->
  <div class="mdx-iconsearch-result" data-mdx-component="iconsearch-result">
    <ol class="mdx-iconsearch-result__list"></ol>
  </div>
</div>

---

## Icon Search Fix Summary

### Afridyne Systems - MaterialX MkDocs

---

### The Problem

!!! important "`The Problem`"

    The icon search was working perfectly on the local site but broken on the live GitHub Pages site. The icons were showing as black squares instead of rendering correctly. The root cause was a combination of two issues:
    
    1. **Wrong path construction** - The JavaScript was building icon paths using `["", "assets", "local_icons", item.path]` which produced `/assets/local_icons/` (an absolute path). 
    On GitHub Pages your site lives at `https://johnpiers.github.io/Afridyne-Systems/` so the browser was looking for icons at `https://johnpiers.github.io/assets/local_icons/` — the wrong place.
    
    2. **Wrong rendering method** - The JavaScript was using a CSS `mask` approach to display the SVG icons. This is unreliable across browsers and environments. Since all the SVGs already had `fill="currentColor"` built in, a simple `<img>` tag was all that was needed.
    
---

## The Fix — Three Changes

### 1. `iconsearch.js`

!!! deep-dive "`docs/javascripts/iconsearch.js`"

    **Find this section (around line 153767):**

    ```javascript
    } else {
      const maskParts = ["", "assets", "local_icons", item.path];
      const localUrl = maskParts.join("/");
      visualHtml = `<div style="width: 24px; height: 24px; background-color: currentColor; 
      display: inline-block; vertical-align: middle; 
      -webkit-mask: url('${localUrl}') no-repeat center / contain; 
      mask: url('${localUrl}') no-repeat center / contain;"></div>`;
    }
    ```

    **Replace with:**

    !!! desc "Replace with Code Below"

        ```javascript
        } else {
          const localUrl = "https://johnpiers.github.io/Afridyne-Systems/assets/local_icons/" + item.path;
          visualHtml = `<img src="${localUrl}" style="width: 24px; height: 24px;" />`;
        }
        ```

    **What this does:**

    - Uses the full absolute GitHub Pages URL so the path is always correct
      regardless of which page the search appears on
    - Switches from CSS mask to a simple `<img>` tag which is far more reliable

---

### 2. `custom.css`

!!! deep-dive "`docs/styles/custom.css`"

    **Add these lines** (before the last block in the file):

    ```css
    /* Dark mode: invert local SVG icons only */
    [data-md-color-scheme="slate"] .mdx-iconsearch-result__item img[src*="local_icons"] {
      filter: invert(1);
    }
    ```
    
    ---
    
    **What this does:**
    
    - In dark mode, inverts the black SVG icons to white so they are visible
    
    - The `[src*="local_icons"]` selector means it ONLY targets local icons, leaving the full colour emojis completely untouched


---

### 3. `Conflicting CSS`

!!! desc "`Remove old conflicting CSS`"

    - If you had any old CSS block in `custom.css` that referenced mask-based icon rendering (anything with `mask-image`, `div[style*="url("]`, or the old `/Afridyne-Systems/assets/local_icons/` content fallback), remove it entirely as it will conflict with the new approach.
    
---

## The Result

| Mode | Icons | Emojis |
|------|-------|--------|
| Light | ✅ Black SVGs render correctly | ✅ Full colour |
| Dark | ✅ White SVGs (inverted) render correctly | ✅ Full colour unchanged |

---

#### Git Commands Used

!!! desc "`Git Commands Used`"

    ```bash
    git add docs/javascripts/iconsearch.js docs/styles/custom.css
    git commit -m "Fix icon search paths and display for GitHub Pages"
    git push origin main
    ```
    
---

#### Key Lesson Learned

!!! git "`Key Lesson Learned`"

    GitHub Pages hosts your site at a subdirectory (`/Afridyne-Systems/`) not at the root (`/`). Any absolute path starting with `/assets/` will fail because the browser looks for it at the domain root.
    
    ---
    
    Always use either:
    
    - A **full absolute URL** including the GitHub Pages subdirectory, or
    
    - A **relative path** carefully calculated from the page's depth
    
    In this case the full absolute URL was the cleanest and most reliable solution.
    
