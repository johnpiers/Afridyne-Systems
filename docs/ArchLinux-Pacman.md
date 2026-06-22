---
icon: material/arch
---

<div style="display: none;">
  <h1>Header</h1>
</div>

![Local image](./assets/logo1.svg){ .center-image }


<div style="text-align: center;">
  <h1><a href="https://archlinux.org/" title="Return to the main page">Arch Linux</a></h1>
</div>

* [Home](https://archlinux.org/)
* [Packages](https://archlinux.org/packages/)
* [Forums](https://bbs.archlinux.org/)
* [Wiki](https://wiki.archlinux.org/)
* [GitLab](https://gitlab.archlinux.org/archlinux)
* [Security](https://security.archlinux.org/)
* [AUR](https://aur.archlinux.org/)
* [Download](https://archlinux.org/download/)
    
!!! info "Info"

    - The [pacman](https://pacman.archlinux.page/) [package manager](https://en.wikipedia.org/wiki/Package_manager) is one of the major distinguishing features of [Arch Linux](https://archlinux.org/). It combines a simple binary package format with an easy-to-use [Arch build system](https://wiki.archlinux.org/title/Arch_build_system). The goal of *pacman* is to make it possible to easily manage packages, whether they are from the [official repositories](https://wiki.archlinux.org/title/Official_repositories) or the user's own builds.

    ---

    - *Pacman* keeps the system up-to-date by synchronizing package lists with the master server. This server/client model also allows the user to download/install packages with a simple command, complete with all required dependencies.

    ---

    - *Pacman* is written in the [C](https://www.c-language.org/) programming language and uses the [bsdtar(1)](https://man.archlinux.org/man/bsdtar.1) [tar](https://en.wikipedia.org/wiki/tar_(computing)) format for packaging.
    

!!! tip "Tip"

     The [pacman](https://archlinux.org/packages/?name=pacman) package contains tools such as [makepkg](https://wiki.archlinux.org/title/Makepkg) and [vercmp(8)](https://man.archlinux.org/man/vercmp.8). Other useful tools such as [pactree](https://man.archlinux.org/man/pactree.8) and [checkupdates](https://man.archlinux.org/man/checkupdates.8) are found in [pacman-contrib](https://archlinux.org/packages/?name=pacman-contrib) ([formerly](https://gitlab.archlinux.org/pacman/pacman/commit/0c99eabd50752310f42ec808c8734a338122ec86) part of pacman). Run `pacman -Ql pacman pacman-contrib | grep -E 'bin/.+'` to see the full list.
     
 
### Usage

[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=1)

!!! tip "Tip"

    For those who have used other Linux distributions before, there is a helpful [Pacman/Rosetta](https://wiki.archlinux.org/title/Pacman/Rosetta) article.
    

### Installing Packages

[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=2)

!!! quote "Installing Packages"

    - A package is an archive containing:
    
    ---
    
    - *All of the (compiled) files of an application.*
    - *Metadata about the application, such as application name, version, dependencies, etc.*
    - Installation files and directives for *pacman*
    
    ---
    
    - Arch's package manager *pacman* can install, update, and remove those packages. Using packages instead of compiling and installing programs yourself has various benefits:
    
    - Easily updatable: *pacman* will update existing packages as soon as updates are available
    - Dependency checks: *pacman* handles dependencies for you, you only need to specify the program and *pacman* installs it together with every other program it needs.
    - Clean removal: *pacman* has a list of every file in a package; this way, no files are unintentionally left behind when you decide to remove a package.
    
!!! note "Note"

    Packages often have [optional dependencies](https://wiki.archlinux.org/title/PKGBUILD#optdepends) which are packages that provide additional functionality to the application but not strictly required for running it. When installing a package, *pacman* will list package's optional dependencies, but they will not be found in **pacman.log**. Use the [#Querying package databases](https://wiki.archlinux.org/title/Pacman#Querying_package_databases) command to view the optional dependencies of a package.
    
    When installing a package which you require only as a (optional) dependency of some other package (i.e. not required by you explicitly), it is recommended to use the **>--asdeps** option. For details, see the [Installation reason](https://wiki.archlinux.org/title/Pacman#Installation_reason) section.
    
!!! danger "Warning"

    When installing packages in Arch, avoid refreshing the package list without [upgrading the system](https://wiki.archlinux.org/title/Pacman#Upgrading_packages) (for example, when a [package is no longer found](https://wiki.archlinux.org/title/Pacman#Packages_cannot_be_retrieved_on_installation) in the official repositories). In practice, do **not** run pacman -Sy package_name instead of pacman -Syu package_name, as this could lead to dependency issues. See [System maintenance#Partial upgrades](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported) are unsupported and [BBS#89328.](https://bbs.archlinux.org/viewtopic.php?id=89328)
    

---
> ⚠️ **Warning**
> *   Users are expected to follow the guidance in the [System maintenance#Upgrading the system](https://wiki.archlinux.org/title/System_maintenance#Upgrading_the_system) section to upgrade their systems regularly and not blindly run the following command.
> *   Arch only supports full system upgrades. See [System maintenance#Partial upgrades are unsupported](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported) and [#Installing packages](https://wiki.archlinux.org/title/Pacman#Installing_packages) for details.
---
> ✨ **Tip**
> You can [enable/start](https://wiki.archlinux.org/title/Enable/start) the `pacman-filesdb-refresh.timer` (provided within the `pacman-contrib` package) to refresh *pacman* files database weekly.
---
### Installing Specific Packages

[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=3)

!!! info "Info"

    To install a single package or list of packages, including dependencies, issue the following command:
    
    ```
    # pacman -S package_name1 package_name2 ...
    ```
    
!!! pied-piper "Regex-package Install"

    To install a list of packages with regex (see [this forum thread](https://bbs.archlinux.org/viewtopic.php?id=7179)):
    
    ```
    # pacman -S $ (pacman -Ssq package_regex)
    ```
    
    Sometimes there are multiple versions of a package in different repositories (e.g. *extra* and *extra-testing*). To install the version from the *extra repository* in this example, the repository needs to be defined in front of the package name:
    
    ```
    # pacman -S extra/ package_name
    ```
    To install a number of packages sharing similar patterns in their names, one can use curly brace expansion. For example:
    
    ```
    # pacman -S plasma-{desktop,mediacenter,nm}
    ```
    
    This can be expanded to however many levels needed:
    
    ```
    # pacman -S plasma-{workspace{,-wallpapers},pa}
    ```
    

##### Virtual Packages {#Virtual_packages}

[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=4)

!!! info "Info"

    A virtual package is a special package which does not exist by itself, but is [provided](https://wiki.archlinux.org/title/PKGBUILD#provides) by one or more other packages. Virtual packages allow other packages to not name a specific package as a dependency, in case there are several candidates. Virtual packages cannot be installed by their name, instead they become installed in your system when you have installed a package providing the virtual package. An example is the [dbus-units](https://wiki.archlinux.org/title/D-Bus#Implementations) package.
    
!!! tip "Tip"

    When there are multiple candidates, the list of choices presented will sort first by [repositories](https://wiki.archlinux.org/title/Repository) in the order they appear in pacman.conf, then alphabetically when multiple results exist from the same repository.
    
##### Installing Package Groups {#Installing_Package_Groups}

[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=5)

!!! pied-piper "Installing Package Groups"

    Some packages belong to a [group of packages](https://wiki.archlinux.org/title/Meta_package_and_package_group) that can all be installed simultaneously. For example, issuing the command:
    
    ```bash
    # pacman -S gnome
    ```
    
    Will prompt you to select the packages from the [gnome](https://archlinux.org/groups/x86_64/gnome/) group that you wish to install.
    
    ---
    
    Sometimes a package group will contain a large amount of packages, and there may be only a few that you do or do not want to install. Instead of having to enter all the numbers except the ones you do not want, it is sometimes more convenient to select or exclude packages or ranges of packages with the following syntax:
    
    - Enter a selection (default=all): 1-10 15
    
    - Which will select packages 1 through 10 and 15 for installation, or:
    
    - Enter a selection (default=all): ^5-8 ^2
    
    - Which will select all packages except 5 through 8 and 2 for installation.
    
    ---
    
    To see what packages belong to the gnome group, run:
    
    ```
    $ pacman -Sg gnome
    ```
    
    ---
    
    Also [visit]( https://archlinux.org/groups/) to see what package groups are available.
    
    
!!! note "Note"

    If a package in the list is already installed on the system, it will be reinstalled even if it is already up-to-date. This behavior can be overridden with the `--needed` option.

### Removing Packages
[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=6)

!!! tip "Tip"

     To remove a single package, leaving all of its dependencies installed:
     
     ```
     # pacman -R package_name
     ```
    To remove a package and its dependencies which are not required by any other installed package:
    
    ```
    # pacman -Rs package_name
    ```
    
!!! danger "Warning"

    When removing a group, such as *gnome*, this ignores the install reason of the packages in the group, because it acts as though each package in the group is listed separately. Install reason of dependencies is still respected.
    
    The above may sometimes refuse to run when removing a group which contains otherwise needed packages. In this case try:
    
    ```
    # pacman -Rsu package_name
    ```
    
To remove a package, its dependencies and all the packages that depend on the target package:

!!! danger "Warning"

    This operation is recursive, and must be used with care since it can remove many potentially needed packages.
    
    ```
    # pacman -Rsc package_name
    ```
    
    To remove a package, which is required by another package, without removing the dependent package:
    
!!! danger "Warning"

    The following operation can break a system and should be avoided. See [System Maintenance](https://wiki.archlinux.org/title/System_maintenance#Avoid_certain_pacman_commands)
    
    ```
    # pacman -Rdd package_name
    ```
    *Pacman* saves important configuration files when removing certain applications and names them with the extension: *.pacsave*. To prevent the creation of these backup files use the **-n** option:
    
    ```
    # pacman -Rn package_name
    ```
!!! note "Note"

    - *Pacman* will not remove configurations that the application itself creates (for example "dotfiles" in the home directory)
    
    
### Upgrading Packages

[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=7)

!!! danger "Warning"

    - Users are expected to follow the guidance in the [System maintenance#Upgrading the system](https://wiki.archlinux.org/title/System_maintenance#Upgrading_the_system) section to upgrade their systems regularly and not blindly run the following command.
    
    - Arch only supports full system upgrades. See [System maintenance#Partial upgrades are unsupported](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported) and [#Installing packages](https://wiki.archlinux.org/title/Pacman#Installing_packages) for details.
    
### Querying Package Databases

[[edit source]](https://wiki.archlinux.org/index.php?title=Pacman&action=edit&section=8)

!!! tip "Tip"

    - *Pacman* can update all packages on the system with just one command. This could take quite a while depending on how up-to-date the system is. 
    
    - The following command synchronizes the repository databases *and* updates the system's packages, excluding "local" packages that are not in the configured repositories:
    
    ```
    # pacman -Syu
    ```
    
!!! pied-piper "Tip"

    - *Pacman* queries the local package database with the `-Q` flag, the sync database with the `-S` flag and the files database with the `-F` flag. 
    
    - See `pacman -Q --help`, `pacman -S --help` and `pacman -F --help` for the respective suboptions of each flag.
    
!!! note "Note."

    - Sync the files database before querying it to get up-to-date results:

    ```
    # pacman -Fy
    ```
    
!!! tip "Tip"

    - Pacman can search for packages in the database, searching both in packages' names and descriptions:

    ```
    $ pacman -Ss string1 string2 ...
    ```
    
!!! abstract "Tip"

    - Sometimes, -s's builtin ERE (Extended Regular Expressions) can cause a lot of unwanted results, so it has to be limited to match the package name only; not the description nor any other field:
    
    ```
    $ pacman -Ss '^vim-'
    ```
    
    - To search for already installed packages:
    
    ```
    $ pacman -Qs string1 string2 ...
    ```
    
!!! note "Note."

    - Packages often have [optional dependencies](https://wiki.archlinux.org/title/PKGBUILD#optdepends) which are packages that provide additional functionality to the application but not strictly required for running it. When installing a package, *pacman* will list a package's optional dependencies, but they will not be found in `pacman.log`. Use the [Querying package databases](https://wiki.archlinux.org/title/Pacman#Querying_package_databases) command to view the optional dependencies of a package.
    
    - When installing a package which you require only as a (optional) dependency of some other package (i.e. not required by you explicitly), it is recommended to use the `--asdeps` option. For details, see the [Installation reason](https://wiki.archlinux.org/title/Pacman#Installation_reason) section.
    

!!! tip "Tip"

    - When there are multiple candidates, the list of choices presented will sort first by [repositories](https://wiki.archlinux.org/title/Repository) in the order they appear in <code>pacman.conf</code>, then alphabetically when multiple results exist from the same repository.
    
     
??? warning "Warning"

    The Docker container is intended for local previewing purposes only and is not suitable for deployment. This is because the web server used by MkDocs for live previews is not designed for production use and may have security vulnerabilities.
    

!!! info "Info."

    If the ESP is not mounted to `/boot`, make sure to not rely on the [systemd automount mechanism](https://wiki.archlinux.org/title/Fstab#Automount_with_systemd "Fstab") (including that of [systemd-gpt-auto-generator](https://wiki.archlinux.org/title/Systemd#GPT_partition_automounting "Systemd")) during kernel upgrades. Always mount it manually prior to any system or kernel update, otherwise you may not be able to mount it after the update, locking you in the currently running kernel with no ability to update the copy of kernel on the ESP.

    Alternatively [preload the required kernel modules on boot](https://wiki.archlinux.org/title/Kernel_module#systemd "Kernel module"), e.g.:

    ```
    /etc/modules-load.d/vfat.conf
    ```

    ---

    ```
    vfat
    nls_cp437
    nls_ascii
    ```


!!! info "Abstract."

    If the ESP is not mounted to `/boot`, make sure to not rely on the [systemd automount mechanism](https://wiki.archlinux.org/title/Fstab#Automount_with_systemd "Fstab") (including that of [systemd-gpt-auto-generator](https://wiki.archlinux.org/title/Systemd#GPT_partition_automounting "Systemd")) during kernel upgrades. Always mount it manually prior to any system or kernel update, otherwise you may not be able to mount it after the update, locking you in the currently running kernel with no ability to update the copy of kernel on the ESP.

    Alternatively [preload the required kernel modules on boot](https://wiki.archlinux.org/title/Kernel_module#systemd "Kernel module"), e.g.:

    ```text {.no-copy .no-style}
    /etc/modules-load.d/vfat.conf
    ```

    ---

    ```text {.no-copy .no-style}
    vfat
    nls_cp437
    nls_ascii
    ```

![](imgs/20260131-222654.png){ .center-image }



### <u>Star S62</u> - Mermaid Diagram

```mermaid
graph TD
    A["Sagittarius A* (supermassive black hole)"] --> B["Orbit of Star S62"]
    B --> C["Periapsis (closest approach): 17.8 AU\n(AU = Astronomical Units, 1 AU ≈ Earth-Sun distance)"] 
    B --> D["Apoapsis (farthest distance): 1,462.2 AU\n(AU = Astronomical Units, 1 AU ≈ Earth-Sun distance)"]
    style A fill:#7a7878,stroke:#948686,stroke-width:2px
    style B fill:#4d6aa1,stroke:#747474,stroke-width:2px
    style C fill:#f05b5b,stroke:#000,stroke-width:2px
    style D fill:#4d964d,stroke:#000,stroke-width:2px
```

