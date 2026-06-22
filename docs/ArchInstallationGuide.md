---
icon: material/arch
---

<div style="display: none;">
  <h1>Header</h1>
</div>

![Local image](./assets/logo1.svg){ .center-image }

<div align="center">
<a href="https://gist.github.com/mjkstra/96ce7a5689d753e7a6bdd92cdc169bae/"" title="Return to the main page"><h2>Arch Linux Installation Guide</h2></a>
 </div>

####     Table Of Contents:

<div class="grid cards cols-3" markdown>

-   <span style="color: #607d8b">:material-information-outline:</span> **Introduction**
    [:octicons-arrow-right-24: Go to section](#introduction){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Jump to the introduction.

-   <span style="color: #89b4fa">:material-clipboard-list-outline:</span> **Preliminary Steps**
    [:octicons-arrow-right-24: Go to section](#preliminary-steps){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Initial preparation and requirements.

-   <span style="color: #009688">:material-hammer-wrench:</span> **Main Installation**
    [:octicons-arrow-right-24: Go to section](#main-installation){ .md-button style="border-color: #009688; color: #009688" }
    The core installation process.

-   <span style="color: #607d8b">:material-file-tree:</span> **Disk Partitioning**
    [:octicons-arrow-right-24: Go to section](#disk-partitioning){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Set up your drive partitions.

-   <span style="color: #89b4fa">:material-format-paint:</span> **Disk Formatting**
    [:octicons-arrow-right-24: Go to section](#disk-formatting){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Format partitions with file systems.

-   <span style="color: #009688">:material-harddisk:</span> **Disk Mounting**
    [:octicons-arrow-right-24: Go to section](#disk-mounting){ .md-button style="border-color: #009688; color: #009688" }
    Mount the drives to the system.

-   <span style="color: #607d8b">:material-package-variant-closed:</span> **Packages Installation**
    [:octicons-arrow-right-24: Go to section](#packages-installation){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Install the base system packages.

-   <span style="color: #89b4fa">:material-file-table:</span> **Fstab**
    [:octicons-arrow-right-24: Go to section](#fstab){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Generate the filesystem table.

-   <span style="color: #009688">:material-console:</span> **Context Switch**
    [:octicons-arrow-right-24: Go to section](#context-switch-to-our-new-system){ .md-button style="border-color: #009688; color: #009688" }
    Chroot into the new system.

-   <span style="color: #607d8b">:material-clock-outline:</span> **Time Zone**
    [:octicons-arrow-right-24: Go to section](#set-up-the-time-zone){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Configure local time settings.

-   <span style="color: #89b4fa">:material-keyboard-outline:</span> **Language & Keyboard**
    [:octicons-arrow-right-24: Go to section](#set-up-the-language-and-tty-keyboard-map){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Set up locale and TTY layout.

-   <span style="color: #009688">:material-dns-outline:</span> **Hostname & Hosts**
    [:octicons-arrow-right-24: Go to section](#hostname-and-host-configuration){ .md-button style="border-color: #009688; color: #009688" }
    Network identification settings.

-   <span style="color: #607d8b">:material-account-cog-outline:</span> **Root & Users**
    [:octicons-arrow-right-24: Go to section](#root-and-users){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Set passwords and create users.

-   <span style="color: #89b4fa">:material-cog-outline:</span> **Grub Configuration**
    [:octicons-arrow-right-24: Go to section](#grub-configuration){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Install and configure the bootloader.

-   <span style="color: #009688">:material-power:</span> **Unmount & Reboot**
    [:octicons-arrow-right-24: Go to section](#unmount-everything-and-reboot){ .md-button style="border-color: #009688; color: #009688" }
    Safely exit and restart.

-   <span style="color: #607d8b">:material-camera-timer:</span> **Snapshot Updates**
    [:octicons-arrow-right-24: Go to section](#automatic-snapshot-boot-entries-update){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Manage automatic boot entries.

-   <span style="color: #89b4fa">:material-cube-outline:</span> **Virtualbox Support**
    [:octicons-arrow-right-24: Go to section](#virtualbox-support){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Guest additions and tools.

-   <span style="color: #009688">:material-package-variant:</span> **Distrobox & Toolbox**
    [:octicons-arrow-right-24: View Distrobox](https://distrobox.it){ .md-button style="border-color: #009688; color: #009688" }
    Run any Linux distribution inside your terminal.

</div>

<div class="grid cards cols-3" markdown>

-   <span style="color: #607d8b">:material-archive-arrow-down-outline:</span> **AUR & Packages**
    [:octicons-arrow-right-24: Go to section](#aur-helper-and-additional-packages-installation){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Install AUR helpers and extra tools.

-   <span style="color: #89b4fa">:material-check-all:</span> **Finalization**
    [:octicons-arrow-right-24: Go to section](#finalization){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Final system tweaks.

-   <span style="color: #009688">:material-video-input-component:</span> **Video Drivers**
    [:octicons-arrow-right-24: Go to section](#video-drivers){ .md-button style="border-color: #009688; color: #009688" }
    GPU driver installation.

-   <span style="color: #607d8b">:material-cpu-64-bit:</span> **AMD**
    [:octicons-arrow-right-24: Go to section](#amd){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Configuration for AMD hardware.

-   <span style="color: #89b4fa">:material-layers-triple-outline:</span> **32-Bit Support**
    [:octicons-arrow-right-24: Go to section](#32-bit-support){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Enable multilib support.

-   <span style="color: #009688">:material-nvme:</span> **Nvidia**
    [:octicons-arrow-right-24: Go to section](#nvidia){ .md-button style="border-color: #009688; color: #009688" }
    Configuration for Nvidia hardware.

-   <span style="color: #607d8b">:material-integrated-circuit-chip:</span> **Intel**
    [:octicons-arrow-right-24: Go to section](#intel){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Configuration for Intel hardware.

-   <span style="color: #89b4fa">:material-monitor-dashboard:</span> **Graphical Env.**
    [:octicons-arrow-right-24: Go to section](#setting-up-a-graphical-environment){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Set up your desktop workspace.

-   <span style="color: #009688">:material-desktop-tower:</span> **KDE Plasma**
    [:octicons-arrow-right-24: Go to section](#option-1-kde-plasma){ .md-button style="border-color: #009688; color: #009688" }
    Install the Plasma desktop.

-   <span style="color: #607d8b">:material-border-all-variant:</span> **Hyprland [WIP]**
    [:octicons-arrow-right-24: Go to section](#option-2-hyprland-wip){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Install the Hyprland compositor.

-   <span style="color: #89b4fa">:material-login:</span> **Display Manager**
    [:octicons-arrow-right-24: Go to section](#adding-a-display-manager){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Login screen configuration.

-   <span style="color: #009688">:material-controller:</span> **Gaming**
    [:octicons-arrow-right-24: Go to section](#gaming){ .md-button style="border-color: #009688; color: #009688" }
    General gaming setup.

-   <span style="color: #607d8b">:material-gamepad-variant-outline:</span> **Gaming Clients**
    [:octicons-arrow-right-24: Go to section](#gaming-clients){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Steam, Lutris, and more.

-   <span style="color: #89b4fa">:material-microsoft-windows:</span> **Windows Compat.**
    [:octicons-arrow-right-24: Go to section](#windows-compatibility-layers){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Wine and Proton settings.

-   <span style="color: #009688">:material-speedometer:</span> **Optimizations**
    [:octicons-arrow-right-24: Go to section](#generic-optimizations){ .md-button style="border-color: #009688; color: #009688" }
    Performance tuning.

-   <span style="color: #607d8b">:material-chart-areaspline:</span> **Monitoring**
    [:octicons-arrow-right-24: Go to section](#overclocking-and-monitoring){ .md-button style="border-color: #607d8b; color: #607d8b" }
    Track system performance.

-   <span style="color: #89b4fa">:material-notebook-edit-outline:</span> **Additional Notes**
    [:octicons-arrow-right-24: Go to section](#additional-notes){ .md-button style="border-color: #89b4fa; color: #89b4fa" }
    Extra info and tips.

-   <span style="color: #009688">:material-plus-box-outline:</span> **Things To Add**
    [:octicons-arrow-right-24: Go to section](#things-to-add){ .md-button style="border-color: #009688; color: #009688" }
    Future roadmap items.

</div>

## Introduction

!!! quote "Introduction"

    - The goal of this guide is to help new users set up a modern and minimal installation of **Arch Linux** with **BTRFS** on an **UEFI system**. I'll start from the basic terminal installation and then set up **video drivers, a desktop environment and provide basic gaming configuration**.
    
    - This guide is thought to be read alongside the wiki, so that it if something ever changes you can fix it but it's not necessary unless my guide becomes outdated. Also I will mention external references to justify some choices that I've made so that curious users can delve into the details.
    
### Note That:

!!! note "NOTE that:"

    - I **won't** prepare the system for **secure boot** because the procedure of custom key enrollment in the BIOS is dangerous and [can lead to a bricked system](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Creating_and_enrolling_keys). If you are wondering why I'm not using the default OEM keys in the BIOS, it's because they will make secure boot useless by being more than likely [not secure enough](https://wiki.archlinux.org/title/Unified_Extensible_Firmware_Interface/Secure_Boot#Implementing_Secure_Boot).
    
    ---
    
    - "I have decided against system encryption as it is unnecessary and introduces boot-phase overhead, which can noticeably delay start-up depending on the configuration." However it may be important for you so if you really want to go this way. I'd recommend reading [the wiki page in this regards](https://wiki.archlinux.org/title/Dm-crypt) and **must** perform the documented steps **IMMEDIATELY AFTER** [disk partitioning](#disk-partitioning). Also note that you must set the type of partition to a LUKS partition instead of a standard Linux partition when partitioning with `fdisk`.
    
        
    ---
    
    - I'll **skip** the Arch ISO installation media preparation.
    
    ---
    
    - I'll use a **wired** connection, so no wireless configuration steps will be shown. If you want to connect to wifi, you can either launch `wifi-menu` from the terminal which is a **TGUI** or use [`iwctl`](https://wiki.archlinux.org/title/Iwd#iwctl).
    
## Preliminary Steps  

!!! info "Preliminary Steps"

    First set up your keyboard layout.
    
    ```Zsh
    List all the available keyboard maps and filter them through grep, in this case i am looking for an italian keyboard, which usually starts with "it", for english filter with "en"
    ls /usr/share/kbd/keymaps/**/*.map.gz | grep it
    
    If you prefer you can scroll the whole list like this:
    ls /usr/share/kbd/keymaps/**/*.map.gz | less
    
    Or like this:
    localectl list-keymaps
    
    Now get the name without the path and the extension ( localectl returns just the name ) and load the layout. In my case it is simply "it"
    loadkeys it
    ```
    
    ---
    
    Check that we are in UEFI mode:
    
    ```Zsh
    If this command prints 64 or 32 then you are in UEFI
    cat /sys/firmware/efi/fw_platform_size
    ```
    
    ---
    
    Check the internet connection:
    
    ```Zsh
    ping -c 5 archlinux.org
    ```
    
    ---
    
    Check the system clock:
    
    ```Zsh
    Check if ntp is active and if the time is right:
    timedatectl
    
    In case it's not active you can do
    timedatectl set-ntp true
    
    Or this:
    systemctl enable systemd-timesyncd.service
    ```
    
## Main Installation

## Disk Partitioning

I will make 2 partitions: 

| Number | Type | Size |
| --- | --- | --- |
| 1 | EFI | 512 Mb |
| 2 | Linux Filesystem | 99.5Gb (all of the remaining space ) |

??? example "Disk Partitioning"

    ```Zsh
    Check the drive name. Mine is /dev/nvme0n1
    If you have an hdd is something like sdax
    fdisk -l
    
    Now you can either go and partition your disk with fdisk and follow the steps below, or if you
    want to do things yourself and make it easier, use cfdisk ( an fdisk TUI wrapper ) which is
    much more user friendly. A reddit user suggested me this and it's indeed very intuitive to use.
    
    If you choose cfdisk you will have to invoke it the same way as I did with fdisk below, but you
    don't need to follow my commands blindly as with fdisk below, just navigate the UI with the
    arrows and press enter to get inside menus, remember to write changes before quitting.
    
    Invoke fdisk to partition
    fdisk /dev/nvme0n1
    
    Now press the following commands, when i write ENTER press enter
    g
    ENTER
    n
    ENTER
    ENTER
    ENTER
    +512M
    ENTER
    t
    ENTER
    ENTER
    1
    ENTER
    n
    ENTER
    ENTER
    ENTER # If you don't want to use all the space then select the size by writing +XG (eg: to make a
    10GB partition +10G)
    p
    ENTER # Now check if you got the partitions right
    
    If so write the changes
    w
    ENTER
    
    If not you can quit without saving and redo from the beginning
    q
    ENTER
    ```
    
## Disk Formatting  

!!! quote "Disk Formatting"

    For the file system I've chosen [**BTRFS**](https://wiki.archlinux.org/title/Btrfs) which has evolved quite a lot in the recent years. It is most known for its **Copy on Write** feature which enables it to make system snapshots in a blink of a an eye and to save a lot of disk space, which can be even saved to a greater extent by enabling built-in **compression**. Also it lets the user create **subvolumes** which can be individually snapshotted.
    
    ```Zsh
    Find the efi partition with fdisk -l or lsblk. For me it's /dev/nvme0n1p1 and format it.
    mkfs.fat -F 32 /dev/nvme0n1p1
    
    Find the root partition. For me it's /dev/nvme0n1p2 and format it. I will use BTRFS.
    mkfs.btrfs /dev/nvme0n1p2
    
    Mount the root fs to make it accessible
    mount /dev/nvme0n1p2 /mnt
    ```
    
## Disk Mounting

!!! quote "Disk Mounting"

    I will lay down the subvolumes on a **flat** layout, which is overall superior in my opinion and less constrained than a **nested** one. What's the difference ? If you're interested [this section of the old sysadmin guide](https://archive.kernel.org/oldwiki/btrfs.wiki.kernel.org/index.php/SysadminGuide.html#Layout) explains it.
    
    ```Zsh
    Create the subvolumes, in my case I choose to make a subvolume for / and one for /home.
    Subvolumes are identified by prepending @
    
    NOTICE: the list of subvolumes will be increased in a later release of this guide, upon proper
    testing and judgement. See the "Things to add" chapter.
    btrfs subvolume create /mnt/@
    btrfs subvolume create /mnt/@home
    ```
    
    ---
    
    
    ### Unmount the root fs
    
    ```zsh
    umount /mnt
    ```
    
    For this guide I'll compress the btrfs subvolumes with **Zstd**, which has proven to be [a good algorithm among the choices](https://www.phoronix.com/review/btrfs-zstd-compress)
    
    ```Zsh
    Mount the root and home subvolume. If you don't want compression just remove the compress option.
    mount -o compress=zstd,subvol=@ /dev/nvme0n1p2 /mnt
    mkdir -p /mnt/home
    mount -o compress=zstd,subvol=@home /dev/nvme0n1p2 /mnt/home
    ```
    
!!! quote "Mount the efi partition"

    Now we have to mount the efi partition. In general there are 2 main mountpoints to use: `/efi` or `/boot` but in this configuration i am **forced** to use `/efi`, because by choosing `/boot` we could experience a **system crash** when trying to restore `@` (the root subvolume) to a previous state after kernel updates. This happens because `/boot` files such as the kernel won't reside on `@` but on the efi partition and hence they can't be saved when snapshotting `@`. Also this choice grants separation of concerns and also is good if one wants to encrypt `/boot`, since you can't encrypt efi files. Learn more [here](https://wiki.archlinux.org/title/EFI_system_partition#Typical_mount_points)
    
    ```Zsh
    mkdir -p /mnt/efi
    mount /dev/nvme0n1p1 /mnt/efi
    ```
    
## Packages Installation  

??? quote "Packages Installation"

    ```Zsh
    - This will install some packages to "bootstrap" metaphorically your system.
    - Feel free to add the ones you want.
    - "base, linux, linux-firmware" are needed. If you want a more stable kernel, then swap linux
      with linux-lts.
    - "base-devel" base development packages.
    - "git" to install the git vcs.
    - "btrfs-progs" are user-space utilities for file system management. (It's needed to harness the
      potential of btrfs).
    - "grub" the bootloader.
    - "efibootmgr" needed to install grub.
    - "grub-btrfs" adds btrfs support for the grub bootloader and enables the user to directly boot
      from snapshots.
    - "inotify-tools" used by grub btrfsd deamon to automatically spot new snapshots and update grub
      entries.
    - "timeshift" a GUI app to easily create,plan and restore snapshots using BTRFS capabilities.
    - "amd-ucode" microcode updates for the cpu. If you have an intel one use "intel-ucode".
    - "vim" my goto editor, if unfamiliar use nano.
    - "networkmanager" to manage Internet connections both wired and wireless (it also has an applet
      package network-manager-applet).
    - "pipewire pipewire-alsa pipewire-pulse pipewire-jack" for the new audio framework replacing
      pulse and jack.
    - "wireplumber" the pipewire session manager.
    - "reflector" to manage mirrors for pacman.
    - "zsh" my favourite shell.
    - "zsh-completions" for zsh additional completions.
    - "zsh-autosuggestions" very useful, it helps writing commands [Needs configuration in .zshrc].
    - "openssh" to use ssh and manage keys.
    - "man" for manual pages.
    - "sudo" to run commands as other users.
    
    pacstrap -K /mnt base base-devel linux linux-firmware git btrfs-progs grub efibootmgr grub-btrfs
    inotify-tools timeshift vim networkmanager pipewire pipewire-alsa pipewire-pulse pipewire-jack
    wireplumber reflector zsh zsh-completions zsh-autosuggestions openssh man sudo
    ```
    
## Fstab

!!! quote "Fstab"

    ```Zsh
    Fetch the disk mounting points as they are now (we mounted everything before) & generate
    instructions to let the system know how to mount the various disks automatically genfstab
    -U /mnt >> /mnt/etc/fstab
    
    Check if fstab is fine (it is if you've faithfully followed the previous steps) cat /mnt/etc/
    fstab
    ```
    
## Context Switch To Our New System

!!! abstract "Context Switch To Our New System"

    ```Zsh
    To access our new system we chroot into it
    arch-chroot /mnt
    ```
    
## Set Up The Time Zone

!!! info "Set Up The Time Zone"

    ```Zsh
    In our new system we have to set up the local time zone, find your one in /usr/share/zoneinfo mine is /usr/share/zoneinfo/Europe/Rome and create a symbolic link to /etc/localtime ln -sf /usr/share/zoneinfo/Europe/Rome /etc/localtime
    
    Now sync the system time to the hardware clock
    hwclock --systohc
    ```
    
## Set Up The Language and tty Keyboard Map

!!! tip "Set Up The Language and tty Keyboard Map"

    Edit `/etc/locale.gen` and uncomment the entries for your locales. Each entry represent a language and its formats for time, date, currency and other country related settings. By uncommenting we will mark the entry to be generated when the generate command will be issued, but note that it won't still be active. In my case I will uncomment ( ie: remove the # ) `en_US.UTF-8 UTF-8` and `it_IT.UTF-8 UTF-8` because I use English as a display language and Italian for date, time and other formats.
    
    ```Zsh
    To edit I will use vim, feel free to use nano instead.
    vim /etc/locale.gen
    
    Now issue the generation of the locales
    locale-gen
    ```
    
    ---
    
    Since the locale is generated but still not active, we will create the configuration file `/etc/locale.conf` and set the locale to the desired one, by setting the `LANG` variable accordingly. In my case I'll write `LANG=it_IT.UTF-8` to apply Italian settings to everything and then override only the display language to English by setting (on a new line) `LC_MESSAGES=en_US.UTF-8`. (if you want formats and language to stay the same **DON'T** set `LC_MESSAGES`). More on this [here](https://wiki.archlinux.org/title/Locale#Variables)
    
    ```Zsh
    touch /etc/locale.conf
    vim /etc/locale.conf
    ```
    
    ---
    
    Now to make the current keyboard layout permanent for tty sessions , create `/etc/vconsole.conf` and write `KEYMAP=your_key_map` substituting the keymap with the one previously set [here](#preliminary-steps). In my case `KEYMAP=it`
    
    ```Zsh
    vim /etc/vconsole.conf
    ```
    
## Hostname and Host Configuration

!!! example "Hostname and Host Configuration"

    ```Zsh
    Create /etc/hostname then choose and write the name of your pc in the first line. In my case I'll use Arch.
    touch /etc/hostname
    vim /etc/hostname
    
    Create the /etc/hosts file. This is very important because it will resolve the listed hostnames locally and not over Internet DNS.
    touch /etc/hosts
    ```
    
    ---
    
    Write the following ip, hostname pairs inside /etc/hosts, replacing `Arch` with **YOUR** hostname:
    
    ```
    127.0.0.1 localhost
    ::1 localhost
    127.0.1.1 Arch
    ```
    
    ---
    
    ```Zsh
    Edit the file with the information above
    vim /etc/hosts
    ```
    
## Root and Users

!!! quote "Root and Users"

    ```Zsh
    Set up the root password
    passwd
    
    Add a new user, in my case mjkstra.
    -m creates the home dir automatically
    -G adds the user to an initial list of groups, in this case wheel, the administration group. If you are on a Virtualbox VM and would like to enable shared folders between host and guest machine, then also add the group vboxsf besides wheel.
    ```
    
    **useradd -mG wheel mjkstra**
    **passwd mjkstra**
    
    ```Zsh
    The command below is a one line command that will open the /etc/sudoers file with your favourite editor.
    You can choose a different editor than vim by changing the EDITOR variable
    Once opened, you have to look for a line which says something like "Uncomment to let members of group wheel execute any action"
    And uncomment exactly the line BELOW it, by removing the #. This will grant superuser priviledges to your user.
    Why are we issuing this command instead of a simple vim /etc/sudoers ?
    Because visudo does more than opening the editor, for example it locks the file from being edited simultaneously and
    runs syntax checks to avoid committing an unreadable file.
    EDITOR=vim visudo
    ```
    
## Grub Configuration

!!! quote "Grub Configuration"

    Now I'll [deploy grub](https://wiki.archlinux.org/title/GRUB#Installation)
    
    ```Zsh
    grub-install --target=x86_64-efi --efi-directory=/efi --bootloader-id=GRUB
    ```
    
    ---
    
    
    *Generate the grub configuration (it will include the microcode installed with pacstrap earlier)*
    
    ```Zsh
    grub-mkconfig -o /boot/grub/grub.cfg
    ```
    
## Unmount Everything and Reboot

!!! info "Unmount Everything and Reboot"

    ```Zsh
    Enable newtork manager before rebooting otherwise, you won't be able to connect
    systemctl enable NetworkManager
    
    Exit from chroot
    exit
    
    Unmount everything to check if the drive is busy
    umount -R /mnt
    
    Reboot the system and unplug the installation media
    reboot
    
    Now you'll be presented at the terminal. Log in with your user account, for me its "mjkstra".
    
    Enable and start the time synchronization service
    timedatectl set-ntp true
    ```
    
## Automatic Snapshot Boot Entries Update  

!!! example "Automatic Snapshot Boot Entries Update"

    Each time a system snapshot is taken with timeshift, it will be available for boot in the bootloader, however you need to manually regenerate the grub configuration, this can be avoided thanks to `grub-btrfs`, which can automatically update the grub boot entries.
    
    Edit the **`grub-btrfsd`** service and because I will rely on timeshift for snapshotting, I am going to replace `ExecStart=...` with `ExecStart=/usr/bin/grub-btrfsd --syslog --timeshift-auto`. If you don't use timeshift or prefer to manually update the entries then lookup [here](https://github.com/Antynea/grub-btrfs)
    
    ```Zsh
    sudo systemctl edit --full grub-btrfsd
    
    Enable grub-btrfsd service to run on boot
    sudo systemctl enable grub-btrfsd
    ```
    
## Virtualbox Support

!!! warning "Virtualbox Support"

    Follow these steps if you are running Arch on a Virtualbox VM.
    This will enable features such as **clipboard sharing**, **shared folders** and **screen resolution tweaks**
    
    ```zsh
    # Install the guest utils
    sudo pacman -S virtualbox-guest-utils
    
    # Enable this service to automatically load the kernel modules
    sudo systemctl enable --now vboxservice.service
    ```
    
    !!! note ""
        The utils will only work after a reboot is performed.
            
    !!! warning ""
        The utils seem to only work in a graphical environment.

## Aur Helper and Additional Packages Installation  

!!! info "Aur Helper and Additional Packages Installation"

    - To gain access to the arch user repository we need an aur helper, I will choose yay which also works as a pacman wrapper (which means you can use yay instead of pacman). 
    
    - Yay has a CLI, but if you later want to have an aur helper with a GUI you can install [`pamac`](https://gitlab.manjaro.org/applications/pamac) (a Manjaro software, so use at your own risk), **however** note that front\-ends like `pamac` and also any store (KDE discovery, Ubuntu store etc.) are not officially supported and should be avoided, because of the high risk of performing [partial upgrades](https://wiki.archlinux.org/title/System_maintenance#Partial_upgrades_are_unsupported). This is also why later when installing KDE, I will exclude the KDE discovery store from the list of packages.
    
    - To learn more about yay read [here](https://github.com/Jguer/yay#yay)
    
    !!! abstract "NOTE!"
        You can't execute makepkg as root, so you need to log in your main account. For me it's mjkstra.
        
        ```Zsh
        Install yay
        sudo pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd
        yay && makepkg -si
        
        Install "timeshift-autosnap", a configurable pacman hook which automatically makes snapshots before pacman upgrades.
        yay -S timeshift-autosnap
        ```
        
    Learn more about timeshift autosnap [here](https://gitlab.com/gobonja/timeshift-autosnap)
    

## Finalization

!!! example "Finalization"

    ```Zsh
    To complete the main/basic installation reboot the system:
    reboot
    ```
    
    > After these steps you **should** be able to boot on your newly installed Arch Linux, if so congrats!
    
    > The basic installation is complete and you could stop here, but if you want to to have a graphical session, you can continue reading the guide.
    
## Video Drivers

!!! example "Video Drivers"

    In order to have the smoothest experience on a graphical environment, **Gaming included**, we first need to install video drivers. To help you choose which one you want or need, read [this section](https://wiki.archlinux.org/title/Xorg#Driver_installation) of the arch wiki.
    
    > Note: skip this section if you are on a Virtual Machine
    
## Amd  

!!! example "AMD"

    For this guide I'll install the [**AMDGPU** driver](https://wiki.archlinux.org/title/AMDGPU) which is the open source one and the recommended, but be aware that this works starting from the **GCN 3** architecture, which means that cards **before** RX 400 series are not supported. (I have an RX 5700 XT)
    
    ```Zsh
    
    What are we installing?
    mesa: DRI driver for 3D acceleration.
    xf86-video-amdgpu: DDX driver for 2D acceleration in Xorg. I won't install
    this, because I prefer the default kernel modesetting driver.
    vulkan-radeon: vulkan support.
    libva-mesa-driver: VA-API h/w video decoding support.
    mesa-vdpau: VDPAU h/w accelerated video decoding support.
    
    sudo pacman -S mesa vulkan-radeon libva-mesa-driver mesa-vdpau
    ```
    
### 32 Bit Support

!!! danger "32 Bit Support"

    If you want to add **32-bit** support, we need to enable the `multilib` repository on pacman: edit `/etc/pacman.conf` and uncomment the `[multilib]` section  (ie: remove the hashtag from each line of the section. Should be 2 lines). Now we can install the additional packages.
    
    ```Zsh
    Refresh and upgrade the system
    yay
    
    Install 32bit support for mesa, vulkan, VA-API and VDPAU
    ```
    
    ```Zsh
    sudo pacman -S lib32-mesa lib32-vulkan-radeon lib32-libva-mesa-driver lib32-mesa-vdpau
    ```
    
## Nvidia  

!!! warning "Nvidia"

    In summary if you have an Nvidia card you have 2 options:
    
    1. [**NVIDIA** proprietary driver](https://wiki.archlinux.org/title/NVIDIA)
    2. [**Nouveau** open source driver](https://wiki.archlinux.org/title/Nouveau)
    
    The recommended is the proprietary one, however I won't explain further because I don't have an Nvidia card and the process for such cards is tricky unlike for AMD or Intel cards. Moreover for reason said before, I can't even test it.
    
## Intel

!!! tip "Intel"

    Installation looks almost identical to the AMD one, but every time a package contains the `radeon` word substitute it with `intel`. However this does not stand for [h/w accelerated decoding](https://wiki.archlinux.org/title/Hardware_video_acceleration), and to be fair I would recommend reading [the wiki](https://wiki.archlinux.org/title/Intel_graphics#Installation) before doing anything.
    
## Setting Up a Graphical Environment

!!! pied-piper "Setting Up a Graphical Environment"

    I'll provide 2 options and a partial one for Gnome with an Arch wiki link.
    
    1. **KDE-plasma**
    2. **Hyprland**
    3. **Gnome**
    
    ---
    
    - Setting up the GNOME desktop environment involves installing core components via package managers and enabling the GDM display manager, creating a customizable user interface centered on the "Activities" workflow.
    
    - The process generally requires updating the system, installing the gnome group, and enabling the display manager, with detailed steps varying slightly by distribution. 
    
    - For a detailed step-by-step guide on setting up GNOME, you can refer to the Arch Wiki, which is widely considered the standard for in-depth Linux installation instructions:
    
    ---
    
    - On top of that I'll add a **display manager**, which you can omit if you don't like (if so, you have additional configuration steps to perform).
    
    ---
    
    - [Archlinux Wiki for GNOME desktop environment.](https://wiki.archlinux.org/title/GNOME)
    
## Option 1: KDE-plasma

??? tip "Option 1: KDE-plasma"

    **KDE Plasma** is a very popular DE which comes bundled in many distributions. It supports both the older **Xorg** and the newer **Wayland** protocols. It's **user friendly**, **light** and it's also used on the Steam Deck, which makes it great for **gaming**. I'll provide the steps for a minimal installation and add some basic packages.
    
    ```Zsh
    plasma-desktop: the barebones plasma environment.
    plasma-pa: the KDE audio applet.
    plasma-nm: the KDE network applet.
    plasma-systemmonitor: the KDE task manager.
    plasma-firewall: the KDE firewall.
    plasma-browser-integration: cool stuff, it lets you manage things from your browser like media
    currently played via the plasma environment. Make sure to install the related extension on
    firefox (you will be prompted automatically upon boot).
    kscreen: the KDE display configurator.
    kwalletmanager: Manage secure vaults (Needed to store the passwords of local applications in an
    encrypted format). This also installs kwallet as a dependency, so I don't need to specify it.
    kwallet-pam: automatically unlocks secure vault upon login (without this, each time the wallet
    gets queried it asks for your password to unlock it).
    bluedevil: the KDE bluetooth manager.
    powerdevil: the KDE power manager.
    power-profiles-daemon: adds 3 power profiles selectable from powerdevil ( power saving, balanced, performance ). Make sure that its service is enabled and running (it should be).
    kdeplasma-addons: some useful addons.
    xdg-desktop-portal-kde: Integrates the plasma desktop in various windows like file pickers.
    xwaylandvideobridge: exposes Wayland windows to XWayland-using screen sharing apps (useful when
    screen sharing on discord, but also in other instances).
    kde-gtk-config: the native settings integration to manage GTK theming.
    breeze-gtk: the breeze GTK theme.
    cups, print-manager: the CUPS print service and the KDE front-end.
    konsole: the KDE terminal.
    dolphin: the KDE file manager.
    ffmpegthumbs: video thumbnailer for dolphin.
    firefox: the web browser.
    kate: the KDE text editor.
    okular: the KDE pdf viewer.
    gwenview: the KDE image viewer.
    ark: the KDE archive manager.
    pinta: a paint.net clone written in GTK.
    spectacle: the KDE screenshot tool.
    dragon: a simple KDE media player. A more advanced alternative based on libmpv is Haruna.
    ```
    
    ```Zsh
    sudo pacman -S plasma-desktop plasma-pa plasma-nm plasma-systemmonitor plasma-firewall plasma-browser-integration kscreen kwalletmanager kwallet-pam bluedevil powerdevil power-profiles-daemon kdeplasma-addons xdg-desktop-portal-kde xwaylandvideobridge kde-gtk-config breeze-gtk cups print-manager konsole dolphin ffmpegthumbs firefox kate okular gwenview ark pinta spectacle dragon
    ```
    
    Now don't reboot your system yet. If you want a display manager, which is generally recommended, head to the [related section](#adding-a-display-manager) in this guide and proceed from there otherwise you'll have to [manually configure](https://wiki.archlinux.org/title/KDE#From_the_console) and launch the graphical environment each time, which I would advise to avoid.
    

### Option 2: Hyprland [WIP]  

!!! tip "Option 2: Hyprland [WIP]"

    !!! abstract "Note!"
    
        Note: this section needs configuration and is basically empty, I don't know when and if I will expand it but at least you have a starting point.
        
    **Hyprland** is a **tiling WM** that sticks to the wayland protocol. It looks incredible and it's one of the best Wayland WMs right now. It's based on **wlroots** the famous library used by Sway, the most mature Wayland WM there is. I don't know if I would recommend this to beginners because it's a totally different experience and it may not be better. Moreover it requires you to read the [wiki](https://wiki.hyprland.org/) for configuration but it also features a [master tutorial](https://wiki.hyprland.org/Getting-Started/Master-Tutorial). The good part is that even if it seems discouraging, it's actually an easy read because it is written beautifully.
    
    ```Zsh
    Install hyprland from tagged releases and other utils:
    swaylock: the lockscreen
    wofi: the wayland version of rofi, an application launcher, extremely configurable
    waybar: a status bar for wayland wm's
    dolphin: a powerful file manager from KDE applications
    alacritty: a beautiful and minimal terminal application, super configurable
    pacman -S --needed hyprland swaylock wofi waybar dolphin alacritty
    wlogout: a logout/shutdown menu
    
    yay -S wlogout
    ```
    
## Adding a Display Manager

!!! tip "Adding a Display Manager"

    **Display managers** are useful when you have multiple DE or WMs and want to choose where to boot from or select the display protocol (Wayland or Xorg) in a GUI fashion, also they take care of the launch process. I'll show the installation process of **SDDM**, which is highly customizable and compatible.
    
    !!! abstract "Note!"
        Hyprland does not support any display manager, however SDDM is reported to work flawlessly from the [wiki](https://wiki.hyprland.org/Getting-Started/Master-Tutorial/#launching-hyprland)
        
    
    Install SDDM
    
    ```Zsh
    sudo pacman -S sddm
    ```
    
    Enable SDDM service to make it start on boot:
    
    ```Zsh
    sudo systemctl enable sddm
    ```
    
    If using KDE I suggest installing this to control the SDDM configuration from the KDE settings App
    
    ```Zsh
    pacman -S --needed sddm-kcm
    ```
    
    Now it's time to reboot the system:
    
    ```Zsh
    reboot
    ```
    
## Gaming

!!! tip "Gaming"

    Gaming on linux has become a very fluid experience, so I'll give some tips on how to setup your arch distro for gaming.
     
    Before going further I'll assume that you have installed the video drivers, also make sure to install with pacman, if you haven't done it already: `lib32-mesa`, `lib32-vulkan-radeon` and additionally `lib32-pipewire` (Note that the `multilib` repository must be enabled, [here](#32-bit-support) I've explained how to do it).
    
    ---
     
    Let's break down what is needed to game:
     
    1. **Gaming client** (eg: Steam, Lutris, Bottles, etc..)
    2. **Windows compatibility layers** (eg: Proton, Wine, DXVK, VKD3D)
    
    ---
     
    Optionally we can have:
     
    1. **Generic optimization** (eg: gamemode)
    2. **Overclocking and monitoring software** (eg: CoreCtrl, Mangohud)
    3. **Custom kernels**
    
## Gaming Clients

!!! tip "Gaming Clients"

    I'll install **Steam** and to access games from other launchers I'll use **Bottles**, which should be installed through **flatpak**.
    
    Install steam and flatpak:
    
    ```Zsh
    sudo pacman -S steam flatpak
    ```
    
    Install bottles through flatpak"
    
    ```Zsh
    flatpak install flathub com.usebottles.bottles
    ```
    
## Windows Compatibility Layers

!!! tip " Windows Compatibility Layers"

    1. Proton's the compatibility layer developed by Valve, which includes **DXVK** (DirectX 9-10-11 to Vulkan), **VKD3D** (DirectX 12 to Vulkan ) and a custom version of **Wine**. It is embedded in Steam and can be enabled for **non** native games direclty in Steam: `Steam > Settings > Compatibility > Enable Steam Play for all other titles`. 
    
    2. A custom version of proton, **Proton GE** exists and can be used as an alternative if something is broken or doesn't perform as expected. Can be either [downloaded manually](https://github.com/GloriousEggroll/proton-ge-custom#installation) or through yay as below.
    
    Installation through yay: (AUR Helper)
    
    ```Zsh
    yay -S proton-ge-custom-bin
    ```
    
## Generic Optimizations

!!! tip "Generic Optimizations"

    We can use gamemode to gain extra performance. To enable it read [here](https://github.com/FeralInteractive/gamemode#requesting-gamemode)
    
    
    ---
        
    Install gamemode:
    
    ```Zsh
    sudo pacman -S gamemode
    ```
    
## Overclocking and Monitoring

!!! pied-piper "Overclocking and Monitoring"

    To live monitor your in-game performance, you can use **mangohud**. To enable it read [here](https://github.com/flightlessmango/MangoHud#normal-usage).
    
    ---
    
    In order to easily configure mangohud, I'll use **Goverlay**.
    
    Install goverlay which includes mangohud as a dependency:
    
    
    ```Zsh
    sudo pacman -S goverlay
    ```
    
    ---
    
    To overclock your system, I would suggest installing [**corectrl**](https://gitlab.com/corectrl/corectrl) if you have an AMD Gpu or [**TuxClocker**](https://github.com/Lurkki14/tuxclocker) for NVIDIA.
    
## Additional Notes

??? abstract "Additional Notes - Click to open and read."

    - On KDE disabling mouse acceleration is simple, just go to the settings via the GUI and on the mouse section enable the flat acceleration profile. If you're not using KDE, then read [here.](https://wiki.archlinux.org/title/Mouse_acceleration)
    
    - To enable Freesync or Gsync you can read [here](https://wiki.archlinux.org/title/Variable_refresh_rate), depending on your session Wayland or Xorg and your gfx provider Nvidia, AMD, Intel the steps may differ. On a KDE wayland session, you can directly enable it from the monitor settings under the name of **adaptive sync.**
    
    - Some considerations if you are thinking about switching to a custom kernel:
    
    - You have to manually recompile it each time there is a new update unless you use a precompiled kernel from pacman or aur such as `linux-zen.` 
    
    - There is no such thing as the best kernel, all kernels make tradeoffs eg: latency for throughtput and this it why it's generally advised to stick with the generic one.
    
    - If you are mainly a gamer you MAY consider the **TKG** or **CachyOS** kernel. These kernels contain many optimizations and are highly customizable, however the TKG Kernel has to be compiled Mainly it's time consuming, not difficult, while the \( CachyOS\) \(Kernel\) comes already packaged and optimized for specific hardware configurations, and can be simply installed with pacman upon adding their repos to `pacman.conf.`
    
    - Some users have reported to have experienced a smoother experience with lower latency, however I couldn't find consistent information about this and it seems that is all backed by a personal sensation and not a result obtained through objective measurements.  Also this is difficult because in Linux there are countless configuration variables and it also depends on the graphic card/s being used.
    
### Some Recommended Reads:

<div class="grid cards cols-3" markdown>

-   <span style="color: #607d8b">:material-linux:</span> **KDE Environment**
    [:octicons-arrow-right-24: Build Guide](https://kde.org/search/?s=Environment){ .md-button style="border-color: #607d8b; color: #607d8b" }

    Official packaging recommendations for building your KDE environment.

-   <span style="color: #89b4fa">:material-controller:</span> **Gaming on Wayland**
    [:octicons-arrow-right-24: Read Article](https://wiki.archlinux.org/title/Wayland){ .md-button style="border-color: #89b4fa; color: #89b4fa" }

    An insightful (though older) look at the state of gaming on Wayland.

-   <span style="color: #009688">:material-speedometer:</span> **Gaming Performance**
    [:octicons-arrow-right-24: Improve FPS](https://linux-gaming.kwindu.eu/index.php/Main_Page){ .md-button style="border-color: #009688; color: #009688" }

    Tips and tweaks for squeezing more performance out of Linux gaming.

-   <span style="color: #607d8b">:octicons-tools-24:</span> **System Maintenance**
    [:octicons-arrow-right-24: View Wiki](https://wiki.archlinux.org/title/System_maintenance){ .md-button style="border-color: #607d8b; color: #607d8b" }

    Essential Arch Linux guide for keeping your system clean and stable.

-   <span style="color: #89b4fa">:octicons-light-bulb-24:</span> **Gen. Recommendations**
    [:octicons-arrow-right-24: View Wiki](https://wiki.archlinux.org/title/General_recommendations){ .md-button style="border-color: #89b4fa; color: #89b4fa" }

    The post-installation "must-read" for Arch Linux users.

-   <span style="color: #009688">:material-gnome:</span> **GNOME Desktop**
    [:octicons-arrow-right-24: View Wiki](https://wiki.archlinux.org/title/GNOME){ .md-button style="border-color: #009688; color: #009688" }

    Comprehensive docs for the GNOME desktop environment on Arch.

</div>

### Things To Add

!!! abstract "Development Roadmap"

    - [x] **Pacman Optimization**: Enable `paccache`, colors, and parallel downloads.
    - [x] **Mirror Management**: Configure `reflector` for faster updates.
    - [x] **Advanced Snapshots**: Integrate `Snapper` as a Timeshift alternative.
    - [x] **BTRFS Overhaul**: Refine subvolumes (`@log`, `@cache`, `@tmp`, `@snapshots`).
    - [x] **System Stability**: Implement a more robust `fstab` structure.

---

<div class="grid cards cols-3" markdown>

-   <span style="color: #607d8b">:material-pac-man:</span> **Pacman Tweaks**
    [:octicons-link-external-24: View Wiki](https://wiki.archlinux.org/title/Pacman/Tips_and_tricks){ .md-button style="border-color: #607d8b; color: #607d8b" }

    Enable colors, ILoveCandy, and parallel downloads.

-   <span style="color: #89b4fa">:material-archive-eye-outline:</span> **Cache Cleanup**
    [:octicons-link-external-24: View Wiki](https://wiki.archlinux.org/title/Pacman#Cleaning_the_package_cache){ .md-button style="border-color: #89b4fa; color: #89b4fa" }

    Automate `paccache` to prevent disk bloat.

-   <span style="color: #009688">:material-mirror:</span> **Reflector**
    [:octicons-link-external-24: View Wiki](https://wiki.archlinux.org/title/Reflector){ .md-button style="border-color: #009688; color: #009688" }

    Automating mirrorlist updates for top speeds.

-   <span style="color: #607d8b">:material-camera-retake:</span> **Snapper**
    [:octicons-link-external-24: View Wiki](https://wiki.archlinux.org/title/Snapper){ .md-button style="border-color: #607d8b; color: #607d8b" }

    Adv BTRFS snapshot man. and boot integration.

-   <span style="color: #89b4fa">:material-harddisk:</span> **BTRFS Overhaul**
    [:octicons-link-external-24: View Wiki](https://btrfs.readthedocs.io/en/latest/){ .md-button style="border-color: #89b4fa; color: #89b4fa" }

    Refining subvolumes for `@log`, `@cache`, and `@tmp`.

-   <span style="color: #009688">:material-file-cog:</span> **Fstab Structure**
    [:octicons-link-external-24: View Wiki](https://wiki.archlinux.org/title/Fstab){ .md-button style="border-color: #009688; color: #009688" }

    Implementing a cleaner, more robust mount structure.

</div>


### Additional Packages (optional)

!!! abstract "Note!"

    The target of the respective URL is also the recommended way to install the package.
    
<div class="grid cards cols-3" markdown>

-   <span style="color: #2094f3">:material-cog:</span> **Sys & Maintenance**
    { .md-button .md-button--primary style="border-color: #2094f3; color: #2094f3; background-color: transparent;" }

    * [Extension Manager](https://flathub.org/en-GB/apps/com.mattjakeman.ExtensionManager)
    * [Flatseal](https://flathub.org/en-GB/apps/com.github.tchx84.Flatseal)
    * [Warehouse](https://flathub.org/en-GB/apps/io.github.flattool.Warehouse)
    * [GNOME Tweaks](https://archlinux.org/packages/extra/any/gnome-tweaks/)
    * [Refine](https://flathub.org/en-GB/apps/page.tesk.Refine)
    * [GDM Settings](https://flathub.org/en-GB/apps/io.github.realmazharhussain.GdmSettings)
    * [GNOME Firmware](https://archlinux.org/packages/extra/x86_64/gnome-firmware/)
    * [Ignition](https://flathub.org/en-GB/apps/io.github.flattool.Ignition)
    * [Preload](https://wiki.archlinux.org/title/Preload)
    * [Mutter Performance](https://aur.archlinux.org/packages/mutter-performance)

-   <span style="color: #4caf50">:material-folder-zip:</span> **Files & Productivity**
    { .md-button .md-button--primary style="border-color: #4caf50; color: #4caf50; background-color: transparent;" }

    * [Pika Backup](https://flathub.org/en-GB/apps/org.gnome.World.PikaBackup)
    * [LocalSend](https://flathub.org/en-GB/apps/org.localsend.localsend_app)
    * [File Roller](https://archlinux.org/packages/extra/x86_64/file-roller/)
    * [Papers](https://flathub.org/en/apps/org.gnome.Papers)
    * [Webapp Manager](https://aur.archlinux.org/packages/webapp-manager)
    * [Ferdium](https://flathub.org/en-GB/apps/org.ferdium.Ferdium)
    * [Alpaca (AI)](https://flathub.org/en-GB/apps/com.jeffser.Alpaca)
    * [Seahorse](https://archlinux.org/packages/extra/x86_64/seahorse/)
    * [Dconf Editor](https://archlinux.org/packages/extra/x86_64/dconf-editor/)
    * [Downgrade](https://aur.archlinux.org/packages/downgrade)

-   <span style="color: #ff9800">:material-palette:</span> **Media & Interface**
    { .md-button .md-button--primary style="border-color: #ff9800; color: #ff9800; background-color: transparent;" }

    * [EasyEffects](https://flathub.org/en-GB/apps/com.github.wwmm.easyeffects)
    * [NoiseTorch](https://aur.archlinux.org/packages/noisetorch)
    * [Amberol](https://archlinux.org/packages/extra/x86_64/amberol/) / [Gapless](https://flathub.org/en-GB/apps/com.github.neithern.g4music)
    * [Parabolic](https://flathub.org/en-GB/apps/org.nickvision.tubeconverter)
    * [Mission Center](https://flathub.org/en-GB/apps/io.missioncenter.MissionCenter)
    * [Monitorets](https://flathub.org/en-GB/apps/io.github.jorchube.monitorets)
    * [AddWater (Firefox)](https://flathub.org/en-GB/apps/dev.qwery.AddWater)
    * [Folder Color](https://aur.archlinux.org/packages/folder-color-switcher)
    * [MenuLibre](https://aur.archlinux.org/packages/Menulibre?O=100)

</div>

### GNOME Extensions (optional)

<div class="grid cards cols-3" markdown>

-   <span style="color: #2094f3">:material-palette-outline:</span> **UI & Visuals**
    { .md-button .md-button--primary style="border-color: #2094f3; color: #2094f3; background-color: transparent;" }

    * [Just Perfection](https://extensions.gnome.org/extension/3843/just-perfection/)
    * [Blur My Shell](https://extensions.gnome.org/extension/3193/blur-my-shell/)
    * [Open Bar](https://extensions.gnome.org/extension/6580/open-bar/)
    * [Weather O'Clock](https://extensions.gnome.org/extension/5470/weather-oclock/)
    * [App Hider](https://extensions.gnome.org/extension/5895/app-hider/)
    * [Lilypad](https://extensions.gnome.org/extension/7266/lilypad/)

-   <span style="color: #4caf50">:material-window-maximize:</span> **Workflow & Dock**
    { .md-button .md-button--primary style="border-color: #4caf50; color: #4caf50; background-color: transparent;" }

    * [Dash to Panel](https://extensions.gnome.org/extension/1160/dash-to-panel/)
    * [Dash to Dock](https://extensions.gnome.org/extension/307/dash-to-dock/)
    * [Tiling Assistant](https://extensions.gnome.org/extension/3733/tiling-assistant/)
    * [Hide Minimized](https://extensions.gnome.org/extension/2639/hide-minimized/)
    * [Happy Appy Hotkey](https://extensions.gnome.org/extension/6057/happy-appy-hotkey/)
    * [Fullscreen Workspace](https://extensions.gnome.org/extension/7559/fullscreen-to-empty-workspace/)

-   <span style="color: #ff9800">:material-pulse:</span> **System & Utils**
    { .md-button .md-button--primary style="border-color: #ff9800; color: #ff9800; background-color: transparent;" }

    * [Arch Update Indicator](https://extensions.gnome.org/extension/1010/archlinux-updates-indicator/)
    * [AppIndicator Support](https://extensions.gnome.org/extension/615/appindicator-support/)
    * [Caffeine](https://extensions.gnome.org/extension/517/caffeine/)
    * [Vitals](https://extensions.gnome.org/extension/1460/vitals/)
    * [System Monitor](https://extensions.gnome.org/extension/3010/system-monitor-next/)
    * [Window Calls](https://extensions.gnome.org/extension/4724/window-calls/)

</div>

### Office Support

<div class="grid cards cols-3" markdown>

-   <span style="color: #4caf50">:material-office-building:</span> **LibreOffice**
    [:octicons-arrow-right-24: View Package](https://archlinux.org/packages/extra/x86_64/libreoffice-fresh/){ .md-button style="border-color: #4caf50; color: #4caf50" }

    The standard powerful, free, and open-source office suite.

-   <span style="color: #ff9800">:material-file-document-edit:</span> **OnlyOffice**
    [:octicons-arrow-right-24: View Flatpak](https://flathub.org/apps/org.onlyoffice.desktopeditors){ .md-button style="border-color: #ff9800; color: #ff9800" }

    High-compatibility Office Suite works with MS Office formats.

-   <span style="color: #2196f3">:material-brush:</span> **Drawing & SVG**
    [:octicons-arrow-right-24: View Drawing](https://flathub.org/apps/com.github.maoschanz.drawing){ .md-button style="border-color: #2196f3; color: #2196f3" }

    Tools for image editing and vector graphics with BoxySVG.

</div>


### Realtime Streaming to other PC, TV or Smart Device

<div class="grid cards cols-3" markdown>

-   <span style="color: #ffc107">:octicons-broadcast-24:</span> **Sunshine & Moonlight**
    [:octicons-arrow-right-24: View Sunshine](https://docs.lizardbyte.dev){ .md-button style="border-color: #ffc107; color: #ffc107" }

    Low-latency self-hosted game streaming server and client.

-   <span style="color: #5865f2">:octicons-hash-24:</span> **Vesktop**
    [:octicons-arrow-right-24: View Flatpak](https://flathub.org/en-GB/apps/dev.vencord.Vesktop){ .md-button style="border-color: #5865f2; color: #5865f2" }

    Enhanced DC client with native Wayland screen sharing.

-   <span style="color: #4caf50">:material-controller:</span> **RetroDECK**
    [:octicons-arrow-right-24: View Docs](https://retrodeck.readthedocs.io){ .md-button style="border-color: #4caf50; color: #4caf50" }

    All-in-one manager for your entire retro gaming collection.

</div>

### Install Sunshine (Streaming Server)

!!! info "Sunshine Installation (Streaming Server)"

    1. Add the [LizardByte Repository](https://github.com) to your config: `sudo nano /etc/pacman.conf`
    
    ```ini
    [lizardbyte]
    SigLevel = Optional
    Server = https://github.com/releases/latest/download
    ```

    2. Install Sunshine: `sudo pacman -Syyu lizardbyte/sunshine`
    3. Start the application and access the Web Interface at [https://localhost:47990](https://localhost:47990) to set your credentials.


### For Developers

<div class="grid cards cols-3" markdown>

-   <span style="color: #607d8b">:material-package-variant:</span> **Distrobox & Toolbox**
    [:octicons-arrow-right-24: View Distrobox](https://distrobox.it/){ .md-button style="border-color: #607d8b; color: #607d8b" }

    Run any Linux distribution inside your terminal with ease.

-   <span style="color: #89b4fa">:material-docker:</span> **Container Runtimes**
    [:octicons-arrow-right-24: View Podman](https://podman.io){ .md-button style="border-color: #89b4fa; color: #89b4fa" }

    Industry standard runtimes including Podman and Docker.

-   <span style="color: #009688">:material-cube-outline:</span> **Virtualization & UI**
    [:octicons-arrow-right-24: View Boxes](https://archlinux.org/packages/extra/x86_64/gnome-boxes/){ .md-button style="border-color: #009688; color: #009688" }

    [Boxes](https://apps.gnome.org/Boxes), [Podman](https://podman-desktop.io/), [BoxBuddyRS](https://github.com/Dvlv/BoxBuddyRS) VM/Container management.

</div>
