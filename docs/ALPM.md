---
icon: material/arch
---

![](imgs/alpmarch.png){: style="display: block; margin: 0 auto"}

<H1 style="text-align: center;"> Arch Linux Package Management [ALPM]</H1>

[Go to: Contributing :fontawesome-solid-paper-plane:](CONTRIBUTING.md){ .md-button .md-button--custom }


!!! git "ALPM"

    This project comprises specifications, as well as [Rust] libraries and tools for **A** rch **L** inux **P** ackage **M** anagement.
    
    The ALPM project arose from the need for more clearly specifying the interfaces, as well as providing bindings and tools in a memory-safe programming language.
    
    The specifications and implementations are based on ad-hoc implementations in the [pacman] project. Currently, this project aims to maintain compatibility with [pacman] `5.1.0` and onwards.
    
    The scope of this project is to provide robust integration for all relevant package creation and consumption, as well as repository management tasks. As such, the ALPM project also aims at providing drop-in replacements or alternatives for some facilities provided by [pacman].
    
    This project has been financed by the [Sovereign Tech Agency].
    Read the [official announcement] for more information.
    
## Documentation

!!! abstract "Documentation"

    The latest project documentation can be found at the [alpm archlinux page](https://alpm.archlinux.page)
    
    Documentation for all current ALPM lints is available at the [alpm archlinux page/lints](https://alpm.archlinux.page/lints/)
    
## Overview

!!! desc "Overview"
    The following mindmap attempts to provide a high-level overview of the project and put file types as well as (existing and upcoming) libraries into context.

    ```mermaid
    mindmap
      root((ALPM))
        📂 Source
          📄 PKGBUILD
          📄 .SRCINFO
          📚️ alpm-pkgbuild
          ⌨️/📚️ alpm-srcinfo
        📦 Package
          📄 .BUILDINFO
          📄 .INSTALL
          📄 .MTREE
          📄 .PKGINFO
          ⌨️/📚️ alpm-buildinfo
          ⌨️/📚️ alpm-mtree
          📚️ alpm-package
          ⌨️/📚️ alpm-pkginfo
          ⌨️/📚️ alpm-soname
        🗄️ Repository
          📄 desc
          📄 files
          ⌨️/📚️ alpm-repo-db
        🗄️ Package Management
          📄 desc
          📄 files
          ⌨️/📚️ alpm-db
        ✅️ Linting
          ⌨️/📚️ alpm-lint
        💬 Language bindings
          🐍 python-alpm
        🛠️ Utils
          📚️ alpm-common
          📚️ alpm-compress
          📚️ alpm-parsers
    ```

    For an overview of planned specifications and components, refer to the [milestones] of the project.


## Components

Currently the following software components are available:

<div class="grid cards cols-3" markdown>

-   <span style="color: #4a90e2">:material-package-variant:</span> **alpm-buildinfo**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-buildinfo){ .md-button style="border-color: #4a90e2; color: #4a90e2" }

    A library and command line interface to work with BUILDINFO(5) files.

-   <span style="color: #4a90e2">:material-code-brackets:</span> **alpm-common**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-common){ .md-button style="border-color: #4a90e2; color: #4a90e2" }

    A library for common traits and functionality.

-   <span style="color: #4a90e2">:material-archive:</span> **alpm-compress**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-compress){ .md-button style="border-color: #4a90e2; color: #4a90e2" }

    A library for compression operations in ALPM.

-   <span style="color: #6d8c6d">:material-database:</span> **alpm-db**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-db){ .md-button style="border-color: #6d8c6d; color: #6d8c6d" }

    A library and CLI to work with [alpm-db(7)](https://alpm.archlinux.page/specifications/alpm-db.7.html), [alpm-db-desc(5)](https://alpm.archlinux.page/specifications/alpm-db-desc.5.html), and [alpm-db-files(5)](https://alpm.archlinux.page/specifications/alpm-db-files.5.html).

-   <span style="color: #6d8c6d">:material-check-decagram:</span> **alpm-lint**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-lint){ .md-button style="border-color: #6d8c6d; color: #6d8c6d" }

    A linting tool for everything around Arch Linux packaging.

-   <span style="color: #6d8c6d">:material-file-tree:</span> **alpm-mtree**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-mtree){ .md-button style="border-color: #6d8c6d; color: #6d8c6d" }

    A library and command line interface to work with ALPM-MTREE(5) files.

-   <span style="color: #c06c5d">:material-archive-outline:</span> **alpm-package**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-package){ .md-button style="border-color: #c06c5d; color: #c06c5d" }

    A library for the creation of [alpm-package(7)](https://alpm.archlinux.page/specifications/alpm-package.7.html) files.

-   <span style="color: #c06c5d">:material-xml:</span> **alpm-parsers**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-parsers){ .md-button style="border-color: #c06c5d; color: #c06c5d" }

    A library for providing various custom parsers/deserializers for ALPM.

-   <span style="color: #c06c5d">:material-information-outline:</span> **alpm-pkginfo**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-pkginfo){ .md-button style="border-color: #c06c5d; color: #c06c5d" }

    A library and command line interface to work with PKGINFO(5) files.

-   <span style="color: #bfa05a">:material-server:</span> **alpm-repo-db**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-repo-db){ .md-button style="border-color: #bfa05a; color: #bfa05a" }

    A library and CLI for [alpm-repo-db(7)](https://alpm.archlinux.page/specifications/alpm-repo-db.7.html), [desc](https://alpm.archlinux.page/specifications/alpm-repo-desc.5.html), and [files](https://alpm.archlinux.page/specifications/alpm-repo-files.5.html) formats.

-   <span style="color: #bfa05a">:material-link-variant:</span> **alpm-soname**
    [:octicons-arrow-right-24: Go to](https://crates.io/crates/alpm-soname){ .md-button style="border-color: #bfa05a; color: #bfa05a" }

    A library and command line interface for looking up soname data.

-   <span style="color: #bfa05a">:material-script-text:</span> **alpm-srcinfo**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-srcinfo){ .md-button style="border-color: #bfa05a; color: #bfa05a" }

    A library and command line interface to work with SRCINFO(5) files.

-   <span style="color: #847eab">:material-shape-plus:</span> **alpm-types**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/alpm-types){ .md-button style="border-color: #847eab; color: #847eab" }

    A central library for types used by other ALPM libraries and tools.

-   <span style="color: #847eab">:material-language-python:</span> **python-alpm**
    [:octicons-arrow-right-24: Go to](https://github.com/archlinux/alpm/tree/main/python-alpm){ .md-button style="border-color: #847eab; color: #847eab" }

    Python bindings for ALPM crates and the python-alpm Python library.

-   <span style="color: #847eab">:material-key-variant:</span> **archlinux-keyring**
    [:octicons-arrow-right-24: Go to](https://gitlab.archlinux.org/archlinux/archlinux-keyring/){ .md-button style="border-color: #847eab; color: #847eab" }

    Arch Linux PGP keyring management and trust database.

</div>

## Contributing

!!! ex "Contributing"

    Please refer to the [contribution guidelines] to learn how to contribute to this project.
    
## Releases

!!! git "Releases"

    Releases of [components] are created by the developers of this project.
    
    [OpenPGP certificates] with the following [OpenPGP fingerprints] can be used to verify signed tags:
    
    - [`3051329b47b855c4f888f975cc9408f679023b65`] ([Arne Christian Beer] &lt;<nukesor@archlinux.org>&gt;)
    - [`991f6e3f0765cf6295888586139b09da5bf0d338`] ([David Runge] &lt;<dvzrv@archlinux.org>&gt;)
    - [`165e0ff7c48c226e1ec363a7f83424824b3e4b90`] ([Orhun Parmaksız] &lt;<orhun@archlinux.org>&gt;)
    
    ---
    
    Some of the above are part of [archlinux-keyring] and certified by at least three [main signing keys] of the distribution.
    
## License

!!! desc "License"

    This project can be used under the terms of the [Apache-2.0] or [MIT].
    
    Contributions to this project, unless noted otherwise, are automatically licensed under the terms of both of those licenses.
    

[ALPM-MTREE(5)]: https://alpm.archlinux.page/specifications/ALPM-MTREE.5.html
[Apache-2.0]: https://github.com/archlinux/alpm/blob/main/LICENSES/Apache-2.0.txt
[Arne Christian Beer]: https://archlinux.org/people/support-staff/#nukesor
[BUILDINFO(5)]: https://alpm.archlinux.page/specifications/BUILDINFO.5.html
[David Runge]: https://archlinux.org/people/developers/#dvzrv
[MIT]: https://github.com/archlinux/alpm/blob/main/LICENSES/MIT.txt
[OpenPGP certificates]: https://openpgp.dev/book/certificates.html
[OpenPGP fingerprints]: https://openpgp.dev/book/certificates.html#fingerprint
[Orhun Parmaksız]: https://archlinux.org/people/package-maintainer/#orhun
[PKGINFO(5)]: https://alpm.archlinux.page/specifications/PKGINFO.5.html
[Rust]: https://www.rust-lang.org/
[SRCINFO(5)]: https://alpm.archlinux.page/specifications/SRCINFO.5.html
[Sovereign Tech Agency]: https://www.sovereign.tech/tech/arch-linux-package-management
[`165e0ff7c48c226e1ec363a7f83424824b3e4b90`]: https://pgpkeys.eu/pks/lookup?search=165e0ff7c48c226e1ec363a7f83424824b3e4b90&fingerprint=on&op=index
[`3051329b47b855c4f888f975cc9408f679023b65`]: https://pgpkeys.eu/pks/lookup?search=3051329b47b855c4f888f975cc9408f679023b65&fingerprint=on&op=index
[`991f6e3f0765cf6295888586139b09da5bf0d338`]: https://pgpkeys.eu/pks/lookup?search=991f6e3f0765cf6295888586139b09da5bf0d338&fingerprint=on&op=index
[alpm-buildinfo]: https://github.com/archlinux/alpm/tree/main/alpm-buildinfo
[alpm-common]: https://github.com/archlinux/alpm/tree/main/alpm-common
[alpm-compress]: https://github.com/archlinux/alpm/tree/main/alpm-compress
[alpm-db(7)]: https://alpm.archlinux.page/specifications/alpm-db.7.html
[alpm-db-desc(5)]: https://alpm.archlinux.page/specifications/alpm-db-desc.5.html
[alpm-db-files(5)]: https://alpm.archlinux.page/specifications/alpm-db-files.5.html
[alpm-db]: https://github.com/archlinux/alpm/tree/main/alpm-db
[alpm-lint]: https://github.com/archlinux/alpm/tree/main/alpm-lint
[alpm-mtree]: https://github.com/archlinux/alpm/tree/main/alpm-mtree
[alpm-package(7)]: https://alpm.archlinux.page/specifications/alpm-package.7.html
[alpm-package]: https://github.com/archlinux/alpm/tree/main/alpm-package
[alpm-parsers]: https://github.com/archlinux/alpm/tree/main/alpm-parsers
[alpm-pkginfo]: https://github.com/archlinux/alpm/tree/main/alpm-pkginfo
[alpm-repo-db(7)]: https://alpm.archlinux.page/specifications/alpm-repo-db.7.html
[alpm-repo-db]: https://github.com/archlinux/alpm/tree/main/alpm-repo-db
[alpm-repo-desc(5)]: https://alpm.archlinux.page/specifications/alpm-repo-desc.5.html
[alpm-repo-files(5)]: https://alpm.archlinux.page/specifications/alpm-repo-files.5.html
[alpm-soname]: https://github.com/archlinux/alpm/tree/main/alpm-srcinfo
[alpm-srcinfo]: https://github.com/archlinux/alpm/tree/main/alpm-srcinfo
[alpm-types]: https://github.com/archlinux/alpm/tree/main/alpm-types
[archlinux-keyring]: https://gitlab.archlinux.org/archlinux/archlinux-keyring
[components]: #components
[contribution guidelines]: CONTRIBUTING.md
[main signing keys]: https://archlinux.org/master-keys/
[milestones]: https://gitlab.archlinux.org/archlinux/alpm/alpm/-/milestones
[official announcement]: https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/thread/MZLH43574GGP7QQ7RKAAIRFT5LJPCEB4/
[pacman]: https://gitlab.archlinux.org/pacman/pacman
[python-alpm]: https://github.com/archlinux/alpm/tree/main/python-alpm


<div style="text-align: center; margin: 0 auto; max-width: 560px;">
    <iframe title="Work on the ALPM project in 2024 and 2025" width="560" height="315" src="https://clip.place/videos/embed/7t8AZALDB3A1C6qyhPf4Sm" allow="fullscreen" sandbox="allow-same-origin allow-scripts allow-popups allow-forms" style="border: 0px;"></iframe>
</div>


<h4 style="text-align: center;">
    <ins>
        <a href="https://clip.place/w/7t8AZALDB3A1C6qyhPf4Sm">MindMap</a>
    </ins>
</h4>

[Go to: Contributing :fontawesome-solid-paper-plane:](CONTRIBUTING.md){ .md-button .md-button--custom }
