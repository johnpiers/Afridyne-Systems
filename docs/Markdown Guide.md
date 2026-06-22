---
icon: octicons/markdown-16
---

![](imgs/20251229-131227.png){ .center-image }

<H1 style="text-align: center;">Basic Syntax</H1>

![Markdown Logo](images/markdown-mark.svg#only-light){ .center-image }
![Markdown Logo](images/markdown-mark-white.svg#only-dark){ .center-image }

<div align="center">
<a href="https://www.markdownguide.org/"" title="Return to the main page"><h1>Markdown Guide</h></a>
 </div>

<div class="grid cards cols-3" markdown>

 -   <span style="color: #0097a7">:octicons-rocket-24:</span> **Get Started**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/getting-started/){ .md-button style="border-color: #0097a7; color: #0097a7" }
    
    An overview of Markdown, why to use it, how it works, and the best way to get started.

-   <span style="color: #0097a7">:octicons-file-badge-24:</span> **Cheat Sheet**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/cheat-sheet/){ .md-button style="border-color: #0097a7; color: #0097a7" }
    
    A quick reference of all the Markdown elements for fast lookups while you're writing.

-   <span style="color: #0097a7">:octicons-terminal-24:</span> **Basic Syntax**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/basic-syntax/){ .md-button style="border-color: #0097a7; color: #0097a7" }
    
    The foundational elements outlined in the original John Gruber design document.

-   <span style="color: #388e3c">:octicons-plus-circle-24:</span> **Extended Syntax**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/extended-syntax/){ .md-button style="border-color: #388e3c; color: #388e3c" }
    
    Advanced features like tables, code blocks, and task lists not found in basic MD.

-   <span style="color: #388e3c">:octicons-tools-24:</span> **Hacks**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/hacks/){ .md-button style="border-color: #388e3c; color: #388e3c" }
    
    Creative ways to extend Markdown functionality for more complex document needs.

-   <span style="color: #388e3c">:octicons-cpu-24:</span> **Tools**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/tools/){ .md-button style="border-color: #388e3c; color: #388e3c" }
    
    A comprehensive list of applications, editors, and libraries that support Markdown.

-   <span style="color: #afb42b">:octicons-book-24:</span> **The Book**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/book/){ .md-button style="border-color: #afb42b; color: #afb42b" }
    
    The Markdown Guide is also available as a paperback and digital book for deep learning.
    
-   <span style="color: #afb42b">:octicons-home-24:</span> **Markdown Guide**
    [:octicons-arrow-right-24: Go to](https://www.markdownguide.org/){ .md-button style="border-color: #afb42b; color: #afb42b" }
    
    The primary resource for learning the syntax, tools, and best practices of Markdown.
    
-   <span style="color: #afb42b">:material-arrow-u-left-top:</span> **MkDocs-Material**
    [:octicons-arrow-right-24: Return to](index.md){ .md-button style="border-color: #afb42b; color: #afb42b" }

    Back to the root documentation.

</div>
<div align="center">
<a href="https://www.markdownguide.org/"" title="Return to the main page"><h3>Markdown Guide</h></a>
 </div>

!!! pied-piper "Markdown"

    <b>The Markdown elements outlined in the original design document.</b>
    

    ---

    ```text {.no-copy .no-style}
    NB: Nearly all Markdown applications support the basic syntax as outlined in
    the original Markdown design document.
    ```
    
    ---
    
    ```text {.no-copy .no-style}
    There are a few minor variations, as well as discrepancies between Markdown
    processors — Most of these are noted inline wherever possible.
    ```

## Headings

To create a heading, add number signs (`#`) in front of a word or phrase. The number of number signs you use should correspond to the heading level. For example, to create a heading level three (`<h3>`), use three number signs (e.g., `### My Header`).

??? desc "HTML Code for the table below"

    ```html
    <div class="isolated-table-container">
      <style>
        /* Use CSS Variables instead of hardcoded colors for dynamic theming */
        .isolated-table-container .table.table-bordered {
          border-collapse: collapse;
          width: 100%;
          max-width: 800px;
          margin: 20px auto;
          /* Use theme default border color */
          border: 1px solid var(--md-default-fg-color--light); 
          font-size: 16px;
          /* Default background color */
          background-color: var(--md-default-bg-color); 
          /* Default text color */
          color: var(--md-default-fg-color);
        }
        .isolated-table-container .table.table-bordered th,
        .isolated-table-container .table.table-bordered td {
          /* Use theme default border color */
          border: 1px solid var(--md-default-fg-color--light); 
          padding: 8px;
          text-align: left;
        }
        .isolated-table-container .table.table-bordered thead th {
          /* Use primary theme color for header background */
          background-color: var(--md-primary-fg-color); 
          font-weight: bold;
          /* Ensure header text is readable against primary color */
          color: var(--md-primary-bg-color); 
        }
        .isolated-table-container .table.table-bordered tbody tr:nth-child(odd) {
            /* Add some striping using a slightly different background color variable */
            background-color: var(--md-default-bg-color--light);
        }
        .isolated-table-container .table.table-bordered a {
          /* Use theme accent color for links */
          color: var(--md-accent-fg-color); 
          text-decoration: underline;
        }
      </style>

      <!-- Your original HTML table code starts here -->
      <table class="table table-bordered">
        <thead class="thead-light">
          <tr>
            <th>Markdown</th>
            <th>HTML</th>
            <th>Rendered Output</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code class="highlighter-rouge"># Heading level 1</code></td>
            <td><code class="highlighter-rouge">&lt;h1&gt;Heading level 1&lt;/h1&gt;</code></td>
            <td><h1 class="no-anchor" data-toc-skip="" id="heading-level-1">Heading level 1</h1></td>
          </tr>
          <tr>
            <td><code class="highlighter-rouge">## Heading level 2</code></td>
            <td><code class="highlighter-rouge">&lt;h2&gt;Heading level 2&lt;/h2&gt;</code></td>
            <td><h2 class="no-anchor" data-toc-skip="" id="heading-level-2">Heading level 2</h2></td>
          </tr>
          <tr>
            <td><code class="highlighter-rouge">### Heading level 3</code></td>
            <td><code class="highlighter-rouge">&lt;h3&gt;Heading level 3&lt;/h3&gt;</code></td>
            <td><h3 class="no-anchor" data-toc-skip="" id="heading-level-3">Heading level 3</h3></td>
          </tr>
          <tr>
            <td><code class="highlighter-rouge">#### Heading level 4</code></td>
            <td><code class="highlighter-rouge">&lt;h4&gt;Heading level 4&lt;/h4&gt;</code></td>
            <td><h4 class="no-anchor" id="heading-level-4">Heading level 4</h4></td>
          </tr>
          <tr>
            <td><code class="highlighter-rouge">##### Heading level 5</code></td>
            <td><code class="highlighter-rouge">&lt;h5&gt;Heading level 5&lt;/h5&gt;</code></td>
            <td><h5 class="no-anchor" id="heading-level-5">Heading level 5</h5></td>
          </tr>
          <tr>
            <td><code class="highlighter-rouge">###### Heading level 6</code></td>
            <td><code class="highlighter-rouge">&lt;h6&gt;Heading level 6&lt;/h6&gt;</code></td>
            <td><h6 class="no-anchor">Heading level 6</h6></td>
          </tr>
        </tbody>
      </table>
    </div>
    ```

<div class="isolated-table-container">
  <style>
    /* Use CSS Variables instead of hardcoded colors for dynamic theming */

    .isolated-table-container .table.table-bordered {
      border-collapse: collapse;
      width: 100%;
      max-width: 800px;
      margin: 20px auto;
      /* Use theme default border color */
      border: 1px solid var(--md-default-fg-color--light); 
      font-size: 16px;
      /* Default background color */
      background-color: var(--md-default-bg-color); 
      /* Default text color */
      color: var(--md-default-fg-color);
    }
    .isolated-table-container .table.table-bordered th,
    .isolated-table-container .table.table-bordered td {
      /* Use theme default border color */
      border: 1px solid var(--md-default-fg-color--light); 
      padding: 8px;
      text-align: left;
    }
    .isolated-table-container .table.table-bordered thead th {
      /* Use primary theme color for header background */
      background-color: var(--md-primary-fg-color); 
      font-weight: bold;
      /* Ensure header text is readable against primary color */
      color: var(--md-primary-bg-color); 
    }
    .isolated-table-container .table.table-bordered tbody tr:nth-child(odd) {
        /* Add some striping using a slightly different background color variable */
        background-color: var(--md-default-bg-color--light);
    }
    .isolated-table-container .table.table-bordered a {
      /* Use theme accent color for links */
      color: var(--md-accent-fg-color); 
      text-decoration: underline;
    }

    /* 
      You don't need the @media (prefers-color-scheme: dark) block anymore 
      because the CSS variables handle the dark/light mode switching dynamically.
    */
  </style>

<!-- Your original HTML table code starts here -->
<table class="table table-bordered">
  <thead class="thead-light">
    <tr>
      <th>Markdown</th>
      <th>HTML</th>
      <th>Rendered Output</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="highlighter-rouge"># Heading level 1</code></td>
      <td><code class="highlighter-rouge">&lt;h1&gt;Heading level 1&lt;/h1&gt;</code></td>
      <td><h1 class="no-anchor" data-toc-skip="" id="heading-level-1">Heading level 1</h1></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">## Heading level 2</code></td>
      <td><code class="highlighter-rouge">&lt;h2&gt;Heading level 2&lt;/h2&gt;</code></td>
      <td><h2 class="no-anchor" data-toc-skip="" id="heading-level-2">Heading level 2</h2></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">### Heading level 3</code></td>
      <td><code class="highlighter-rouge">&lt;h3&gt;Heading level 3&lt;/h3&gt;</code></td>
      <td><h3 class="no-anchor" data-toc-skip="" id="heading-level-3">Heading level 3</h3></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">#### Heading level 4</code></td>
      <td><code class="highlighter-rouge">&lt;h4&gt;Heading level  4&lt;/h4&gt;</code></td>
      <td><h4 class="no-anchor" id="heading-level-4">Heading level 4</h4></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">##### Heading level 5</code></td>
      <td><code class="highlighter-rouge">&lt;h5&gt;Heading level 5&lt;/h5&gt;</code></td>
      <td><h5 class="no-anchor" id="heading-level-5">Heading level 5</h5></td>
    </tr>
    <tr>
      <td><code class="highlighter-rouge">###### Heading level 6</code></td>
      <td><code class="highlighter-rouge">&lt;h6&gt;Heading level 6&lt;/h6&gt;</code></td>
      <td><h6 class="no-anchor">Heading level 6</h6></td>
    </tr>
  </tbody>
</table>

</div> <!-- Ends the isolated-table-container div -->


### Table converted from html to markdown as a ref.

??? desc "Table converted from html to markdown as a ref."

    ```markdown

    | Markdown | HTML | Rendered Output |
    | :--- | :--- | :--- |
    | `# Heading level 1` | `<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
    | `## Heading level 2` | `<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |
    | `### Heading level 3` | `<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
    | `#### Heading level 4` | `<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
    | `##### Heading level 5` | `<h5>Heading level 5</h5>` | <h5>Heading level 5</h5> |
    | `###### Heading level 6` | `<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |
    ```


| Markdown | HTML | Rendered Output |
| :--- | :--- | :--- |
| `# Heading level 1` | `<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `## Heading level 2` | `<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |
| `### Heading level 3` | `<h3>Heading level 3</h3>` | <h3>Heading level 3</h3> |
| `#### Heading level 4` | `<h4>Heading level 4</h4>` | <h4>Heading level 4</h4> |
| `##### Heading level 5` | `<h5>Heading level 5</h5>` | <h5>HEADING LEVEL 5</h5> |
| `###### Heading level 6` | `<h6>Heading level 6</h6>` | <h6>Heading level 6</h6> |

### Alternate Syntax

Alternatively, on the line below the text, add any number of `==` characters for heading level 1 or `--` characters for heading level 2.

### Alternate Syntax Reference

??? desc "HTML Code for the table below"

    ```html
    <div class="isolated-table-container">
      <style>
        /* Use CSS Variables instead of hardcoded colors for dynamic theming */
        .isolated-table-container .table.table-bordered {
          border-collapse: collapse;
          width: 100%;
          max-width: 800px;
          margin: 20px auto;
          border: 1px solid var(--md-default-fg-color--light); 
          font-size: 16px;
          background-color: var(--md-default-bg-color); 
          color: var(--md-default-fg-color);
        }
        .isolated-table-container .table.table-bordered th,
        .isolated-table-container .table.table-bordered td {
          border: 1px solid var(--md-default-fg-color--light); 
          padding: 8px;
          text-align: left;
        }
        .isolated-table-container .table.table-bordered thead th {
          background-color: var(--md-primary-fg-color); 
          font-weight: bold;
          color: var(--md-primary-bg-color); 
        }
        .isolated-table-container .table.table-bordered tbody tr:nth-child(odd) {
            background-color: var(--md-default-bg-color--light);
        }
        .isolated-table-container .table.table-bordered a {
          color: var(--md-accent-fg-color); 
          text-decoration: underline;
        }
      </style>

      <table class="table table-bordered">
        <thead class="thead-light">
          <tr>
            <th>Markdown</th>
            <th>HTML</th>
            <th>Rendered Output</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td><code class="highlighter-rouge">Heading level 1<br>===============</code></td>
            <td><code class="highlighter-rouge">&lt;h1&gt;Heading level 1&lt;/h1&gt;</code></td>
            <td><h1 class="no-anchor" data-toc-skip="" id="heading-level-1-1">Heading level 1</h1></td>
          </tr>
          <tr>
            <td><code class="highlighter-rouge">Heading level 2<br>---------------</code></td>
            <td><code class="highlighter-rouge">&lt;h2&gt;Heading level 2&lt;/h2&gt;</code></td>
            <td><h2 class="no-anchor" data-toc-skip="" id="heading-level-2-1">Heading level 2</h2></td>
          </tr>
        </tbody>
      </table>
    </div>
    ```

??? desc "Table converted from html to markdown as a ref."

    ```markdown

    | Markdown | HTML | Rendered Output |
    | :--- | :--- | :--- |
    | `Heading level 1`<br>`===============` | `<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
    | `Heading level 2`<br>`---------------` | `<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |
    ```


| Markdown | HTML | Rendered Output |
| :--- | :--- | :--- |
| `Heading level 1`<br>`===============` | `<h1>Heading level 1</h1>` | <h1>Heading level 1</h1> |
| `Heading level 2`<br>`---------------` | `<h2>Heading level 2</h2>` | <h2>Heading level 2</h2> |


### Heading Best Practices

Markdown applications don’t agree on how to handle a missing space between the number signs (`#`) and the heading name. For compatibility, always put a space between the number signs and the heading name.

## Paragraphs

To create paragraphs, use a blank line to separate one or more lines of text.

### Heading Best Practices

Markdown applications don’t agree on how to handle a missing space between the number signs (`#`) and the heading name. For compatibility, always put a space between the number signs and the heading name.

## Paragraphs

To create paragraphs, use a blank line to separate one or more lines of text.

!!! tip "Paragraph Best Practices"
    Unless the [paragraph is in a list](https://www.markdownguide.org/basic-syntax/#paragraphs), don’t indent paragraphs with spaces or tabs.

    1. List item one.
    
       List item one continued with a second paragraph followed by an indented block.
       
       ```bash
       $ ls *.sh
       $ mv *.sh ~/tmp
       ```
       
       List item continued with a third paragraph.

    2. List item two continued with an open block.
       
       This paragraph is part of the preceding list item.
       
       *   **a.** This list is nested and does not require explicit item continuation.
           
           This paragraph is part of the preceding list item.
       
       *   **b.** List item b.
       
       This paragraph belongs to item two of the outer list.


