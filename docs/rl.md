---
icon: simple/materialformkdocs
---

![](imgs/20260105-102020.png){ .center-image }

<H1 style="text-align: center;"> <u>MkDocs Creating Your Site</u></H1>

!!! quote ""

    After you've [installed] Material for MkDocs, you can bootstrap your project documentation using the `mkdocs` executable. Go to the directory where you want your project to be located and enter:
    
    ```
    mkdocs new .
    ```
    
!!! info ""

    Alternatively, if you're running Material for MkDocs from within Docker, use:

    === "Unix, Powershell"

        ```
        docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material new .
        ```

    === "Windows (cmd)"

        ```
        docker run --rm -it -v "%cd%":/docs squidfunk/mkdocs-material new .
        ```

    This will create the following structure:

    ``` { .sh .no-copy }
    .
    ├─ docs/
    │  └─ index.md
    └─ mkdocs.yml
    ```
    
  [installed]: MkDocs-Material-Start.md


## Configuration

### Minimal Configuration

!!! info ""

    Simply set the `site_name` and add the following lines to `mkdocs.yml` to enable the theme:

    ``` yaml hl_lines="2-5"
    site_name: My site
    site_url: https://mydomain.org
    theme:
      name: material
    ```

    The `site_url` setting is important for a number of reasons. By default, MkDocs will assume that your site is hosted at the root of your domain. This is not the case, for example, when [publishing](MkDocs-Material/publishing-your-site.md) to [GitHub pages] - unless you use a custom domain. Another reason is that some of the plugins require the `site_url` to be set, so you should always do this.
  
  [Publishing](https://squidfunk.github.io/mkdocs-material/publishing-your-site/) to [GitHub pages.](https://docs.github.com/en/pages)
  [installation methods]: ./MkDocs-Material/getting-started.md#installation

???+ tip "Recommended: [configuration validation and auto-complete]"

    In order to minimize friction and maximize productivity, Material for MkDocsprovides its own [schema.json] [`^1`] for `mkdocs.yml`. If your editor supports YAML schema validation, it's definitely recommended to set it up:

    === "Visual Studio Code"

        1.  Install [`vscode-yaml`][vscode-yaml] for YAML language support.
        2.  Add the schema under the `yaml.schemas` key in your user or workspace [`settings.json`][settings.json]:

            ``` json
            {
              "yaml.schemas": {
                "https://squidfunk.github.io/mkdocs-material/schema.json": "mkdocs.yml"
              },
              "yaml.customTags": [ // (1)!
                "!ENV scalar",
                "!ENV sequence",
                "!relative scalar",
                "tag:yaml.org,2002:python/name:material.extensions.emoji.to_svg",
                "tag:yaml.org,2002:python/name:material.extensions.emoji.twemoji",
                "tag:yaml.org,2002:python/name:pymdownx.superfences.fence_code_format",
                "tag:yaml.org,2002:python/object/apply:pymdownx.slugs.slugify mapping"
              ]
            }
            ```

        1.  This setting is necessary if you plan to use [icons and emojis], or Visual Studio Code will show errors on certain lines.

    === "Other"

        1.  Ensure your editor of choice has support for YAML schema validation.
        2.  Add the following lines at the top of `mkdocs.yml`:

            ``` yaml
            # yaml-language-server: $schema=https://squidfunk.github.io/mkdocs-material/schema.json
            ```

  [^1]:
    If you're a MkDocs plugin or Markdown extension author and your project works with Material for MkDocs, you're very much invited to contribute a schema for your [extension] or [plugin] as part of a pull request on GitHub. If you already have a schema defined, or wish to self-host your schema to reduce duplication, you can add it via [$ref].

  [configuration validation and auto-complete]: https://x.com/squidfunk/status/1487746003692400642
  [schema.json]: schema.json
  [vscode-yaml]: https://marketplace.visualstudio.com/items?itemName=redhat.vscode-yaml
  [settings.json]: https://code.visualstudio.com/docs/getstarted/settings
  [extension]: https://github.com/squidfunk/mkdocs-material/tree/master/docs/schema/extensions
  [plugin]: https://github.com/squidfunk/mkdocs-material/tree/master/docs/schema/plugins
  [$ref]: https://json-schema.org/understanding-json-schema/structuring.html#ref
  [icons and emojis]: ./MkDocs-Material/icons-emojis.md

### Advanced Configuration

!!! bug ""
    - Material for MkDocs comes with many configuration options.
    
    - The setup section explains in great detail how to configure and customize colors, fonts, icons and much more:
    

<div class="grid cards cols-3" markdown>

-   <span style="color: #2094f3">:material-palette:</span> **Changing the Colors**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/changing-the-colors.md){ .md-button }
    
    Customise primary and accent colors to match your brand identity.

-   <span style="color: #2094f3">:material-format-font:</span> **Changing the Fonts**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/changing-the-fonts.md){ .md-button }
    
    Configure Google Fonts or custom web fonts for typography.

-   <span style="color: #2094f3">:material-translate:</span> **Changing the Language**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/changing-the-language.md){ .md-button }
    
    Localize your site interface and search into 50+ languages.

-   <span style="color: #2094f3">:material-emoticon-happy-outline:</span> **Changing the Logo**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/changing-the-logo-and-icons.md){ .md-button }
    
    Set a custom logo and choose from thousands of integrated icons.

-   <span style="color: #4caf50">:material-shield-check:</span> **Data Privacy**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/ensuring-data-privacy.md){ .md-button }
    
    Enable GDPR-compliant features and cookie consent management.

-   <span style="color: #4caf50">:material-compass:</span> **Site Navigation**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-navigation.md){ .md-button }
    
    Define your site structure, tabs, and table of contents behavior.

-   <span style="color: #4caf50">:material-magnify:</span> **Site Search**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-site-search.md){ .md-button }
    
    Configure the built-in search engine with highlighting and indexing.

-   <span style="color: #4caf50">:material-chart-bar:</span> **Site Analytics**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-site-analytics.md){ .md-button }
    
    Integrate Google Analytics or other privacy-focused tracking tools.

-   <span style="color: #4caf50">:material-page-layout-header:</span> **The Header**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-the-header.md){ .md-button }
    
    Customize the sticky header, search bar, and repository links.

-   <span style="color: #4caf50">:material-page-layout-footer:</span> **The Footer**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-the-footer.md){ .md-button }
    
    Manage "Previous/Next" buttons and the copyright notice area.

-   <span style="color: #ff9800">:material-card-account-details:</span> **Social Cards**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-social-cards.md){ .md-button }
    
    Generate automatic preview images for Twitter and LinkedIn shares.

-   <span style="color: #ff9800">:material-post:</span> **Setting up a Blog**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-a-blog.md){ .md-button }
    
    Transform your documentation into a fully-featured technical blog.

-   <span style="color: #ff9800">:material-tag:</span> **Setting up Tags**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-tags.md){ .md-button }
    
    Organize content with categories and tags for easier discovery.

-   <span style="color: #ff9800">:material-source-branch:</span> **Versioning**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/setting-up-versioning.md){ .md-button }
    
    Host multiple versions of your documentation simultaneously.

-   <span style="color: #ff9800">:material-git:</span> **Git Repository**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/adding-a-git-repository.md){ .md-button }
    
    Link your source code to enable "Edit this page" functionality.

-   <span style="color: #ff9800">:material-comment-text-outline:</span> **Comment System**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/adding-a-comment-system.md){ .md-button }
    
    Integrate Giscus or Disqus to build community engagement.

-   <span style="color: #ff9800">:material-lightning-bolt:</span> **Optimization**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/building-an-optimized-site.md){ .md-button }
    
    Minify CSS/JS and optimize images for lightning-fast loading.

-   <span style="color: #ff9800">:material-wifi-off:</span> **Offline Usage**
    [:octicons-arrow-right-24: View Guide](./MkDocs-Material/building-for-offline-usage.md){ .md-button }
    
    Package your documentation for use without an internet connection.

</div>


!!! info "Supported Markdown Extensions"
    Furthermore, see the list of supported [Markdown extensions] that are natively integrated with Material for MkDocs.
    
[Markdown extensions]: https://squidfunk.github.io/mkdocs-material/setup/extensions/python-markdown-extensions/

## Templates

If you want to jump start a new project, you can go to our [Custom Ttemplates:](https://zensical.org/docs/customization/?h=templates#custom-templates)

<div class="grid cards" markdown>

- :material-book-open-outline: __[Blog]__ – Set up a standalone blog or host it alongside your documentation
- :material-cards-variant: __[Social Cards]__ – Automatically create social media previews when sharing links


</div>

[Blog]: MkDocs-Material/setting-up-a-blog.md
[Social Cards]: MkDocs-Material/setting-up-social-cards.md

### Python Markdown Extensions

The [Python Markdown Extensions](https://facelessuser.github.io/pymdown-extensions/) package is an excellent collection of additional extensions perfectly suited for advanced technical writing. Material for MkDocs lists this package as an explicit dependency, so it's automatically installed with a supported version.

### Supported Extensions

In general, all extensions that are part of [Python Markdown Extensions](https://facelessuser.github.io/pymdown-extensions/) should work with Material for MkDocs. The following list includes all extensions that are natively supported, meaning they work without any further adjustments.

### Arithmatex

<!-- md:version 1.0.0 -->
<!-- md:extension [pymdownx.arithmatex][Arithmatex] -->

The [Arithmatex] extension allows for rendering of block and inline block equations and integrates seamlessly with [MathJax][^1] – a library for mathematical typesetting. Enable it via `mkdocs.yml`:

  [^1]:
    Other libraries like [KaTeX] are also supported and can be integrated with some additional effort. See the [Arithmatex documentation on KaTeX] for further guidance, as this is beyond the scope of Material for MkDocs.

``` yaml
markdown_extensions:
  - pymdownx.arithmatex:
      generic: true
```

Besides enabling the extension in `mkdocs.yml`, a MathJax configuration and the JavaScript runtime need to be included, which can be done with a few lines of [additional JavaScript]:

=== ":octicons-file-code-16: `docs/javascripts/mathjax.js`"

    ``` js
    window.MathJax = {
      tex: {
        inlineMath: [["\\(", "\\)"]],
        displayMath: [["\\[", "\\]"]],
        processEscapes: true,
        processEnvironments: true
      },
      options: {
        ignoreHtmlClass: ".*|",
        processHtmlClass: "arithmatex"
      }
    };

    document$.subscribe(() => { // (1)!
      MathJax.startup.output.clearCache()
      MathJax.typesetClear()
      MathJax.texReset()
      MathJax.typesetPromise()
    })
    ```

    1. This integrates MathJax with [instant loading]


=== ":octicons-file-code-16: `mkdocs.yml`"

    ``` yaml
    extra_javascript:
      - javascripts/mathjax.js
      - https://unpkg.com/mathjax@3/es5/tex-mml-chtml.js
    ```

The other configuration options of this extension are not officially supported by Material for MkDocs, which is why they may yield unexpected results. Use them at your own risk.

See reference for usage:

- [Using block syntax]
- [Using inline block syntax]

  [Arithmatex]: https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/
  [Arithmatex documentation on KaTeX]: https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/#loading-katex
  [MathJax]: https://www.mathjax.org/
  [KaTeX]: https://github.com/Khan/KaTeX
  [additional JavaScript]: https://github.com/squidfunk/mkdocs-material/blob/master/docs/customization.md#additional-javascript
  [instant loading]: MkDocs-Material/setting-up-navigation.md#instant-loading
  [Using block syntax]: https://github.com/squidfunk/mkdocs-material/blob/master/docs/reference/math.md#using-block-syntax
  [Using inline block syntax]: https://github.com/squidfunk/mkdocs-material/blob/master/docs/reference/math.md#using-inline-block-syntax

### Previewing As You Write

MkDocs includes a live preview server, so you can preview your changes as you write your documentation. The server will automatically rebuild the site upon saving. Start it with:

``` sh
mkdocs serve # (1)!
```

1.  If you have a large documentation project, it might take minutes until MkDocs has rebuilt all pages for you to preview. If you're only interested in the current page, the [`--dirtyreload`][--dirtyreload] flag will make rebuilds much faster:

    ```
    mkdocs serve --dirtyreload
    ```

If you're running Material for MkDocs from within Docker, use:

=== "Unix, Powershell"

    ```
    docker run --rm -it -p 8000:8000 -v ${PWD}:/docs squidfunk/mkdocs-material
    ```

=== "Windows"

    ```
    docker run --rm -it -p 8000:8000 -v "%cd%":/docs squidfunk/mkdocs-material
    ```

Point your browser to [localhost:8000][live preview] and you should see:

[![Creating your site]][Creating your site]

  [--dirtyreload]: https://www.mkdocs.org/about/release-notes/#support-for-dirty-builds-990
  [live preview]: http://localhost:8000
  [Creating your site]: ./assets/assets/screenshots/creating-your-site.png

### Building Your Site

When you're finished editing, you can build a static site from your Markdown files with:

```
mkdocs build
```

If you're running Material for MkDocs from within Docker, use:

=== "Unix, Powershell"

    ```
    docker run --rm -it -v ${PWD}:/docs squidfunk/mkdocs-material build
    ```

=== "Windows"

    ```
    docker run --rm -it -v "%cd%":/docs squidfunk/mkdocs-material build
    ```

The contents of this directory make up your project documentation. There's no need for operating a database or server, as it is completely self-contained. The site can be hosted on [GitHub Pages], [GitLab Pages], a CDN of your choice or your private web space.

  [GitHub Pages]: ./MkDocs-Material/publishing-your-site.md#github-pages
  [GitLab pages]: ./MkDocs-Material/publishing-your-site.md#gitlab-pages

If you intend to distribute your documentation as a set of files to be read from a local filesystem rather than a web server (such as in a `.zip` file), please read the notes about [building for offline usage].

  [building for offline usage]: ./MkDocs-Material/building-for-offline-usage.md


### Example of a Relative Link

<div class="admonition tip"> <p class="admonition-title">Tip</p> <p>If you don't have prior experience with Python, we recommend reading <a href="https://realpython.com/what-is-pip/" target="_blank" rel="noopener">Using Python's pip to Manage Your Projects' Dependencies</a>, which is a really good introduction on the mechanics of Python package management and helps you troubleshoot if you run into errors.</p> </div>

# Extensions

Markdown is a very small language with a kind-of reference implementation called
[John Gruber's Markdown]. [Python Markdown] and [Python Markdown Extensions]
are two packages that enhance the Markdown writing experience, adding useful
syntax extensions for technical writing.

  [John Gruber's Markdown]: https://daringfireball.net/projects/markdown/
  [Python Markdown]: MkDocs-Material/python-markdown.md
  [Python Markdown Extensions]: MkDocs-Material/python-markdown-extensions.md

## Supported Extensions

The following extensions are all supported by Material for MkDocs and therefore strongly recommended. Click on each extension to learn about its purpose and configuration:



| Supported Extensions | Supported Extensions |
| :--- | :--- |
| - [Abbreviations] <br> - [Admonition] <br> - [Arithmatex] <br> - [Attribute Lists] <br> - [BetterEm] <br> - [Caret, Mark & Tilde] <br> - [Critic] <br> - [Definition Lists] <br> - [Details] <br> - [Emoji] <br> - [Footnotes] | - [Highlight] <br> - [Keys] <br> - [Markdown in HTML] <br> - [SmartSymbols] <br> - [Snippets] <br> - [SuperFences] <br> - [Tabbed] <br> - [Table of Contents] <br> - [Tables] <br> - [Tasklist] |



  [Abbreviations]: MkDocs-Material/python-markdown.md#abbreviations
  [Admonition]: MkDocs-Material/python-markdown.md#admonition
  [Arithmatex]: MkDocs-Material/python-markdown-extensions.md#arithmatex
  [Attribute Lists]: MkDocs-Material/python-markdown.md#attribute-lists
  [BetterEm]: MkDocs-Material/python-markdown-extensions.md#betterem
  [Caret, Mark & Tilde]: MkDocs-Material/python-markdown-extensions.md#caret-mark-tilde
  [Critic]: MkDocs-Material/python-markdown-extensions.md#critic
  [Definition Lists]: MkDocs-Material/python-markdown.md#definition-lists
  [Details]: MkDocs-Material/python-markdown-extensions.md#details
  [Emoji]: MkDocs-Material/python-markdown-extensions.md#emoji
  [Footnotes]: MkDocs-Material/python-markdown.md#footnotes
  [Highlight]: MkDocs-Material/python-markdown-extensions.md#highlight
  [Keys]: MkDocs-Material/python-markdown-extensions.md#keys
  [Markdown in HTML]: MkDocs-Material/python-markdown.md#markdown-in-html
  [SmartSymbols]: MkDocs-Material/python-markdown-extensions.md#smartsymbols
  [Snippets]: MkDocs-Material/python-markdown-extensions.md#snippets
  [SuperFences]: MkDocs-Material/python-markdown-extensions.md#superfences
  [Tabbed]: MkDocs-Material/python-markdown-extensions.md#tabbed
  [Table of Contents]: MkDocs-Material/python-markdown.md#table-of-contents
  [Tables]: MkDocs-Material/python-markdown.md#tables
  [Tasklist]: MkDocs-Material/python-markdown-extensions.md#tasklist

## Configuration

Extensions are configured as part of `mkdocs.yml` – the MkDocs configuration file. The following sections contain two example configurations to bootstrap your documentation project.

  [overview]: #advanced-configuration

### Minimal Configuration

This configuration is a good starting point for when you're using Material for MkDocs for the first time. The best idea is to explore the [reference], and gradually add what you want to use:

``` yaml
markdown_extensions:

  # Python Markdown
  - toc:
      permalink: true

  # Python Markdown Extensions
  - pymdownx.highlight
  - pymdownx.superfences
```

  [reference]: MkDocsCaption/index.md

### Recommended Configuration

This configuration enables all Markdown-related features of Material for MkDocs and is great for experienced users bootstrapping a new documentation project:

``` yaml
markdown_extensions:

  # Python Markdown
  - abbr
  - admonition
  - attr_list
  - def_list
  - footnotes
  - md_in_html
  - toc:
      permalink: true

  # Python Markdown Extensions
  - pymdownx.arithmatex:
      generic: true
  - pymdownx.betterem:
      smart_enable: all
  - pymdownx.caret
  - pymdownx.details
  - pymdownx.emoji:
      emoji_index: !!python/name:material.extensions.emoji.twemoji
      emoji_generator: !!python/name:material.extensions.emoji.to_svg
  - pymdownx.highlight
  - pymdownx.inlinehilite
  - pymdownx.keys
  - pymdownx.mark
  - pymdownx.smartsymbols
  - pymdownx.superfences
  - pymdownx.tabbed:
      alternate_style: true
  - pymdownx.tasklist:
      custom_checkbox: true
  - pymdownx.tilde
```
