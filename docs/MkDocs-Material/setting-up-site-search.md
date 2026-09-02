---
status: new
icon: octicons/search-24
search:
  boost: 1.05
---

![](imgs/20260323-210417.png){: style="display: block; margin: 0 auto"}
<H1 style="text-align: center;"><ins>Setting Up Site Search</ins></H1>


!!! quote ""
    MaterialX `10.2.0` fully refactors the search module with a brand-new architecture, greatly improving **search quality** and **indexing efficiency**.
    
    It supports multi-provider mode, chunked indexing, on-demand loading, index compression, multilingual search and cross-domain search. It is suitable for various complex scenarios and large-scale sites, and can handle sites with more than 100,000 pages.
    
    [Pagefind]{target="_blank"} is the default provider. You may switch back to the original [Lunr]{target="_blank"} when using it in an [offline]{target="_blank"} environment (opened via the `file://` protocol).
    
  [Pagefind]: https://pagefind.app/
  [Lunr]: https://lunrjs.com/
  [offline]: offline.md
    
    

[Back to: #Advanced-Configuration  :fontawesome-solid-paper-plane:](../index.md#advanced-configuration){ .md-button .md-button--custom }

## Configuration

### Built-in Search Plugin

<!-- md:version 0.1.0 -->
<!-- md:plugin -->

!!! pied-piper ""
    The built-in search plugin integrates seamlessly with Material for MkDocs, adding multilingual client-side search with [lunr] and [lunr-languages]. It's enabled by default, but must be re-added to `mkdocs.yml` when other plugins are used:
    
    ``` yaml
    plugins:
      - search
    ```
    
    For a list of all settings, please consult the [plugin documentation].
    
  [plugin documentation]: search.md

  [lunr]: https://lunrjs.com
  [lunr-languages]: https://github.com/MihaiValentin/lunr-languages
    
    
### Search Suggestions

<!-- md:version 7.2.0 -->
<!-- md:feature -->
<!-- md:flag experimental -->

!!! info ""
    When search suggestions are enabled, the search will display the likeliest completion for the last word which can be accepted with the ++arrow-right++ key. Add the following lines to `mkdocs.yml`:
    
    ``` yaml
    theme:
      features:
        - search.suggest
    ```
    
    Searching for [:octicons-search-24: search su][Search suggestions example] yields ^^search suggestions^^ as a suggestion.
    
   [Search suggestions example]: ?q=search+su
    
### Search Highlighting

<!-- md:version 7.2.0 -->
<!-- md:feature -->
<!-- md:flag experimental -->

!!! info ""
    When search highlighting is enabled and a user clicks on a search result, Material for MkDocs will highlight all occurrences after following the link. Add the following lines to `mkdocs.yml`:
    
    ``` yaml
    theme:
      features:
        - search.highlight
    ```
    
    Searching for [:octicons-search-24: code blocks][Search highlighting example] highlights all occurrences of both terms.
    
   [Search highlighting example]: code-blocks.md?h=code+blocks
    
### Search Sharing

<!-- md:version 7.2.0 -->
<!-- md:feature -->

!!! info ""
    When search sharing is activated, a :material-share-variant: share button is rendered next to the reset button, which allows to deep link to the current search query and result. Add the following lines to `mkdocs.yml`:
    
    ``` yaml
    theme:
      features:
        - search.share
    ```
    
    When a user clicks the share button, the URL is automatically copied to the clipboard.
    
## Usage

### Search Boosting

!!! recommendation "Search Boosting"

    Pages can be boosted in search with the front matter `search.boost` property, which will make them rank higher. Add the following lines at the top of a Markdown file:

    === ":material-arrow-up-circle: Rank up"

        ``` yaml
        ---
        search:
          boost: 2 # (1)!
        ---

        # Page title
        ...
        ```

        1.  :woman_in_lotus_position: When boosting pages, be gentle and start with
            __low values__.

    === ":material-arrow-down-circle: Rank down"

        ``` yaml
        ---
        search:
          boost: 0.5
        ---

        # Page title
        ...
        ```

### Search Exclusion

!!! recommendation "Search Exclusion"

    Pages can be excluded from search with the front matter `search.exclude` property, removing them from the index. Add the following lines at the top of a Markdown file:

    ``` yaml
    ---
    search:
      exclude: true
    ---

    # Page title
    ...
    ```

#### Excluding Sections

!!! recommendation "Excluding Sections"

    When [Attribute Lists] is enabled, specific sections of pages can be excluded
    from search by adding the `data-search-exclude` pragma after a Markdown
    heading:

    === ":octicons-file-code-16: `docs/page.md`"

        ``` markdown
        # Page title

        ## Section 1

        The content of this section is included

        ## Section 2 { data-search-exclude }

        The content of this section is excluded
        ```

    === ":octicons-codescan-16: `search_index.json`"

        ``` json
        {
          ...
          "docs": [
            {
              "location":"page/",
              "text":"",
              "title":"Document title"
            },
            {
              "location":"page/#section-1",
              "text":"<p>The content of this section is included</p>",
              "title":"Section 1"
            }
          ]
        }
        ```

      [Attribute Lists]: python-markdown.md#attribute-lists

#### Excluding Blocks

!!! recommendation "Excluding Blocks"

    When [Attribute Lists] is enabled, specific sections of pages can be excluded from search by adding the `data-search-exclude` pragma after a Markdown inline- or block-level element:

    === ":octicons-file-code-16: `docs/page.md`"

        ``` markdown
        # Page title

        The content of this block is included

        The content of this block is excluded
        { data-search-exclude }
        ```

    === ":octicons-codescan-16: `search_index.json`"

        ``` json
        {
          ...
          "docs": [
            {
              "location":"page/",
              "text":"<p>The content of this block is included</p>",
              "title":"Document title"
            }
          ]
        }
        ```

[Back to: #Advanced-Configuration  :fontawesome-solid-paper-plane:](../index.md#advanced-configuration){ .md-button .md-button--custom }