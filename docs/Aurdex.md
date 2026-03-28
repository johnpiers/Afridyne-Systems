---
icon: material/alert-outline
---

<div style="display: none;"><h1>Header</h1></div>

![](imgs/20260228-175823.png){: style="display: block; margin: 0 auto"}

<H3 style="text-align: center;">Aurdex TUI for Browsing AUR Package Metadata.</H3>

##### Aurdex TUI

!!! abstract "Aurdex TUI"

    **"aurdex is a terminal user interface (TUI) for browsing AUR package metadata."**
    
    ---
    
    - Filter and search packages by name, maintainer, status, and more.
    - View detailed metadata, dependencies, and reverse dependencies.
    - Explore package git repositories and commit history.
    - View package comments from aurweb.

##### Not an Aur Helper
    
!!! quote "NB"

    Aurdex is **not** an AUR helper. It does **not** install or build packages.
    
    ---
    
    - It’s designed for `viewing package information` and understanding dependency relationships.
    
##### Screenshots
            
![AUR_Package_Browser_2025-06-24T20_40_26_492693](https://github.com/user-attachments/assets/d63b2ba5-e6cb-4c4d-a31e-6b355120fdcb)
![AUR_Package_Browser_2025-06-24T20_40_37_345778](https://github.com/user-attachments/assets/cf1bcaba-79b1-47f6-99d8-7afeb6105611)
![AUR_Package_Browser_2025-06-24T20_40_43_800563](https://github.com/user-attachments/assets/11398438-f363-49f2-a42b-7ae9ce433228)
![AUR_Package_Browser_2025-06-24T20_42_26_423139](https://github.com/user-attachments/assets/bece2564-7133-4436-a665-144311c83e29)

---


![](imgs/20260102-211054.png){: style="display: block; margin: 0 auto"}

---

##### Aurdex Terminal UI AUR

!!! info "Aurdex"

    **"Aurdex - A terminal UI for the Arch User Repository."**
    
    ---
    
    - Positional arguments:
    
    - package_name: Display information for a specific package and exit.
    
    ---
    
    
    ```
    options:
    
    -h, --help              Show this help message and exit.
    --version               Show program's version number and exit.
    --list-profiles         List available profiles and exit.
    --profile PROFILE       Load a specific profile on startup.
    
    -s, --search TERM [TERM ...] 
                            One or more search terms. Regular expressions are automatically
                            detected (e.g. '^lib.*').
                            
    -l, --limit LIMIT       Limit results to integer limit. Defaults to 20, '-1' sets to
                            infinite.
    -f, --filter key=value
                            Apply one or more filters (can be repeated and combined with
                            --search). Example: "-f maintainer=alice -f out_of_date" Supported
                            keys: maintainer, source, depends, makedepends, checkdepends,
                            optdepends, provides, out_of_date, abandoned, comaintainers,
                            license, arch, submitter
                            
    --deptree PACKAGE [PACKAGE ...]
                            Resolve and display the shallow dependency installation tree for
                            one or more packages.
                            
    --deptree-deep PACKAGE [PACKAGE ...]
                            Resolve and display the deep dependency installation tree for one
                            or more packages.
                            
    --rebuild               Force a full download and rebuild of the package database.
    --update                Download AUR metadata and update the package database.
    ```
    

---

##### Aurdex Abandoned

!!! pied-piper "Aurdex Abandoned"

    ``` markdown title="$ aurdex -f abandoned -f out_of_date -l 5"


    Running search for  with {'abandoned': 'true', 'out_of_date': 'true'}...
    Printing directly... 
    Found 5 packages (limit: 5).
    ```
    
    | Source | Name | Version | description |
    | :--- | :--- | :--- | :--- |
    | aur | dict-gcide | 0.53-4 | GNU version of the Collaborative International Dictionary of English for dictd et al. |
    | aur | openide-bin | 243.26053.27.8-1 | OpenID is an open source software development tool for Java, Python, and other programming languages. |
    | aur | friidump | [0.5.3.1-1 ](https://github.com/bradenmcd/friidump) | A program to dump Nintendo Wii and GameCube disc |
    | aur | rsvndump | [0.6.2-1](https://aur.archlinux.org/packages?O=0&K=rsvndump) | Remote Subversion repository dump. |
    | [aur](https://aur.archlinux.org/#) | aurvote-utils-git | [1.1.0.r7.g3e82548-1](https://aur.archlinux.org/packages?O=0&K=aurvote-utils-git) | A set of utilities for managing AUR votes |

---

##### Aurdex Example CLI Usage

##### Aurdex Installation

!!! quote "Aurdex Example CLI Usage"
    ```bash
    $ aurdex --deptree waydroid
    Resolving shallow dependency tree for: waydroid...
    📦 Installation Plan
    └── ✅ Step 1: Install Dependencies
        ├── Already satisfied
        │   ├── ✔️ bash
        │   ├── ✔️ dbus
        │   ├── ✔️ glib2
        │   ├── ✔️ glibc
        │   ├── ✔️ gmp
        │   ├── ✔️ gtk3
        │   ├── ✔️ libcap
        │   ├── ✔️ libidn2
        │   ├── ✔️ libnetfilter_conntrack
        │   ├── ✔️ libseccomp
        │   ├── ✔️ nettle
        │   ├── ✔️ nftables
        │   ├── ✔️ perl
        │   ├── ✔️ python
        │   ├── ✔️ python-dbus
        │   ├── ✔️ python-gobject
        │   ├── ✔️ rsync
        │   └── ✔️ wget
        ├── From Repositories
        │   ├── 📦 dnsmasq (2.91-1) (extra)
        │   └── 📦 lxc (1:6.0.4-2) (extra)
        └── From AUR
            ├── 🔨 libglibutil (1.0.80-1)
            ├── 🔨 libgbinder (1.1.42-2)
            ├── 🔨 python-gbinder (1.1.2-3)
            └── 🔨 waydroid (1.5.4-1)
    ```

    !!! info "Aurdex Installation"
        The **aurdex** tool is available in the **AUR** (Arch User Repository).

        You can install it using an AUR helper such as **yay** or **paru**:

        ```bash
        $ yay -S aurdex

        # or

        $ paru -S aurdex
        ```


---

##### Aurdex Manual Installation

!!! quote "Aurdex Manual Installation"

    ``` markdown title="Clone the package and build it with makepkg:"


     $ git clone https://aur.archlinux.org/aurdex.git
     $ cd aurdex
     $ makepkg -si
    ```
