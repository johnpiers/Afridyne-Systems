---
icon: material/arch
---

<div style="display: none;">
  <h1>Header</h1>
</div>

![Local image](./images/logo.png){: style="display: block; margin: 0 auto"}
<H2 style="text-align: center;"> Arch Linux Install Guide</H2>


<div align="center">

<p dir="auto"><a href="https://github.com/silentz"><img src="https://camo.githubusercontent.com/d5e915e83cf7643f4d1a4fc8384359122e61d5bb8604ad5e6a2e7dd83e1f7205/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f417574686f722d4d6178696d5f5065727368696e2d666636663030" alt="Author" data-canonical-src="https://img.shields.io/badge/Author-Maxim_Pershin-ff6f00" style="max-width: 100%;"></a>
<a href="https://github.com/silentz/arch-linux-install-guide/blob/main/LICENSE.txt"><img src="https://camo.githubusercontent.com/bbb012395ef1fa09ec910634c05f9b3ac78fa2ab7ac4c9a825fba78b82a1adf7/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4170616368652d2d322e302d626c7565" alt="License" data-canonical-src="https://img.shields.io/badge/License-Apache--2.0-blue" style="max-width: 100%;"></a>
<a target="_blank" rel="noopener noreferrer nofollow" href="https://camo.githubusercontent.com/24e36cd8f72c9c0d9fbe2f6da1abc863e3946356994c41534ffd8cd33715d9a9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6173745f557064617465642d4175677573745f323032352d303262353332"><img src="https://camo.githubusercontent.com/24e36cd8f72c9c0d9fbe2f6da1abc863e3946356994c41534ffd8cd33715d9a9/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6173745f557064617465642d4175677573745f323032352d303262353332" alt="Last Updated" data-canonical-src="https://img.shields.io/badge/Last_Updated-August_2025-02b532" style="max-width: 100%;"></a></p>

</div>
<H3 style="text-align: center;">Arch Linux with Xfce4 and i3 Window Manager Installation Guide.</H3>

---

<H4 style="text-align: center;"><b>How to install Arch Linux with Xfce/i3 and not spend ages on debugging.</b></H4>

---

###Getting Started

Welcome to the Arch Linux with Xfce4 and i3 Window Manager Installation Guide!

This guide provides you with a step-by-step walkthrough of installing
Arch Linux along with the Xfce4 and i3 window manager. It has been carefully created
based on my own experience of installation Arch Linux on multiple devices over the years.
This guide aims to make your installation process as smooth as possible.

To begin your Arch Linux installation journey, please follow the step-by-step instructions provided below.

Support and Feedback

If you have any suggestions, corrections, or encounter any issues while following
the guide, I encourage you to get involved through Github.

**Issues:** If you come across any problems or have specific questions, please open
an issue on the Github repository for this guide. This allows me to track and
address your concerns effectively.

**Pull Requests:** If you have improvements or additions to the guide, feel free to submit
a pull request. Your contributions can help enhance the clarity of the guide for everyone.

Section 01: &#128640; Step-by-step guide of installing Arch Linux on your hardware. &#128640;

####Step 01: Downloading Arch Linux image
```
1. Go to Arch Linux downloads page https://archlinux.org/download/

2. Find **HTTP Direct Downloads** section and choose any download mirror.
   Select a mirror that is geographically closer to your location.

3. On the mirror page find archive named like `archlinux-YYYY.MM.DD-x86_64.iso` or `archlinux-x86_64.iso`
   or any other file with `.iso` suffix. Other files (like _.txt_, _.tar.gz_ and even _.iso.sig_)
   are not needed for installation process.
```
####Step 02: Preparing Installation Medium
```
1. Insert a USB-stick into your PC with at least 2Gb of space available on it.

2. Find corresponding block device for USB-stick in `/dev` folder. Usually it is `/dev/sdb`.
```
&#128161; IMPORTANT NOTE</b>: you need block device without a number on the end.
If you have for example /dev/sdb, /dev/sdb1 and /dev/sdb2  you need /dev/sdb!
<br>
```
3. Burn previously downloaded Arch Linux ISO-image on a USB-stick (in my case it is `/dev/sdb`):

$sudo dd conv=fsync oflag=direct status=progress bs=4M \
          if=./archlinux-YYYY.MM.DD-x86_64.iso of=/dev/sdb
```
 
####Step 03: Boot into Arch Linux Medium

```
1. Insert the installation medium into the computer on which you are installing Arch Linux.

2. Power on your PC and press _boot menu key_. For _Lenovo ThinkPad X1 Carbon_ series laptop,
   this key is `F12`.

3. Boot from USB-stick and wait until boot process is finished.
```

&#128161; IMPORTANT NOTE</b>: not every device can run a system from USB-stick out of the box.
Many BIOS'es by default come with activated <i>Secure boot</i> option.You might need to
deactivate it in your BIOS.


####Step 04: Syncronize Packages

```
1. [Optional] Connect to WiFi using `iwctl` and check connection is established:

$iwctl
[iwd]# station wlan0 get-networks
[iwd]# station wlan0 connect &lt;Name of WiFi access point&gt;
[iwd]# exit
$ ping 1.1.1.1

2. Synchronize pacman packaes:

$pacman -Syy
```

####Step 05: Disk partitioning

```
1. Partition main storage device using `fdisk` utility.
   You can find storage device name using `lsblk` command.

$fdisk /dev/nvme0n1
                [repeat this command until existing partitions are deleted]
Command (m for help): d
Command (m for help): d
Command (m for help): d

                [create partition 1: efi]
Command (m for help): n
Partition number (1-128, default 1): Enter &crarr;
First sector (..., default 2048): Enter &crarr;
Last sector ...: +256M

                [create partition 2: main]
Command (m for help): n
Partition number (2-128, default 2): <b>Enter &crarr;
First sector (..., default ...): Enter &crarr;
Last sector ...: -32G // double size of your RAM

                [create partition 3: swap]
Command (m for help): n
Partition number (3-128, default 3): <b>Enter &crarr;
First sector (..., default ...): Enter &crarr;
Last sector ...: Enter &crarr;

                [change partition types]
Command (m for help): t
Partition number (1-3, default 1): 1
Partion type or alias (type L to list all): uefi
Command (m for help): t
Partition number (1-3, default 2): 2
Partion type or alias (type L to list all): linux
Command (m for help): t
Partition number (1-3, default 3): 3
Partion type or alias (type L to list all): swap

                [write partitioning to disk]
Command (m for help): w

2. Create filesystems on created disk partitions:

$mkfs.fat -F 32 /dev/nvme0n1p1  #on EFI System partition>
$mkfs -t ext4 /dev/nvme0n1p2   #on Linux filesystem partition
$mkswap /dev/nvme0n1p3         #on Linux swap partition

3. Correctly mount all filesystems to the `/mnt`:

$mount /dev/nvme0n1p2 /mnt
$mkdir -p /mnt/boot/efi
$mount /dev/nvme0n1p1 /mnt/boot/efi
$swapon /dev/nvme0n1p3

4. Install essential packages into new filesystem and generate fstab:

$pacstrap -i /mnt base linux linux-firmware sudo vim
$enfstab -U -p /mnt > /mnt/etc/fstab

```

####Step 06: Basic configuration of new system
```
1. Chroot into freshly created filesystem:

$arch-chroot /mnt

2. Setup system locale and timezone, sync hardware clock with system clock:

$vim /etc/locale.gen   #uncomment your locales, i.e. `en_US.UTF-8` or `en_GB.UTF-8`
$locale-gen
$echo "LANG=en_US.UTF-8" > /etc/locale.conf                #choose your locale
$ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime   #choose your timezone
$hwclock --systohc

3. Setup system hostname:

$echo yourhostname > /etc/hostname
$vim /etc/hosts
    127.0.0.1 localhost
   ::1       localhost
   127.0.1.1 yourhostname

4. Add new users and setup passwords:

$useradd -m -G wheel,storage,power,audio,video -s /bin/bash yourusername
$passwd root
$passwd <i>yourusername

5. Add wheel group to sudoers file to allow users to run sudo:

$visudo
    [uncomment following line in file]
     %wheel ALL=(ALL) ALL

6. Install and configure GRUB:

$pacman -S grub efibootmgr
$grub-install /dev/nvme0n1
$grub-mkconfig -o /boot/grub/grub.cfg

7. Setup networking stack:

$pacman -S dhcpcd networkmanager resolvconf
$systemctl enable dhcpcd
$systemctl enable NetworkManager
$systemctl enable systemd-resolved

8. Exit chroot, unmount all disks and reboot:

$exit
$umount /mnt/boot/efi
$umount /mnt
$reboot>
```

####Section 02: Configuring userspace after initial system setup &#127919;

Step 01: Basic configuration of userspace
```
1. Activate time syncronization using NTP:

$timedatectl set-ntp true

2. [Optional] Connect to WiFi using `nmcli`:

$nmcli device wifi connect &lt;Name of WiFi access point&gt; password &lt;password&gt;

3. Install X.Org and its utilities:

$sudo pacman -S xorg xorg-apps xorg-xinit xorg-xlsfonts xdotool xclip xsel

4. Install a bunch of useful utilities:

$sudo pacman -S dbus            #Message bus used by many applications
$sudo pacman -S intel-ucode     #Microcode update files for Intel CPUs
$sudo pacman -S fuse2           #Interface for programs to export a filesystem to the Linux kernel
$sudo pacman -S lshw            #Provides detailed information on the hardware of the machine
$sudo pacman -S powertop        #A tool to diagnose issues with power consumption and power management
$sudo pacman -S inxi            #Full featured CLI system information tool
$sudo pacman -S acpi            #Client for battery, power, and thermal readings

$sudo pacman -S base-devel      #Basic tools to build Arch Linux packages
$sudo pacman -S git             #Distributed version control system
$sudo pacman -S zip             #Compressor/archiver for creating and modifying zipfiles
$sudo pacman -S unzip           #For extracting and viewing files in .zip archives
$sudo pacman -S p7zip           #For extracting and viewing files in .7z archives
$sudo pacman -S htop            #Interactive CLI process viewer
$sudo pacman -S tree            #A directory listing program

$sudo pacman -S dialog          #A tool to display dialog boxes from shell scripts
$sudo pacman -S reflector       #Script to retrieve and filter the latest Pacman mirror list
$sudo pacman -S bash-completion #Programmable completion for the bash shell

$sudo pacman -S iw              #CLI configuration utility for wireless devices
$sudo pacman -S wpa_supplicant  #A utility providing key negotiation for WPA wireless networks
$sudo pacman -S tcpdump         #Powerful command-line packet analyzer
$sudo pacman -S mtr             #Combines the functionality of traceroute and ping into one tool
$sudo pacman -S net-tools       #Configuration tools for Linux networking
$sudo pacman -S conntrack-tools #Userspace tools to interact with the Netfilter tracking system
$sudo pacman -S ethtool         #Utility for controlling network drivers and hardware
$sudo pacman -S wget            #Network utility to retrieve files from the Web
$sudo pacman -S rsync           #File copying tool for remote and local files
$sudo pacman -S socat           #Multipurpose socket relay
$sudo pacman -S openbsd-netcat  #Netcat program. OpenBSD variant.
$sudo pacman -S axel            #Light command line download accelerator
$sudo pacman -S bind            #I use dig utility for DNS resolution from this package

5. Install Xfce4, i3, or both:
```

####Instructions for installing Xfce4
```
$sudo pacman -S xfce4
$sudo pacman -S xfce4-notifyd xfce4-screensaver xfce4-screenshooter
$sudo pacman -S thunar-archive-plugin thunar-media-tags-plugin
$sudo pacman -S network-manager-applet
$sudo pacman -S xfce4-xkb-plugin         xfce4-battery-plugin \
                 xfce4-datetime-plugin    xfce4-mount-plugin   \
                 xfce4-netload-plugin     xfce4-wavelan-plugin \
                 xfce4-pulseaudio-plugin  xfce4-weather-plugin \
                 xfce4-whiskermenu-plugin
```
####Instructions for installing i3
```
$sudo pacman -S i3-wm i3status i3lock pango
$sudo pacman -S lxappearance

# You will most probably need these apps for i3

$sudo pacman -S polybar      #nice statusbar for i3-based UIs
$sudo pacman -S rofi         #like dmenu, but more customizable
$sudo pacman -S alacritty      #terminal emulator
$sudo pacman -S dunst        #notification manager
$sudo pacman -S feh          #fast and light image viewer
$sudo pacman -S xss-lock     #screen lock controller
$sudo pacman -S flameshot    # screenshot app
$sudo pacman -S gsimplecal   #small calendar widget
$sudo pacman -S yazi         #console file manager

# additionals to yazi:

$sudo pacman -S ueberzugpp   #viewing images in terminal

6. Install login session manager, I prefer `ly` for it's minimalism:

$sudo pacman -S ly
$sudo systemctl enable ly

7. Install essential system fonts:

$sudo pacman -S ttf-dejavu ttf-freefont ttf-liberation ttf-droid terminus-font
$sudo pacman -S noto-fonts noto-fonts-emoji ttf-ubuntu-font-family ttf-roboto
  ttf-roboto-mono ttf-ibm-plex

8. [Optional] Enable sound support on your PC:

$sudo pacman -S sof-firmware   #Sound Open Firmware
$sudo pacman -S pulseaudio      #A featureful, general-purpose sound server
$sudo pacman -S pavucontrol     #PulseAudio Volume Control
$sudo pacman -S alsa-utils      #Advanced Linux Sound Architecture - Utilities
$sudo pacman -S alsa-plugins    #Additional ALSA plugins

9. [Optional] Enable bluetooth support on your PC:

$sudo pacman -S bluez bluez-utils blueman
$sudo systemctl enable bluetooth

10. [Optional] Enable printing support on your PC:

$sudo pacman -S cups cups-filters cups-pdf system-config-printer
$sudo pacman -S hplip    #for HP devices
$>sudo systemctl enable cups.service
```

&#128161; IMPORTANT NOTE: if there is no option for system-config-printer in xfce4-settings-manager,
go to <code>/usr/share/applications/system-config-printer.desktop</code> and set
<code>Categories=System;Settings;X-XFCE-SettingsDialog;X-XFCE-HardwareSettings;</code>

```
11. [Optional] Improve battary usage with TLP - utility that basically does kernel settings
    tweaking that improve power consumption. More information about TLP
    [can be found here](https://linrunner.de/tlp/). More information about TLP-RDW (radio device wizard)
    [can be found here](https://linrunner.de/tlp/settings/rdw.html).

$sudo pacman -S tlp tlp-rdw
$sudo systemctl enable tlp

# execute following commands only if using TLP-RDW:

$sudo systemctl enable NetworkManager-dispatcher.service
$sudo systemctl mask systemd-rfkill.service
$sudo systemctl mask systemd-rfkill.socket


12. [Optional] Run service that will discard unused blocks on mounted filesystems. This is useful for
    solid-state drives (SSDs) and thinly-provisioned storage. More information on fstrim
    [can be found here](https://man7.org/linux/man-pages/man8/fstrim.8.html).

$sudo systemctl enable fstrim.timer


13. [Optional] Install GTK themes and icons:

$sudo pacman -S arc-gtk-theme adapta-gtk-theme materia-gtk-theme
$sudo pacman -S papirus-icon-theme


14. [Optional] Choose fastest pacman mirrors (use your own country list):

$sudo reflector --country Germany,Austria,Switzerland \
                 --fastest 10 \
                 --threads $(nproc) \
                 --save /etc/pacman.d/mirrorlist</b>

15. [Optional] Install NetworkManager addons:

$sudo pacman -S nm-connection-editor networkmanager-openvpn


16. [Optional] Install vulkan drivers:

$pacman -S mesa vulkan-intel   #only for systems with Intel graphics
$pacman -S nvidia-utils        #only for systems with Nvidia graphics
$pacman -S amdvlk              #only for systems with AMD graphics

17. Reboot to finalize installation:

$reboot
```

####Step 02: Enable hibernation support
```
1. Open your `/etc/fstab` and find UUID for your swap partition

2. Open GRUB configuration file and add resume UUID to `GRUB_CMDLINE_LINUX_DEFAULT`:

$sudo vim /etc/default/grub
  Example:
  ...
  GRUB_CMDLINE_LINUX_DEFAULT="quiet splash
  resume=UUID=&lt;UUID of your swap partition&gt;"
  GRUB_CMDLINE_LINUX_DEFAULT="quiet splash
  resume=UUID=97d9e9f5-899f-4e9e-910e-623a5f665271 "
  ...

3. Generate GRUB config:

$sudo grub-mkconfig -o /boot/grub/grub.cfg

4. Open mkinitcpio configuration file and add `resume` hook:

$sudo vim /etc/mkinitcpio.conf</b>
  Example:
  ...
  HOOKS="base udev resume autodetect modconf block filesystems keyboard fsck"
  ...

5. Generate initramfs:

$sudo mkinitcpio -p linux

6. From now onwards, you can hibernate your system using:

$sudo systemctl hibernate
```

####Section 03: Installing Third-party Apps and Setting up dev Environment &#129489;&#8205;&#128187;


    These is my personal list of apps and utilities which I use on regular basis,
    so feel free to fork this repo and add something yours


####Step 01 - General-purpose Apps
```
$sudo pacman -S chromium          #web-browser
$sudo pacman -S obsidian          #note-taking app
$sudo pacman -S bitwarden         #password manager for all devices
$sudo pacman -S bitwarden-cli     #command line bitwarden client
$sudo pacman -S mousepad          #simple graphical text editor
$sudo pacman -S file-roller       #archive manager
$sudo pacman -S evince            #pdf viewer
$sudo pacman -S xournalpp         #pdf editor
$sudo pacman -S libreoffice       #office packages
$sudo pacman -S gimp              #image editor
$sudo pacman -S gpick             #color picker
$sudo pacman -S inkscape          #vector graphics editor
$sudo pacman -S fontforge         #fonts editor
$sudo pacman -S gparted           #grphical disk management tool>
$sudo pacman -S vlc               #video player
$sudo pacman -S remmina           #remote desktop client
$sudo pacman -S shotcut           #video editing tool
$sudo pacman -S evolution         #email client
$sudo pacman -S redshift          #adjusts the color temperature of your screen
$sudo pacman -S obs-studio        #screencasting and streaming app
$sudo pacman -S wireshark-qt      #network protocol analyzer
$sudo pacman -S spotify-launcher  #spotify client
$sudo pacman -S telegram-desktop  #my preffered messenger
$sudo pacman -S rclone            #manage or migrate files on cloud storage
$sudo pacman -S openvpn           #openvpn client
$sudo pacman -S wireguard-tools   #wireguard client
$sudo pacman -S arandr            #gui for xrandr
```

####Step 02 - Install Package Manager for AUR (Arch User Repository)
```
$git clone https://aur.archlinux.org/yay.git
$cd yay
$makepkg -si
```

####Step 03 - Software Development Tools
```
1. General purpose development tools:

$sudo pacman -S neovim           #powerful console editor
$sudo pacman -S zed              #ultimate graphical editor
$sudo pacman -S tree-sitter      #parsing system for programming tools
$sudo pacman -S tree-sitter-cli  #cli tool tree-sitter parsers
$sudo pacman -S stow             #configuration manager
$sudo pacman -S sqlite3          #console sqlite client
$sudo pacman -S tldr             #collection of simplified man pages
$sudo pacman -S jq               #cli json processor
$sudo pacman -S tmux             #terminal session multiplexer
$sudo pacman -S nmap             #network scanner with advanced features
$sudo pacman -S masscan          #high performance network scanner</i>
$sudo pacman -S pgcli            #console client for PostgreSQL</i>
$sudo pacman -S redis            #console client for Redis</i>
$sudo pacman -S apache           #http server + some useful utilities (htpasswd)
$sudo pacman -S meld             #git visual diff and merge tool
$sudo pacman -S websocat         #command line client for websockets
$sudo pacman -S sshpass          #noninteractive ssh password provider</i>
$sudo pacman -S git-filter-repo  #faster and safer git-filter-branch alternative
$sudo pacman -S httpie           #human-friendly CLI HTTP client for the API era
```

&#128161; IMPORTANT NOTE: execute <code>sudo setcap 'cap_net_raw+epi' /usr/bin/masscan</code> to enable
the ability to run <code>masscan</code> as non-root user.

```
2. Infrastructure as a Code and DevOps tools:

$sudo pacman -S ansible         #infrastructure as a code tool (bare metal)
$sudo pacman -S podman          #cli tool for container management
$sudo pacman -S podman-compose  #run multi-container applications with podman
$sudo pacman -S docker          #cli tool for container management
$sudo pacman -S docker-compose  #run multi-container applications with docker
$sudo pacman -S kubectl         #cli tool for managing kubernetes clusters
$sudo pacman -S helm            #package manager for kubernetes
$sudo pacman -S terraform       #infrastructure as a code tool (clouds)

#configure docker>

$sudo systemctl enable docker            #enable docker daemon on system start
#sudo usermod -a -G docker yourusername  #to be able to run docker as non-root
$newgrp docker                           #login to docker group without restart

3. Install Golang and its tools:

$sudo pacman -S go
$go install github.com/fullstorydev/grpcurl/cmd/grpcurl@latest
$go install github.com/hairyhenderson/gomplate/v4/cmd/gomplate@latest

4. Install Java and its tools

$sudo pacman -S jdk8-openjdk    #OpenJDK Java  8 development kit
$sudo pacman -S jdk11-openjdk   #OpenJDK Java 11 development kit
$sudo pacman -S jdk17-openjdk   #OpenJDK Java 17 development kit
$sudo pacman -S jdk21-openjdk   #OpenJDK Java 21 development kit
$sudo pacman -S jdk-openjdk>    #OpenJDK Java 22 development kit
$sudo pacman -S maven           #Java project management tool
$sudo pacman -S gradle          #Java project management tool
```

&#128161; IMPORTANT NOTE: JVM version can be switched using<br> <code>archlinux-java</code> List all available JVM versions using<br> <code>archlinux-java status</code> and set one using <code>archlinux-java set VERSION</code>

```
5. Install Dart and Flutter following instructions from:

 https://docs.flutter.dev/get-started/install/linux

6. Install C, C++ and tools for low-level development:

$sudo pacman -S gcc        #GNU Compiler Collection, C and C++ frontends
$sudo pacman -S gdb        #GNU Debugger
$sudo pacman -S clang      #C/C++ frontend compiler for LLVM
$sudo pacman -S cmake      #C/C++ project management too
$sudo pacman -S ninja      #Build system with a focus on speed
$sudo pacman -S cuda       #NVIDIA GPU programming toolkit
$sudo pacman -S nasm       #Asssembler for the x86 CPU architecture
$sudo pacman -S boost      #C++ library with general purpose utils and data structures
$sudo pacman -S cdrtools   #CD/DVD/BluRay command line recording software
$sudo pacman -S qemu-full  #Open source machine emulator and virtualizer
$sudo pacman -S flex       #A tool for generating text-scanning programs
$sudo pacman -S bison      #The GNU general-purpose parser generator
$sudo pacman -S gperf      #Perfect hash function generator
$sudo pacman -S libusb     #Library that provides generic access to USB devices
$sudo pacman -S ccache     #Compiler cache that speeds up recompilation by caching previous compilations
$sudo pacman -S dfu-util   #Tool intended to download and upload firmware using DFU protocol to devices connected over USB

7. Install Python and its tools:

$sudo pacman -S python              #python itself
$sudo pacman -S python-pip          #python package manager
$sudo pacman -S python-virtualenv   #python virtualenv
$sudo pacman -S python-poetry>      #python package manager (better one)

8. Install Lua:

$sudo pacman -S lua       #Collection of Lua tools


9. Install JavaScript and its tools:

$sudo pacman -S nodejs    #JavaScript runtime
$sudo pacman -S npm       #JavaScript package manager
$sudo pacman -S yarn      #JavaScript package manager


10. Install Rust and its tools:

$sudo pacman -S rust    #Rust compiler and tools for project management.


11. Install Virtualbox:

$sudo pacman -S linux-headers         #Headers for building Linux kernel modules
$sudo pacman -S virtualbox-host-dkms  #VirtualBox Host kernel modules sources
$sudo pacman -S virtualbox            #Hypervisor for x86 virtualization


12. Architecture diagraming tools:

$sudo pacman -S plantuml   #Tool for creating UML diagrams

13. Install hugo (static website generator):

$sudo pacman -S hugo       #fast and flexible static site generator in go
$sudo pacman -S dart-sass  #implementation of sass (required for hugo)

14. Accounting software:

$sudo pacman -S gnucash #Personal and small-business financial-accounting application.

15. 3D-Printing software:

$sudo pacman -S freecad :Feature based parametric 3D CAD modeler
$sudo pacman -S prusa-slicer :G-code generator for 3D printers

16. Security related software:

$sudo pacman -S zaproxy          #integrated penetration testing tool for finding vulnerabilities in web applications
$sudo pacman -S gobuster         #directory, file, dns and vhost busting tool written in go
$sudo pacman -S radare2          #open-source tools to disasm, debug, analyze and manipulate binary files
$sudo pacman -S ghidra           #software reverse engineering framework
$r2pm -U && r2pm -ci r2ghidra    #integrate ghidra decompiler into radare2


17. Games:

$sudo pacman -S 0ad    #cross-platform, 3d and real-time strategy game

```

####Step 04: Install Wine (Windows application runner)
```
1. Go to `/etc/pacman.conf` and uncomment (or add) following lines:

[multilib]
include = /etc/pacman.d/mirrorlist

2. Update package database:

$sudo pacman -Syu

3. Install Wine and its utilities:

$sudo pacman -S wine        #Compatibility layer for running Windows programs
$sudo pacman -S wine-mono   #Wine's replacement for Microsoft's .NET Framework
$sudo pacman -S wine-gecko  #Wine's replacement for Microsoft's Internet Explorer
$sudo pacman -S winetricks  #Installer for various runtime libraries in Wine</i>
$sudo pacman -S zenity      #Display dialog boxes from shell scripts (wine dependency)

4. Configure smooth font in Wine applications:

$winetricks settings fontsmooth=rgb
```

&#128161; IMPORTANT NOTE</b>: if you are facing error
<code>wine: Read access denied for device L"\\??\\Z:\\", FS volume label and serial are not available</code>,
go to <code>~/.wine/dosdevices</code>, remove <code>z:</code> symbolic link and make it point to your <code>$HOME</code><br>
<br>
####Step 05: Install texlive (LaTeX distribution)

```
1. Download texlive installer:

$wget http://mirrors.ctan.org/systems/texlive/tlnet/install-tl-unx.tar.gz

2. Unpack texlive installer archive:

$mkdir ./texlive
$tar -xvf install-tl-unx.tar.gz -C texlive --strip-components=1

3. Run texlive install and select nearest CTAN mirror:

$cd ./texlive
$sudo ./install-tl -select-repository
```

####Step 06: Setup Android development tools

```
1. Download zip-archive from here: https://developer.android.com/studio
   from _Command line tools only_ section.

2. Unpack archive and copy cmdline-tools to `$ANDROID_HOME`:

$unzip commandlinetools-linux-..._latest.zip  # archive you got from website

$mkdir -p ~/Android/cmdline-tools/latest
$mv ./cmdline-tools/* ~/Android/cmdline-tools/latest/

3. Set `ANDROID_HOME` environment variable to `~/Andoird` in `.bashrc`

4. Install platform tools, build tools and accept all licenses:

$sdkmanager "platform-tools" "platforms;android-29"
$sdkmanager "build-tools;29.0.3"
$sdkmanager --licenses
$sdkmanager --update

```

####Step 07: Install Yubikey tools
```
$sudo pacman -S yubikey-manager
$sudo pacman -S yubikey-personalization-gui

```
####Bonus: My list of reverse engineering tools
```
1. Binary reverse engineering:
   `gdb`, `strace`, `ltrace`, `ldd`, `objdump` `radare2`, `frida`,
   `Ghidra`, `IDA Pro`, `cutter` + `rz-ghidra` + `cutterref`, `angr-management`
   `API Monitor`, `PEiD`, `UpxUnpacker`

2. Python: `pycdc`

3. Java: `jd-gui`, `jadx`

4. C#: `Avalonia ILSpy`
```
<h3 align="center">
    Section 04: F.A.Q.s, bug fixes and other useful tips and playbooks
    for Arch Linux &#129714;
</h3>

####Playbook 01: Fix XHCI hibernation error. <br>
<br>
In some Linux kernels there are some broken USB 3.0 device drivers, that
_sometimes_ wake up the system right after you launch hibernation process. 
If you see errors like this in your`dmesg` command output after an 
unsuccessful hibernation:

```
xhci_hcd 0000:00:14.0: PM: pci_pm_freeze(): hcd_pci_suspend+0x0/0x20 returns -16
xhci_hcd 0000:00:14.0: PM: dpm_run_callback(): pci_pm_freeze+0x0/0xc0 returns -16
xhci_hcd 0000:00:14.0: PM: failed to freeze async: error -16

```
To fix the issue put following lines in `/usr/lib/systemd/system-sleep/xhci` and make this file executable: <br>
<br>

```
#!/bin/sh
#
run_pre_hook() {
    echo "Disable xhci module before suspend at $(date)..."
    >> /tmp/systemd_suspend_log 
    grep XHC.\*enable /proc/acpi/wakeup && echo XHC > /proc/acpi/wakeup
}
#
run_post_hook() {
    echo "Enable xhci module after wakeup from $(date)" >> /tmp/systemd_suspend_log
    grep XHC.\*disable /proc/acpi/wakeup && echo XHC > /proc/acpi/wakeup
}
#
case $1 in
    pre) run_pre_hook ;;
    post) run_post_hook ;;
esac

```

Original solution: https://gist.github.com/ioggstream/8f380d398aef989ac455b93b92d42048<br>
<br>
####Playbook 02: Fix GRUB screen resolution

```
_This can help if you have very tiny grub font on your 4k monitor_

1. Open `/etc/default/grub` with text editor and add following lines:

GRUB_TERMINAL_OUTPUT="gfxterm"
GRUB_GFXPAYLOAD_LINUX=keep
GRUB_GFXMODE=1920x1080x32,1024x768x32,auto

2. Generate `grub.cfg`:

$sudo grub-mkconfig -o /boot/grub/grub.cfg
```

####Playbook 03: Fix Lightdm screen resolution
```
_This can help if you use lightdm and have very tiny font on your 4k monitor_
```

Open <code>/etc/lightdm/lightdm.conf</code> file and add following line under <code>[Seat:\*]</code> section:

display-setup-script=xrandr --output eDP-1 --mode 1920x1080

P.S. your screen output name, like eDP-1 in my case, can be found in <code>xrandr -q</code><br>
<br>

Playbook 04: Activate dark mode in GTK apps
```
$gsettings set org.gnome.desktop.interface color-scheme 'prefer-dark'

```
Playbook 05: System goes to sleep too fast with Xfce
```
- If system goes to sleep after 3-5 minutes, this might be screensaver.
  To stop this, disable option `Settings -> Screensaver 
  -> Activate Screensaver when computer is idle`.
```
Playbook 06: All requests, expept those to internal addresses, fail after launching Wireguard VPN
```
- This happens when your Wireguard server can only handle requests only to configured
  IP addresses and DNS names.
  Use `resolvectl revert wg0` (change `wg0` to your wireguard interface name).
  This will prevent system from using Wireguard interface for all routes.
```
Playbook 07: Screen frozen (or hangs) after 2-10 minutes of inactivity when using Picom
```
- If your screen freezes (or hangs) while not touching keyboard or mouse for some time
  (usually 2-10 minutes), this might be an issue with picom.
  Try first stopping picom at all to see if this helps.
  If yes, try to change rendering backend of picom from `xrender` to `glx`
  and check if it helps. Worked for me.
```
Playbook 08: Remove annoying menubar from Slack<br>
<br>
- `Window -> Always show menu bar -> disable`<br>
<br>
Playbook 09: Encrypt external disk.<br>

```
1. [Only once] Select disk partition to be encrypted (in this example `/dev/sdb1`)
   and initialize LUKS:

$sudo cryptsetup luksFormat /dev/sdb1
```
```
2. Open and decrypt LUKS partition, this will create decrypted device at `/dev/mapper/cryptdev`

$sudo cryptsetup open /dev/sdb1 <i>cryptdev</i>
```
```
3. [Only once] Initialize filesystem on decrypted partition, in this example `ext4`:

$sudo mkfs.ext4 /dev/mapper/cryptdev
```
```
4. Mount created filesystem, to `/mnt` folder in this example, and use it as you want:

$sudo mount /dev/mapper/<i>cryptdev</i> /mnt
```
```
5. Unmount filesystem and close LUKS device after using it:

$sudo umount /mnt
$sudo cryptsetup close 'cryptdev'
```
```
6. [If needed] Change LUKS disk encryption passphrase:

TLDR: LUKS generates a single master key (also known as the "encryption key"), which is used to encrypt
the data on the disk. Instead of storing the master key directly, LUKS uses key slots. Each slot contains the
master key encrypted with a unique password or other authentication information. To change the password, we
need to obtain LUKS slot number for the current key.

$sudo cryptsetup luksDump /dev/sdb1             #most probably it will be 0
$sudo cryptsetup luksChangeKey /dev/sdb1 -S 0   #use your own slot number in -S parameter
```

```
Playbook 10: Fix external microphone artefacts happening after ~20 minutes of connection

1. Open: /etc/pulse/daemon.conf>
2. Set `exit-idle-time = -1`. Don't forget to uncomment this line if it's uncommented.
3. Stop pulseaudio service: `pulseaudio -k`
4. Clear pulseaudio cache: `rm -r ~/.config/pulse/*`
5. Start pulseaudio once again: `pulseaudio --start`
```
-----------------------------------------------------------------------------------------------------------------------------------------------<br>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/3jdKH6bLgUE?si=tNeqElaTxPdZeio8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<br>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/5DHz23VQJxk?si=RB3ElcZRXcxro4Ty" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
<br>
<br>
<iframe width="560" height="315" src="https://www.youtube.com/embed/vQUOf2E6XZw?si=UwPDwoiu5fCZZOx1" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
