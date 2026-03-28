---
icon: simple/materialformkdocs
---

![](imgs/20260224-124153.png){: style="display: block; margin: 0 auto"}

<H2 style="text-align: center;" markdown="1">
© Afridyne Systems™ ➠ [MkDocs](https://www.mkdocs.org/) ➻ [Material](https://squidfunk.github.io/mkdocs-material/)
</H2>

---

For full Documentation visit: [mkdocs.org](https://www.mkdocs.org).

---

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



## Commands

!!! abstract "The Basic Commands"

    * `mkdocs new [dir-name]` - Create a new project.
    * `mkdocs serve` - Start the live-reloading docs server.
    * `mkdocs build` - Build the documentation site.
    * `mkdocs -h` - Print help message and exit.
    
## Project Layout

=== "Visual Reference"
    !!! info "Project Layout"
        :material-folder:{ style="color: #2196f3;" } `docs/`
        &emsp; :material-file-outline:{ style="color: #9e9e9e;" } `index.md  # The documentation homepage.`
        &emsp; :material-file-outline:{ style="color: #9e9e9e;" } `...       # Other markdown pages.`
        :material-file-code-outline:{ style="color: #9e9e9e;" } `mkdocs.yml   # The configuration file.`

=== "Annotated (Side-by-Side)"

    <div style="display: flex; gap: 20px;">
    <div style="flex: 1;">

    ```yaml
    mkdocs.yml    # (1)
    docs/
        index.md  # (2)
        ...       # (3)
    ```

    </div>
    <div style="flex: 1; font-size: 0.9em; padding-top: 10px;">

    1. **Configuration:** Where you enable all those cool extensions.
    2. **Homepage:** The main entry point for your site.
    3. **Other Pages:** Any additional markdown files.

    </div>
    </div>


## Getting Started with MkDocs

##### An introductory tutorial!

---

##### Installation

!!! quote "Installation"

    To install MkDocs, run the following command from the command line:
    
    ```bash
    pip install mkdocs
    ```
    
For more details, see the [Installation Guide](https://www.mkdocs.org/user-guide/installation/).

## Creating a New Project

!!! pied-piper "Creating a New Project"

    Getting started is super easy. To create a new project, run the following command from the command line:
    
    ```bash
    $ mkdocs new my-project
    cd my-project
    ```
    
    ---
    
    
    <H4 style="text-align: center;">Take a moment to review the initial project that has been created for you.</H4>
    
    
    ![The initial MkDocs layout](imgs/20260224-085639.png){ .center-image }
    

- There's a single configuration file named `mkdocs.yml`, and a folder named `docs` that will contain your documentation source files (`docs` is the default value for the [docs_dir](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/configuration.md#docs_dir) configuration setting).

- Right now the `docs` folder just contains a single documentation page, named `index.md`.

!!! info "MkDocs built-in dev-server"

    - MkDocs comes with a built-in dev-server that lets you preview your documentation as you work on it.
    
    - Make sure you're in the same directory as the `mkdocs.yml` configuration file, and then start the server by running the `mkdocs serve` command:
    
    ```console
    $ mkdocs serve
    INFO    -  Building documentation...
    INFO    -  Cleaning site directory
    INFO    -  Documentation built in 0.22 seconds
    INFO    -  [15:50:43] Watching paths for changes: 'docs', 'mkdocs.yml'
    INFO    -  [15:50:43] Serving on http://127.0.0.1:8000/
    ```
    
    Open up <http://127.0.0.1:8000/> in your browser, and you'll see the default home page being displayed:
    

![The MkDocs live server](imgs/20260224-085814.png){ .center-image }

- The dev-server also supports auto-reloading, and will rebuild your documentation whenever anything in the configuration file, documentation directory, or theme directory changes.

- Open the `docs/index.md` document in your text editor of choice, change the initial heading to `MkLorum`, and save your changes. Your browser will auto-reload and you should see your updated documentation immediately.

!!! info "mkdocs.yml"

    Now try editing the configuration file: `mkdocs.yml`. Change the [`site_name`](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/configuration.md#site_name) setting to `MkLorum` and save the file.
    
    ```yaml
    site_name: MkLorum
    ```
    
    ---
    
    <H4 style="text-align: center;">Your browser should immediately reload, and you'll see your new site name take effect.</H4>
    
    ![The site_name setting](imgs/20260224-091757.png){ .center-image }
    

!!! warning "NOTE!"

    The [`site_name`](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/configuration.md#site_name) configuration option is the only required option in your configuration file.
    
##### Adding Pages

!!! info "AddingPages"

    Now add a second page to your documentation:
    
    ```bash
    curl 'https://jaspervdj.be/lorem-markdownum/markdown.txt' > docs/about.md
    ```
    
!!! pied-piper "Edit Config"

    As our documentation site will include some navigation headers, you may want to edit the configuration file and add some information about the order, title, and nesting of each page in the navigation header by adding a [`nav`](https://www.mkdocs.org/user-guide/configuration/#nav) setting:
    
    ```yaml
    site_name: MkLorum
    nav:
      - Home: index.md
      - About: about.md
    ```
    
!!! pied-piper ""

    Save your changes and you'll now see a navigation bar with `Home` and `About` items on the left as well as `Search`, `Previous`, and `Next` items on the right.
    ⬇️⬇️⬇️
    
![Screenshot](imgs/20260224-092213.png)
!!! quote ""
    - Try the menu items and navigate back and forth between pages. Then click on `Search`. A search dialog will appear, allowing you to search for any text on any
    page.
    
    - Notice that the search results include every occurrence of the search term on the site and links directly to the section of the page in which the search term appears. You get all of that with no effort or configuration on your part!
    ⬇️⬇️⬇️

![Screenshot](imgs/20260224-092503.png)

##### Theming our Documentation

!!! info "Theming"

    Now change the configuration file to alter how the documentation is displayed by changing the theme. Edit the `mkdocs.yml` file and add a [`theme`](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/configuration.md#theme) setting:
    
    ```yaml
    site_name: MkLorum
    nav:
      - Home: index.md
      - About: about.md
    theme: readthedocs
    ```
    
    Save your changes, and you'll see the ReadTheDocs theme being used.
    

![Screenshot](imgs/20260224-084351.png)

##### Changing the Favicon Icon

By default, MkDocs uses the [MkDocs favicon](https://www.mkdocs.org/getting-started/#changing-the-favicon-icon) icon. To use a different icon, create an `img` subdirectory in the `docs` directory and copy your custom `favicon.ico` file to that directory. MkDocs will automatically detect and use that file as your favicon icon.

![](imgs/20260224-190712.png)

##### Building the Site

!!! info "Building the Site"

    That's looking good. You're ready to deploy the first pass of your `MkLorum` documentation.
    
    First build the documentation:
    
    ```bash
    mkdocs build
    ```
    
    ---
    
    This will create a new directory, named `site`. Take a look inside the directory:
    
    ```console
    $ ls site
    $ about fonts index.html license search.html css img js mkdocs sitemap.xml
    ```
    
- Notice that your source documentation has been output as two HTML files named `index.html` and `about/index.html`. 

- You also have various other media that's been copied into the `site` directory as part of the documentation theme.

- You even have a `sitemap.xml` file and `mkdocs/search_index.json`.

!!! pied-piper ""

    If you're using source code control such as `git` you probably don't want to check your documentation builds into the repository. Add a line containing `site/` to your `.gitignore` file.
    
    ```bash
    echo "site/" >> .gitignore
    ```
    
    ---
    
    - If you're using another source code control tool you'll want to check its documentation on how to ignore specific directories.
    
##### Other Commands and Options

!!! pied-piper "Other Commands and Options"

    There are various other commands and options available. For a complete list of commands, use the `--help` flag:
    
    ```bash
    mkdocs --help
    ```
    
!!! info "Options"

    To view a list of options available on a given command, use the `--help` flag with that command. For example, to get a list of all options available for the `build` command run the following:
    
    ```bash
    mkdocs build --help
    ```
    
##### Deploying

!!! quote "Deploying"

    The documentation site that you just built only uses static files so you'll be able to host it from pretty much anywhere. Simply upload the contents of the entire `site` directory to wherever you're hosting your website from and you're done. For specific instructions on a number of common hosts, see the [Deploying your Docs](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/deploying-your-docs.md) deploy page.
    

##### Getting Help

!!! pied-piper ""
    See the [User Guide](https://www.mkdocs.org/user-guide/) for more complete documentation of all of MkDocs' features.
    

---

!!! pied-piper ""
    To get help with MkDocs, please use the [GitHub Discussions](https://github.com/mkdocs/mkdocs/discussions) or [GitHub Issues](https://github.com/mkdocs/mkdocs/issues).
    

---

##### Useful Links

<div class="grid cards cols-3" markdown>

-   <span style="color: #2094f3">:material-download:</span> **Installation Guide**
    [:octicons-arrow-right-24: View Guide](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/installation.md){ .md-button style="border-color: #2094f3; color: #2094f3" }

    Step-by-step instructions to get MkDocs up and running.

-   <span style="color: #2094f3">:material-cog:</span> **Configuration (docs_dir)**
    [:octicons-arrow-right-24: View Config](https://github.com/mkdocs/mkdocs/blob/master/docs/user-guide/configuration.md#docs_dir){ .md-button style="border-color: #2094f3; color: #2094f3" }

    Learn how to set up your source directory structure.

-   <span style="color: #2094f3">:material-rocket-launch:</span> **Deploying Your Docs**
    [:octicons-arrow-right-24: View Guide](https://www.mkdocs.org/user-guide/deploying-your-docs/){ .md-button style="border-color: #2094f3; color: #2094f3" }

    How to publish your documentation to the web.

-   <span style="color: #4caf50">:material-map-legend:</span> **Documentation Layout**
    [:octicons-arrow-right-24: View Layout](https://www.mkdocs.org/user-guide/configuration/#nav){ .md-button style="border-color: #4caf50; color: #4caf50" }

    Configure the navigation and global site structure.

-   <span style="color: #4caf50">:material-forum:</span> **GitHub Discussions**
    [:octicons-arrow-right-24: Join Discussions](https://github.com/mkdocs/mkdocs/discussions){ .md-button style="border-color: #4caf50; color: #4caf50" }

    Ask questions and engage with the community.

-   <span style="color: #4caf50">:material-alert-circle:</span> **GitHub Issues**
    [:octicons-arrow-right-24: View Issues](https://github.com/mkdocs/mkdocs/issues){ .md-button style="border-color: #4caf50; color: #4caf50" }

    Report bugs or request new features.

-   <span style="color: #ff9800">:material-card-text:</span> **Site Name**
    [:octicons-arrow-right-24: View Settings](https://www.mkdocs.org/user-guide/configuration/#site_name){ .md-button style="border-color: #ff9800; color: #ff9800" }

    Define the title of your project and browser tab.

-   <span style="color: #ff9800">:material-brush:</span> **Theme**
    [:octicons-arrow-right-24: View Theme](https://www.mkdocs.org/user-guide/configuration/#theme){ .md-button style="border-color: #ff9800; color: #ff9800" }

    Customise the look and feel of your documentation.

-   <span style="color: #ff9800">:material-book-open-variant:</span> **User Guide**
    [:octicons-arrow-right-24: Open Guide](https://www.mkdocs.org/user-guide/){ .md-button style="border-color: #ff9800; color: #ff9800" }

    The complete manual for all MkDocs features.

</div>

---


