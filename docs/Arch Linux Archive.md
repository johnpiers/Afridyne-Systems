---
icon: material/arch
---

![](imgs/20251231-204146.png){ .center-image }
<H1 style="text-align: center;"> Arch Linux Archive</H1>

!!! quote " Arch Linux Archive"
    
    The Arch Linux Archive (a.k.a. ALA), formerly known as Arch Linux Rollback Machine (a.k.a. ARM), stores official repositories snapshots, iso images and bootstrap tarballs across time.

<b>You can use it to:</b>

* Downgrade to a previous version of one package (last version is broken, I want the previous one)
* Restore all your packages at a precise moment (my system is broken, I want to go back 2 months ago)
* Find a previous version of an ISO image


Packages are only kept for a few years, afterwards they are moved to the Arch Linux Historical Archive on archive.org

## 1. Location<a id="Location"></a><a id="1. Location"></a>


The Arch Linux Archive is available at [Arch Linux Archive](https://archive.archlinux.org/) and [mirrors](https://gitlab.archlinux.org/archlinux/infrastructure/-/blob/master/docs/servers.md#archive-mirrors) around the globe.

The [source code](https://github.com/seblu/archivetools) is also available for setting up your own mirror.

## 2. Directories<a id="Directories"></a><a id="2. Directories"></a>

The Archive is split into 3 main directories detailed below.

!!! quote "3 Main Directories"

    ```
    ├── iso
    ├── packages
    └── repos
    ```

#### 2.1 /repos<a id="/repos"></a><a id=".2Frepos"></a>

The [repos](https://archive.archlinux.org/repos) directory contains daily snapshots of official mirror organized by date like in the following example.

??? quote "Index of /repos/"

    ```
    repos
    ├── 2013
    │   ├── 08
    │   │   └── 31
    │   │       ├── community
    │   │       ├── community-staging
    │   │       ├── community-testing
    │   │       ├── core
    │   │       ├── extra
    │   │       ├── gnome-unstable
    │   │       ├── kde-unstable
    │   │       ├── lastsync
    │   │       ├── multilib
    │   │       ├── multilib-staging
    │   │       ├── multilib-testing
    │   │       ├── pool
    │   │       ├── staging
    │   │       └── testing
    │   ├── 09
    │   │   ├── 01
    │   │   ├── 02
    │   │   ├── ...
    │   │   ├── 21
    │   │   └── 22
    │   ├── 10
    │   │   ├── 01
    │   │   ├── 02
    │   │   ├── ...
    │   │
    │   ├── 11
    │   └── 12
    ├── 2014
    │   ├── 01
    │   │   ├── 01
    │   │   ├── 02
    │   │   ├── ...
    │   │
    │   ├── 02
    │   ├── 03
    │   ├── ...
    │   └── 09
    │       ├── 01
    │       ├── ...
    │       └── 28
    ├── last
    ├── month
    └── week
    ```

#### 2.2 /repos<a id="/packages"></a><a id=".2Fpackages"></a>

The packages directory contains all versions of each package with their signatures. One directory by package and package directories are grouped by their first letter.

??? quote "Packages Directory-Contains All v. of each Package"

    ```
    packages
    │── packages
    │   ├── a
    │   │   ├── awesome
    │   │   │   ├── awesome-4.3-2-x86_64.pkg.tar.zst
    │   │   │   ├── awesome-4.3-2-x86_64.pkg.tar.zst.sig
    │   │   │   ├── awesome-4.3-3-x86_64.pkg.tar.zst
    │   │   │   ├── awesome-4.3-3-x86_64.pkg.tar.zst.sig
    │   │   │   ├── ...
    │   │   │
    │   │   ├── ...
    │   │   ├── awstats
    │   │   └── axel
    │   │
    │   ├── b
    │   ├── ...
    │   └── z
    ```

You can use the magic subdirectory<code><b>.all</b></code>to access all packages by their name. It acts as a flat directory containing all versions of every package.

??? quote ""Magic Subdirectory" .all"

    ```
    ├── packages
    │   ├── .all
    │   │   ├── awesome-4.3-2-x86_64.pkg.tar.zst
    │   │   ├── ...
    │   │   ├── zsh-5.8-1-x86_64.pkg.tar.zst
    │   │   ├── zsh-5.8.1-1-x86_64.pkg.tar.zst
    │   │   └── ...
    ``` 

You can download the full package list (there are over a hundred thousand packages) as a compressed index: [index.0.xz](https://archive.archlinux.org/packages/.all/index.0.xz)

!!! example "Curl Example-Download Full Package List"

    ```bash
    $ curl
    https://archive.archlinux.org/packages/.all/index.0.xz | unxz
    ```

    ---

    ```bash {.no-copy}
    0ad-a23.1-2-x86_64
    0ad-a23.1-3-x86_64
    ...
    zziplib-0.13.69-1-x86_64
    zziplib-0.13.70-1-x86_64
    ```

#### 2.3 /iso<a id="/iso"></a><a id=".2Fiso"></a>

The [iso](https://archive.archlinux.org/iso/) directory contains official ISO images and bootstrap tarballs sorted by release date.


??? quote "Index of /iso/"

    ```bash {.no-copy}
    ├── 2014.09.03
    ├── 2014.10.01
    ├── 2014.11.01
    ├── 2014.12.01
    ├── 2015.07.01
    ├── 2015.08.01
    ├── 2015.09.01
    └── 2017.04.01
      ├── arch
      ├── archlinux-2017.04.01-x86_64.iso
      ├── archlinux-2017.04.01-x86_64.iso.sig
      ├── archlinux-2017.04.01-x86_64.iso.torrent
      ├── archlinux-bootstrap-2017.04.01-x86_64.tar.gz
      ├── archlinux-bootstrap-2017.04.01-x86_64.tar.gz.sig
      ├── md5sums.txt
      └── sha1sums.txt
    ```

!!! tip "Tip"
    
    Since release 2022.10.01, the Arch Linux Archive is also added as a WebSeed to the torrents (but not magnet links). All torrent files can be downloaded from [the release page](https://archlinux.org/releng/releases/).

## 3. Frequently Asked Questions<a id="Frequently_asked_questions"></a><a id="Frequently_asked_questions"></a>

#### 3.1 How to downgrade one package.<a id="How to downgrade one package."></a><a id=".3FHow to downgrade one package."></a>
Find the package you want under [/packages](https://wiki.archlinux.org/title/Arch_Linux_Archive#/packages) and let pacman fetch it for installation. For example:

!!! quote ".pkg.tar.zst"

    ```
    # pacman -U https://archive.archlinux.org/packages/<i>path/packagename</i>.pkg.tar.zst
    ```

!!! abstract "Auto .pkg & pacman.conf"

    ``` markdown title="If the automatic download is not for you, use the alternative, download and install the package manually using pacman -U"


    Letting pacman fetch it will automatically download the package's detached
    `.sig` file and verify it according to `/etc/pacman.conf` settings. 
     
    ```

See also [Downgrading packages#Automation](https://wiki.archlinux.org/title/Downgrading_packages#Automation) for tools that simplify the process.

#### 3.2 How to restore all packages to a specific date.<a id="How to restore all packages to a specific date."></a><a id=".3FHow to restore all packages to a specific date."></a>

To restore all packages to their version at a specific date, let us say 30 March 2014, you have to direct pacman to this date, by editing your /etc/pacman.conf and use the following server directive:

!!! abstract "Restore Packages to Specific Date"

    ``` markdown title="Package Required"


    [core]
    SigLevel = PackageRequired 
    Server = https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
    
    [extra]
    SigLevel = PackageRequired
    Server = https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
    ```

or by replacing your ``/etc/pacman.d/mirrorlist`` with the following content:

!!! abstract "Mirrorlist"

    ``` markdown title="/etc/pacman.d/mirrorlist"


    ##
    ## Arch Linux repository mirrorlist 
    ## Generated on 2042-01-01
    ##
    Server = https://archive.archlinux.org/repos/2014/03/30/$repo/os/$arch
    
    ```


!!! pied-piper "Note!"

    In May 2023 the [community repository](https://archlinux.org/news/git-migration-completed/) has been removed. If you need to downgrade beyond that point, you must add a similar community entry.

Then update the database and force downgrade:

!!! example "Pacman"

        # sudo pacman -Syyuu
 
If you get errors complaining about corrupted/invalid packages due to PGP signature, try to first update separately [archlinux-keyring](https://archlinux.org/packages/?name=archlinux-keyring) and [ca-certificates](https://archlinux.org/packages/?name=ca-certificates). Alternatively, you can decide to temporarily [disable signature checking](https://wiki.archlinux.org/title/Pacman/Package_signing#Disabling_signature_checking) altogether.

!!! danger "Partial Upgrades are Unsupported!"

    It is [not safe](https://wiki.archlinux.org/title/Partial_upgrade) to mix Archive and up-to-date mirrors. In case of a download failure, you will fall-back on an upstream package and you will have packages not from the same epoch in the rest of the system.

## 4. Historical Archive<a id="Historical Archive"></a><a id="Historical Archive"></a>

Maintaining the Arch Linux Archive consumes significant amount of resources, so old packages are cleaned up from time to time.

Before removing them, old packages are uploaded to a [dedicated collection "Arch Linux Historical Archive" on archive.org](https://archive.org/details/archlinuxarchive).

The Historical Archive does not provide a way to access a "snapshot" of Arch packages at a given point in time. However, there is a redirection on archive.archlinux.org so that downloads for old packages are redirected to the Historical Archive on archive.org. There should be no visible impact from the user side, except from the fact that archive.org is generally quite slow for downloading.

#### 4.1 Finding packages in the Historical Archive.<a id="Finding packages in the Historical Archive."></a><a id=".4FFinding packages in the Historical Archive."></a>

The **Arch Linux Historical Archive** collection has an [index of all packages:](https://archive.org/details/archlinuxarchive)

It is also possible to directly access a package by its **identifier**. The general pattern for identifiers is _archlinux_pkg_sanitized_package_name._

To obtain the _sanitized_ package name, simply replace any @, + or . character in the package name by an underscore _.

For instance, the identifier for [lucene++](https://archlinux.org/packages/?name=lucene%2B%2B) is archlinux_pkg_lucene__.

You can then access the details page of a package via its [identifier](https://archive.org/details/archlinux_pkg_lucene__), for instance: [archlinux_pkg_lucene__](https://archive.org/details/archlinux_pkg_lucene__).

It is also possible to run searches with the [archive.org Python client:](https://github.com/jjjake/internetarchive)

#### 4.2 Downloading packages from the Historical Archive.<a id="Downloading packages from the Historical Archive."></a><a id=".4FDownloading packages from the Historical Archive."></a>

All available package versions (and their signature) can be accessed via the download page of a [package:](https://archive.org/download/archlinux_pkg_lucene__).

To download, verify and install a package using [pacman:](https://wiki.archlinux.org/title/Pacman)

```bash
# sudo pacman -U https://archive.org/download/archlinux_pkg_cjdns/
cjdns-20.5-1-x86_64.pkg.tar.zst
```
Package verification is controlled by pacman's RemoteFileSigLevel option. Note that if you use pacman, you have to figure out the dependencies yourself.

It is also possible to use the [archive.org Python client](https://github.com/jjjake/internetarchive).

Download a specific version of a package:
```bash
$ ia download archlinux_pkg_cjdns cjdns-20.5-1-x86_64.pkg.tar.zst{,.sig}
```
Download all x86_64 versions of a package, with signatures:
```bash
$ ia download archlinux_pkg_cjdns --glob="*x86_64.pkg.tar.*"
```
## 5. History<a id="History"></a><a id="History"></a>

* The original ARM (Archlinux Rollback Machine) was closed on 2013-08-18.[[1]](https://bbs.archlinux.org/viewtopic.php?pid=1313360#p1313360)
* It was then hosted on [seblu.net](https://seblu.net/) since 2013-08-31. 
* New URL and closing the old ARM hierarchy on 2015-10-13. A new software, [agetpkg-git](https://aur.archlinux.org/packages/agetpkg-git/)<small> AUR</small> was introduced.
* Moved to [archive.archlinux.org](https://archive.archlinux.org/) on 2015-12-19.[[2]](https://lists.archlinux.org/archives/list/arch-dev-public@lists.archlinux.org/message/WFG4Z3CIHOYSEGRP6PRD2WGW2YJB3TFN/)
* Old packages from 2013-2016 uploaded to [archive.org](https://archive.org/details/archlinuxarchive) on 2018-06-05.



!!! warning "$ systemd-cgtop"
    ```
    systemd-cgtop
    -------------------------------------------------------------------------------------------------
    Control Group                            Tasks   %CPU   Memory  Input/s Output/s
    user.slice                                 540  152,8     3.3G        -        -
    user.slice/user-1000.slice                 540  152,8     3.3G        -        -
    user.slice/u…000.slice/session-1.scope     425  149,5     3.1G        -        -
    system.slice                                37      -   215.6M        -        -
    ```

!!! warning "$ systemd"

    ```text
    systemd-cgtop
    -------------------------------------------------------------------------------------------------
    Packages for common Linux
    ```

!!! quote "Quote"

    - Admonitions, also known as <em>call-outs</em>, are an excellent choice for including side content without significantly interrupting the document flow.
    
    - Material for MkDocs provides several different types of admonitions and allows for the inclusion and nesting of arbitrary content.


!!! pied-piper "Pied Piper"

    ``` markdown title="The last 3 special directories."


     NB: The last 3 special directories (last, week and month) which links repectively to
     the last synced repository, to the last Monday and to the first of the current month.
    ```


!!! note "The Title"

    - The content is correctly parsed because it's separated by blank lines from the raw HTML block tags.
    

