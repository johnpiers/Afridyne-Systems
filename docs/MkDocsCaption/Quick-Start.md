---
icon: simple/materialformkdocs
---

![](imgs/20260309-021514.png){ .center-image }

<H1 style="text-align: center;">Quick Start</H1>

Back to: [Caption Main Page](../Caption.md)

- The plugin can be configured in the MkDocs configuration file `mkdocs.yml`. By default, the figure and table captions are enabled.

- To enable the plugin, simply add the plugin to the `plugin` section of your configuration.

!!! info "In `mkdocs.yml`:"

    ```yaml
    ...
    plugins:
     - caption
    ```
- With the plugin enabled, one can now use an easy and descriptive syntax to add captions to figures and tables. The captions are automatically numbered and can be referenced in the text.

!!! tip

    The caption text is converted by mkdocs itself. This means that technically a caption can contain the same things than any other text.

!!! info ""

    === "Markdown"

        ```Markdown
        ![figure caption](img.jpg)

        Table: table caption {#my-table}


        | heading 1| heading 2 | 
        | - | - | 
        | content 1 | content 2 |
        | content 3 | content 4 |

        See [#my-table] for more details.
        ```

    === "HTML"

        ```html
        <p>
        <figure id=_figure-1>
            <img src="img.jpg" />
            <figcaption>Figure 1. figure caption</figcaption>
        </figure>
        </p>
        <p>
        <table id="my-table">
        <thead>
            <tr>
            <th>heading 1</th>
            <th>heading 2</th>
            </tr>
        </thead>
        <tbody>
            <tr>
            <td>content 1</td>
            <td>content 2</td>
            </tr>
            <tr>
            <td>content 3</td>
            <td>content 4</td>
            </tr>
        </tbody>
        <caption style="caption-side:bottom">Table 1: table caption</caption>
        </table>
        <p>
        See <a href="#my-table">Table 1</a> for more details.
        </p>
        ```

![figure caption](imgs/tldr.jpg){ .center-image }

<figure id=_figure-1>
    <figcaption>Figure 1. figure caption</figcaption>
</figure>



<div class="center-container" markdown="1">


| heading 1 | heading 2 |
| :---: | :---: |
| content 1 | content 2 |
| content 3 | content 4 |

</div>


<div class="center-container">
  <p>See <a href="#my-table">Table 1</a> for more details.</p>
</div>


<!-- 1. The Image -->
<div class="center-container" markdown="1">
![figure caption](imgs/tldr.jpg){ .center-image }
</div>

<!-- 2. The Figure Caption (Manual ID for the link to work) -->
<div class="center-container">
  <p id="_figure-1">Figure 1. figure caption</p>
</div>

<!-- 3. The Table -->
<div class="center-container" markdown="1">

| heading 1 | heading 2 |
| :---: | :---: |
| content 1 | content 2 |
| content 3 | content 4 |
</div>

<!-- 4. The Table Caption + Link Anchor -->
<div class="center-container">
  <p id="my-table">Table 1: table caption</p>
</div>

<!-- 5. The Reference Link -->
<div class="center-container">
  <p>See <a href="#my-table">Table 1</a> for more details.</p>
</div>
