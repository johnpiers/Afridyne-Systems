---
icon: material/arch
created: 2025-01-15 10:30:00
---

<h1 align="center">
  <img src="https://github.com/murkl/arch-os/raw/main/docs/logo.svg" width="150" height="150">
  <br>
  Arch OS
</h1>

<div align="center">

<p><strong>Boot from latest <a target="_blank" href="https://github.com/murkl/arch-os/releases/latest">Arch OS ISO</a> to launch the Installer automatically.</strong></p>

 <p>Alternatively boot from official <a target="_blank" href="https://archlinux.org/download/">Arch Linux ISO</a> and run</p>

<code><b>curl -Ls bit.ly/arch-os | bash</b></code>

<p><b>

<b><a about="_blank" href="https://github.com/murkl/arch-os?tab=readme-ov-file#arch-os-installation">➜ Step by Step Installation Guide</a></b>
<br></b></p>

<p><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/installer.png"></p>

<b><a about="_blank" href="https://github.com/murkl/arch-os/blob/main/docs/DOCS.md">➜ More Screenshots</a></b>

<h2 style="text-align:center;">More Information</h2>

<p>
  <img src="https://img.shields.io/badge/MAINTAINED-YES-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-GPL_v2-blue?style=for-the-badge">
</p>

<b><a about="_blank" href="https://github.com/murkl/arch-os/blob/main/docs/DOCS.md">➜ Arch OS Documentation</a></b>
<br>
<b><a about="_blank" href="https://t.me/archos_community">➜ t.me/archos_community</a></b>

<h5 style="text-align: center;">
  <a href="https://www.shellcheck.net/">100% shellcheck approved</a>
</h5>

</div>

!!! ex "Optimised for Gaming, Emulation, Audio & Development"

    - This project aims to provide a mostly automated, minimal and robust Arch Linux base (minimal tty core or desktop), along with an easy-to-use and fast properties-file-based installer with error handling. 
    
    - Install a minimal Arch Linux core with optional features such as GNOME Desktop with Graphics Driver, Automatic Housekeeping, Zen Kernel, Fancy Shell Enhancement, pre-installed Paru as AUR Helper, enabled MultiLib, Bootsplash, System Manager and some more...
    
### Core Features

<div class="grid cards cols-3" markdown>

-   <span style="color: #2094f3">:material-thumb-up:</span> **Minimal Arch Linux**
    [:octicons-arrow-right-24: View Minimal-Installation](DOCS.md#minimal-installation){ .md-button style="border-color: #2094f3; color: #2094f3" }

    Minimal Arch Linux Minimal-installation) (~150 packages).

-   <span style="color: #2094f3">:material-cog-sync:</span> **Zen Kernel Installation**
    [:octicons-arrow-right-24: View Advanced-Installation](DOCS.md#advanced-installation){ .md-button style="border-color: #2094f3; color: #2094f3" }

    Zen Kernel Advanced-Installation) (Configurable).

-   <span style="color: #2094f3">:material-star-circle:</span> **Swap-zram-generator**
    [:octicons-arrow-right-24: View Enhanced config](DOCS.md#swap){ .md-button style="border-color: #2094f3; color: #2094f3" }

    Swap with zram-generator (zstd). Swap Enhanced config.

-   <span style="color: #4caf50">:material-information-outline:</span> **Sole OS Partitions**
    [:octicons-arrow-right-24: View: Sole OS-Layout](DOCS.md#partitions-layout){ .md-button style="border-color: #4caf50; color: #4caf50" }

     The partition layout is seperated in two partitions.

-   <span style="color: #4caf50">:material-information-outline:</span> **BTRFS Snapshot**
    [:octicons-arrow-right-24: View Managing Snapshots](DOCS.md/#btrfs){ .md-button style="border-color: #4caf50; color: #4caf50" }

    BTRFS Snapshot Support (Snapper, OverlayFS)

-   <span style="color: #4caf50">:material-information-outline:</span> **All-in-One password**
    [:octicons-arrow-right-24: View Passwords/Security](https://wiki.archlinux.org/title/Users_and_groups){ .md-button style="border-color: #4caf50; color: #4caf50" }

     All-in-One password (encryption, root & user)

-   <span style="color: #ff9800">:material-xml:</span> **Multilingual Support**
    [:octicons-arrow-right-24: View Multilingual Support](https://wiki.archlinux.org/title/Localization){ .md-button style="border-color: #ff9800; color: #ff9800" }

    Localization (l10n) and internationalization (i18n).

-   <span style="color: #ff9800">:material-heart:</span> **Filesystem Support**
    [:octicons-arrow-right-24: View Filesystem btrfs/ext4](https://wiki.archlinux.org/title/File_systems){ .md-button style="border-color: #ff9800; color: #ff9800" }

    Filesystem support for [btrfs](https://wiki.archlinux.org/title/Btrfs) or [ext4](https://wiki.archlinux.org/title/Ext4) support.

-   <span style="color: #ff9800">:material-heart:</span> **Bootloader Systemd**
    [:octicons-arrow-right-24: View Bootloader systemd](https://wiki.archlinux.org/title/Systemd){ .md-button style="border-color: #ff9800; color: #ff9800" }

    Bootloader: [grub](https://wiki.archlinux.org/title/GRUB) or [systemd](https://wiki.archlinux.org/title/Systemd-boot) (auto updated)

-   <span style="color: #9c27b0">:material-lifebuoy:</span> **Silent Boot**
    [:octicons-arrow-right-24: View Silent Boot](https://wiki.archlinux.org/title/Silent_boot){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    Silent Boot (optional) configuration.

-   <span style="color: #9c27b0">:material-memory:</span> **Systemd OOM**
    [:octicons-arrow-right-24: View OOM Killer](https://wiki.archlinux.org/title/Improving_performance){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    Systemd OOM (out-of-memory killer) setup.

-   <span style="color: #9c27b0">:material-download:</span> **Pacman Tweaks**
    [:octicons-arrow-right-24: View Pacman](https://wiki.archlinux.org/title/Pacman){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    Pacman parallel downloads & [eyecandy](https://wiki.archlinux.org/title/Category:Eye_candy) (optional).

-   <span style="color: #00bcd4">:material-lan:</span> **Network Manager**
    [:octicons-arrow-right-24: View Networking](https://wiki.archlinux.org/title/NetworkManager){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    Network Manager configuration.

-   <span style="color: #00bcd4">:material-harddisk:</span> **SSD Support**
    [:octicons-arrow-right-24: View SSD Trim](https://wiki.archlinux.org/title/Solid_state_drive){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    SSD Support (fstrim) optimization.

-   <span style="color: #00bcd4">:lucide-cpu:</span> **Microcode Support**
    [:octicons-arrow-right-24: View Microcode](https://wiki.archlinux.org/title/Microcode){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    Microcode Support (Intel & AMD).

-   <span style="color: #4caf50">:material-shield-alert:</span> **Disabled Watchdog**
    [:octicons-arrow-right-24: View Watchdog](https://wiki.archlinux.org/title/Power_management#:~:text=Disabling%20NMI-,watchdog,-%5Bedit%20source){ .md-button style="border-color: #4caf50; color: #4caf50" }

    Disabled Watchdog (optional) power management.

-   <span style="color: #4caf50">:material-check-circle-outline:</span> **UEFI Support**
    [:octicons-arrow-right-24: View UEFI](DOCS.md){ .md-button style="border-color: #4caf50; color: #4caf50" }

    UEFI only supported (V).

-   <span style="color: #4caf50">:material-information-outline:</span> **More Info**
    [:octicons-arrow-right-24: View Details](DOCS.md#technical-information){ .md-button style="border-color: #4caf50; color: #4caf50" }

    [More Information...](DOCS.md#technical-information) about the system specs.


</div>

---

### Desktop Features

<div class="grid cards cols-3" markdown>

-   <span style="color: #9c27b0">:material-monitor:</span> **GNOME Desktop**
    [:octicons-arrow-right-24: View Recommendation](DOCS.md#recommendation){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    [GNOME Desktop Environment](DOCS.md#recommendation) (optional with additional packages)

-   <span style="color: #9c27b0">:material-layers-outline:</span> **Arch OS Slim**
    [:octicons-arrow-right-24: View Installer Config](DOCS.md#example-installerconf){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    [Arch OS Slim Version](DOCS.md#example-installerconf) (GNOME Core Apps only)

-   <span style="color: #9c27b0">:material-video-input-component:</span> **Graphics Drivers**
    [:octicons-arrow-right-24: View Drivers](DOCS.md#install-graphics-driver-manually){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    [Graphics Driver](DOCS.md#install-graphics-driver-manually) (Mesa, Intel i915, NVIDIA, AMD, ATI)

-   <span style="color: #00bcd4">:material-volume-high:</span> **Pipewire Audio**
    [:octicons-arrow-right-24: View Audio Setup](DOCS.md#for-audiophiles){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    [Pipewire Audio](DOCS.md#for-audiophiles) (Dolby Atmos supported)

-   <span style="color: #00bcd4">:material-package-variant-closed:</span> **Flatpak Packages**
    [:octicons-arrow-right-24: View Flatpak](https://archlinux.org){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    Flatpak Support + Auto Update (GNOME Software)

-   <span style="color: #00bcd4">:material-folder-network:</span> **Samba & Protocols**
    [:octicons-arrow-right-24: View Samba](https://archlinux.org){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    Samba, Networking Protocol Libs, Git, Utils & Codecs included

-   <span style="color: #4caf50">:material-battery-charging:</span> **Power Profiles**
    [:octicons-arrow-right-24: View Power](https://archlinux.org){ .md-button style="border-color: #4caf50; color: #4caf50" }

    GNOME Power Profiles Support (tuned-ppd)

-   <span style="color: #4caf50">:material-lock-open-outline:</span> **VPN Support**
    [:octicons-arrow-right-24: View VPN](https://archlinux.org){ .md-button style="border-color: #4caf50; color: #4caf50" }

    VPN Support configuration

-   <span style="color: #4caf50">:octicons-typography-16:</span> **Basic Fonts**
    [:octicons-arrow-right-24: View Fonts](https://archlinux.org){ .md-button style="border-color: #4caf50; color: #4caf50" }

    Basic Fonts documentation

-   <span style="color: #3f51b5">:material-window-maximize:</span> **Wayland Engine**
    [:octicons-arrow-right-24: View Wayland](https://archlinux.org){ .md-button style="border-color: #3f51b5; color: #3f51b5" }

    Wayland optimized architecture

-   <span style="color: #3f51b5">:material-login-variant:</span> **Auto Login**
    [:octicons-arrow-right-24: View Login](https://archlinux.org){ .md-button style="border-color: #3f51b5; color: #3f51b5" }

    Auto GNOME Login enabled

-   <span style="color: #3f51b5">:material-printer:</span> **Printer Support**
    [:octicons-arrow-right-24: View CUPS](https://archlinux.org){ .md-button style="border-color: #3f51b5; color: #3f51b5" }

    Printer Support via cups

-   <span style="color: #e91e63">:material-key:</span> **SSH Agent**
    [:octicons-arrow-right-24: View SSH](https://archlinux.org){ .md-button style="border-color: #e91e63; color: #e91e63" }

    SSH Agent managed by gcr

-   <span style="color: #e91e63">:material-controller:</span> **Gamemode**
    [:octicons-arrow-right-24: View Gamemode](https://archlinux.org){ .md-button style="border-color: #e91e63; color: #e91e63" }

    Gamemode preinstalled for performance

-   <span style="color: #e91e63">:material-text-box-remove-outline:</span> **No Xorg**
    [:octicons-arrow-right-24: View Display](https://archlinux.org){ .md-button style="border-color: #e91e63; color: #e91e63" }

    No Xorg display server included

</div>

---

### Additional Features

<div class="grid cards cols-3" markdown>

-   <span style="color: #9c27b0">:material-tune:</span> **Core Tweaks**
    [:octicons-arrow-right-24: View Tweaks](DOCS.md#core-tweaks){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    [Arch OS Core Tweaks](DOCS.md#core-tweaks) for system optimization.

-   <span style="color: #9c27b0">:material-image:</span> **Bootsplash**
    [:octicons-arrow-right-24: View Theme](https://github.com){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    [Arch OS Bootsplash](https://github.com) theme engine.

-   <span style="color: #9c27b0">:material-shield-lock:</span> **System Manager**
    [:octicons-arrow-right-24: View Manager](DOCS.md#arch-os-manager){ .md-button style="border-color: #9c27b0; color: #9c27b0" }

    [Arch OS System Manager](DOCS.md#arch-os-manager) administration tools.

-   <span style="color: #00bcd4">:octicons-terminal-16:</span> **Shell Upgrades**
    [:octicons-arrow-right-24: View Shell](DOCS.md#shell-enhancement){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    [Arch OS Shell Enhancement](DOCS.md#shell-enhancement) configurations.

-   <span style="color: #00bcd4">:material-rocket-launch:</span> **Starship Theme**
    [:octicons-arrow-right-24: View Starship](https://github.com){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    [Arch OS Starship Theme](https://github.com) prompt layout.

-   <span style="color: #00bcd4">:material-trash-can-outline:</span> **Housekeeping**
    [:octicons-arrow-right-24: View Housekeeping](DOCS.md#housekeeping){ .md-button style="border-color: #00bcd4; color: #00bcd4" }

    [Arch OS Automatic Housekeeping](DOCS.md#housekeeping) maintenance scripts.

-   <span style="color: #4caf50">:material-package-variant:</span> **AUR Helper**
    [:octicons-arrow-right-24: View AUR Setup](DOCS.md#advanced-installation){ .md-button style="border-color: #4caf50; color: #4caf50" }

    [AUR Helper](DOCS.md#advanced-installation) (configurable options).

-   <span style="color: #4caf50">:material-server:</span> **VM Support**
    [:octicons-arrow-right-24: View VM Info](DOCS.md#vm-support){ .md-button style="border-color: #4caf50; color: #4caf50" }

    [VM Support](DOCS.md#vm-support) (optional virtualization).

-   <span style="color: #4caf50">:material-lightning-bolt:</span> **Kernel Tweaks**
    [:octicons-arrow-right-24: View Kernel](https://archlinux.org){ .md-button style="border-color: #4caf50; color: #4caf50" }

    Advanced kernel optimizations and power management.

-   <span style="color: #e91e63">:material-shield-check:</span> **Security Policies**
    [:octicons-arrow-right-24: View Security](https://archlinux.org){ .md-button style="border-color: #e91e63; color: #e91e63" }

    Sandboxing and Sandbox Access Rule enhancements.

-   <span style="color: #e91e63">:material-content-copy:</span> **32-Bit Support**
    [:octicons-arrow-right-24: View Multilib](https://wiki.archlinux.org/title/Official_repositories#multilib:~:text=a%20lot%20more.-,multilib,-%5Bedit%20source){ .md-button style="border-color: #e91e63; color: #e91e63" }

    32 Bit Support (Multilib package compatibility layers).

-   <span style="color: #e91e63">:material-lock:</span> **Disk Encryption**
    [:octicons-arrow-right-24: View Encryption](https://wiki.archlinux.org/title/Data-at-rest_encryption){ .md-button style="border-color: #e91e63; color: #e91e63" }

    Disk Encryption via standard LUKS2 containers.

</div>

---

### Additional Packages (optional)

!!! abstract "NOTE"

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

###Arch OS Installation

!!! desc "Arch OS Installation"

    To install Arch OS, an internet connection is required, as many packages will be downloaded during the installation process.
    
#### 1. Prepare bootable USB Device

!!! recommendation "Prepare bootable USB Device"

    - Download latest Arch OS ISO from **[GitHub](https://github.com/murkl/arch-os/releases/latest)**
    
    - Alternatively, download official Arch Linux ISO from **[archlinux.org](https://www.archlinux.org/download)** or **[archlinux.de](https://www.archlinux.de/download)**
    
    - Use **[Ventoy](https://www.ventoy.net/en/download.html)** or your prefered iso writer tool to create a bootable USB device
    
    - Alternatively (Linux only): **[➜ Arch OS Creator](https://github.com/murkl/arch-os-creator)**
    
#### 2. Configure BIOS / UEFI Settings

!!! recommendation "Configure BIOS / UEFI Settings"

    - Disable Secure Boot
    
    - Set Boot Mode to UEFI
    
#### 3. Boot from USB Device

!!! recommendation "Boot from USB Device"
    
    - Load prefered keyboard layout (optional): `loadkeys de`
    
    - Connect to WLAN (optional): `iwctl station wlan0 connect 'SSID'`
    
#### 3.1. Run Arch OS Installer

!!! recommendation "Run Arch OS Installer"

    ```vim
    curl -Ls bit.ly/arch-os | bash
    ```
    
!!! important "NOTE!"

    **Note:** _Cancel the Arch OS Installer with `Ctrl + c`. The properties will be restored upon the next execution._
    
**[➜ See Advanced Installation](DOCS.md#advanced-installation)**

### System Maintenance

<p><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/manager_menu.png"></p>

!!! abstract "System Maintenance"

    After installing Arch OS with the default properties preset, most maintenance tasks are performed automatically. However, the following steps must be executed manually on a regular basis:
    
    - Regularly upgrade your system packages (Pacman/AUR & Flatpak)
    - Regularly read the **[Arch Linux News](https://www.archlinux.org/news)** (preferably before upgrading your system)
    - Regularly check & merge new configurations with `pacdiff` (preferably after each system upgrade)
    - Consult the **[Arch Linux Wiki](https://wiki.archlinux.org)** (if you need help)
    
    ---
    
    - To streamline this process, you can use the preinstalled **[➜ Arch OS System Manager](https://github.com/murkl/arch-os-manager)**
    
    - If you need to rescue your Arch OS in case of a crash, boot from an **[Arch ISO Device](#1-prepare-bootable-usb-device)** and start the **[➜ Arch OS Recovery](https://github.com/murkl/arch-os-recovery)** with:

    
    ```vim
    curl -Ls bit.ly/arch-os-recovery | bash
    ```
    
<details>

<summary><h2 style="display: inline;" id="screenshots">Screenshots</h2></summary>

<div align="center">
  <p><div><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/desktop_overview.jpg"></div><sub><i>Desktop Demo</i></sub></p>
  <p><div><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/bootsplash.png"></div><sub><i>Bootsplash Demo</i></sub></p>
  <p><div><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/starship.png"></div><sub><i>Starship Demo</i></sub></p>
  <p><div><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/fastfetch.png"></div><sub><i>Fetch Demo</i></sub></p>
  <p><div><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/desktop_apps.png"></div><sub><i>Desktop Core Apps Demo</i></sub></p>
  <p><div><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/manager_dashboard.png"></div><sub><i>System Manager Demo</i></sub></p>
  <p><div><img src="https://github.com/murkl/arch-os/raw/main/docs/screenshots/recovery.png"></div><sub><i>BTRFS Recovery Demo</i></sub></p>
</div>

</details>
