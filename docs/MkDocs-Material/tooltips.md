---
icon: material/tooltip-plus
---

![](imgs/20260316-231142.png){: style="display: block; margin: 0 auto"}

 <H1 style="text-align: center;"> Tooltips</H1>

!!! info ""
    Technical documentation often incurs the usage of many acronyms, which may need additional explanation, especially for new user of your project. For these matters, Material for MkDocs uses a combination of Markdown extensions to enable site-wide glossaries.
    
### Configuration

!!! pied-piper "Configuration"

    This configuration enables abbreviations and allows to build a simple project-wide glossary, sourcing definitions from a central location. Add the following line to `mkdocs.yml`:
    
    ``` yaml
    markdown_extensions:
      - abbr
      - attr_list
      - pymdownx.snippets
    ```
    
See additional configuration options:

<div class="grid cards cols-3" markdown>

-   <span style="color: #009688">:material-cursor-default:</span> **Abbreviations**
    [:octicons-arrow-right-24: View Abbreviations](python-markdown.md#abbreviations){ .md-button style="border-color: #009688; color: #009688" }

    The Extension adds the ability to add a small tooltip to an element.

-   <span style="color: #66c0f4">:material-firefox:</span> **Attribute Lists**
    [:octicons-arrow-right-24: View Attribute Lists](python-markdown.md#attribute-lists){ .md-button style="border-color: #66c0f4; color: #66c0f4" }

    Allows HTML attributes & CSS classes to almost every MD inline & block-level element.

-   <span style="color: #4caf50">:material-puzzle:</span> **Snippets**
    [:octicons-arrow-right-24: View Snippets](python-markdown-extensions.md#snippets){ .md-button style="border-color: #4caf50; color: #4caf50" }

    The extension adds the ability to embed content from arbitrary files into a document.

</div>

### Improved Tooltips

<!-- md:version 9.5.0 -->
<!-- md:flag experimental -->

!!! info "Improved Tooltips"

    When improved tooltips are enabled, Material for MkDocs replaces the browser's rendering logic for `title` attribute with beautiful little tooltips.
    Add the following lines to `mkdocs.yml`:
    
    ``` yaml
    theme:
      features:
        - content.tooltips
    ```

Now, tooltips will be rendered for the following elements:

- __Content__ – elements with a `title`, permalinks and code copy button
- __Header__ – home button, header title, color palette switch and repository link
- __Navigation__ – links that are shortened with ellipsis, i.e. `...`

## Usage

### Adding Tooltips

!!! info "Adding Tooltips"

    The [Markdown syntax] allows to specify a `title` for each link, which will render as a beautiful tooltip when [improved tooltips] are enabled. Add a tooltip to a link with the following lines:
    
    ``` markdown title="Link with tooltip, inline syntax"
    [Hover me](https://example.com "I'm a tooltip!")
    ```
    
<div class="result" markdown>

<span style="color: #00b8d4; font-size: 0.9rem; vertical-align: middle;"> :material-information-outline:{ title="Come visit us for all your needs!" }</span> [Afridyne Systems](https://afridyne.co.za "Afridyne Systems, our service is the difference!")

</div>


!!! info ""

    Tooltips can also be added to link references:
    
    ``` markdown title="Link with tooltip, reference syntax"
    [Hover me][example]
    [example]: https://example.com "I'm a tooltip!"
    ```
    

<div class="result" markdown>

[Afridyne Systems (PTY) Ltd](https://afridyne.co.za "Our Service Is The Difference!")

</div>

!!! info "Other Elements"

    For all other elements, a `title` can be added by using the [Attribute Lists](http://127.0.0.1:8000/MkDocs-Material/python-markdown/#attribute-lists) extension:

    ``` markdown title="Icon with tooltip"
    :material-information-outline:{ title="Important information" }
    ```
    
<div class="result" markdown>

<span style="color: #00b8d4; font-size: 0.9rem; vertical-align: middle;"> :material-information-outline:{ title="Come visit us for all your needs!" }</span>

</div>

  [Markdown syntax]: https://daringfireball.net/projects/markdown/syntax#link
  [improved tooltips]: #improved-tooltips

### Adding Abbreviations

!!! quote ""

    Abbreviations can be defined by using a special syntax similar to URLs and [footnotes], starting with a `*` and immediately followed by the term or acronym to be associated in square brackets:
    
    ``` markdown title="Text with abbreviations"
    The HTML specification is maintained by the W3C.
    
    *[HTML]: Hyper Text Markup Language
    *[W3C]: World Wide Web Consortium
    ```
    
<div class="result" markdown>

The HTML specification is maintained by the W3C.

*[HTML]: Hyper Text Markup Language
*[W3C]: World Wide Web Consortium

</div>

  [footnotes]: footnotes.md

### Adding a Glossary

The [Snippets] extension can be used to implement a simple glossary by moving all abbreviations in a dedicated file[^1], and [auto-append] this file to all pages with the following configuration:

  [^1]:
    It's highly recommended to put the Markdown file containing the abbreviations outside of the `docs` folder (here, a folder with the name `includes` is used), as MkDocs might otherwise complain about an unreferenced file.
    
    
!!! quote ""

    === ":octicons-file-code-16: `includes/abbreviations.md`"

        ```` markdown
        *[HTML]: Hyper Text Markup Language
        *[W3C]: World Wide Web Consortium
        ````

    === ":octicons-file-code-16: `mkdocs.yml`"

        ```` yaml
        markdown_extensions:
          - pymdownx.snippets:
              auto_append:
                - includes/abbreviations.md
        ````


  [auto-append]: https://facelessuser.github.io/pymdown-extensions/extensions/snippets/#auto-append-snippets

!!! tip

    When using a dedicated file outside of the `docs` folder, add the parent directory to the list
    of `watch` folders so that when the glossary file is updated, the project is automatically
    reloaded when running `mkdocs serve`.

    ```` yaml
    watch:
      - includes
    ````
