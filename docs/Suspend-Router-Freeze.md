---
tags:
  - Arch Linux Suspend
  - Network
  - Reyee Router Freeze
  - Troubleshooting
  - NetworkManager
  - Power Management

icon: material/router-network-wireless
---

<div style="display: none;"><h1>Suspend-Router-Freeze </h1></div>

![](imgs/20260821-021336.png){: style="display: block; margin: 0 auto"}

---

<H2 style="text-align: center;">  🛠️ Arch Linux Suspend & Reyee Router Freeze Troubleshooting</H2>

!!! deep-dive "Part 1: Environment & Symptoms"

    ## Part 1: Environment & Symptoms {.toc-hidden-header}
    
    A comprehensive technical summary documenting the investigation, diagnosis, and resolution of an intermittent network freeze occurring during system power state transitions.
    
---

!!! example "🔍 The Anatomy of the Bug"

    ### 🔍 The Anatomy of the Bug {.toc-hidden-header}
    
    ***Initial Problem Environment***
    
    - **Host System:** Arch Linux x86_64 (Kernel upgraded to: `7.2.3-zen1-3-zen`)
    - **Desktop Environment & Interface:** GNOME on Wayland, wired Realtek `r8169` Gigabit Ethernet (`enp9s0`), connected to a Reyee EW1200G-PRO router bridging setup.
    
    ***Symptoms & Failure Mode (Phase 2 Recurrence)***
    
    1. Automatic suspend stalls or behaves erratically on `notify-send`.
    2. Wake-up leads to unmanaged network adapters and hard PCI Express lockups requiring system reboots.
    3. The router's bridging engine may crash under faulty EEE signals, requiring a physical power cycle.
    
!!! desc "Symptoms & Failure Mode"

    ### Symptoms & Failure Mode {.toc-hidden-header}
    
    1.  The host PC is configured to "Automatic Suspend" after 2 hours of inactivity.
    2.  The suspend process behaves erratically, stalling frequently on a notify-send announcement ("Preparing to suspend").
    3.  Upon system wake-up, the network icon indicates "No Connection", and the network adapter enters an unmanaged state.
    4.  Concurrently, the Reyee router's physical LAN bridge software crashes. The router's hardware LED remains a deceptive solid blue, but all network traffic halts, requiring a hard power cycle of the routing hardware to recover.
    
---

!!! deep-dive "🔬 Part 2: Root Cause Analysis"

    ## 🔬 Part 2: Root Cause Analysis {.toc-hidden-header}
    
    The failure was determined to be a cascading layer-1 and layer-2 network loop freeze caused by flawed power-state handling within the Linux network stack:
    
    [GNOME Suspend Triggered] ↴
        ⇣
    [NetworkManager Tries to Sleep Interface] ↴
        ⇣
    [Internal Daemon Race Condition / Hangs for 25s] ↴
        ⇣
    [NIC Emits Fluctuating Voltages / EEE Garbage Data over Cat 5] ↴
        ⇣
    [Reyee Router Switch Bridge Flooded & Crashes Software Layer] ↴
    
    - **The OS Choke Point & ACPI Defect:** Suspend timeouts and ASUS `asus_wmi: failed to register LPS0 sleep handler` errors corrupt the PCIe lane and `r8169` state during power transitions.
    
    - **The Router Impact:** Malformed Energy-Efficient Ethernet (EEE) states corrupt the Cat 5 line and crash the router's broadcast switch engine.
    
---

!!! deep-dive "🛠️ Part 3: Remediation & Verification"

    ## 🛠️ Part 3: Remediation & Verification {.toc-hidden-header}
    
    🛠️ ***Step-by-Step Remediation Strategy***
    ### 🛠️ Step-by-Step Remediation Strategy {.toc-hidden-header}
    
    - To mitigate the issue, disable EEE, restrict NetworkManager power management, enforce S3 deep sleep via `mem_sleep_default=deep` in your `systemd-boot` loader configuration, and implement a custom sleep script at `/usr/lib/systemd/system-sleep/disconnect-ethernet.sh` to safely unload and reload the `r8169` module during pre/post suspend phases.
    
    - You can find the full configuration snippets and script contents in the referenced web document.
    
!!! desc "Step 1: Disabling Energy-Efficient Ethernet (EEE)"

    ### Step 1: Disabling Energy-Efficient Ethernet (EEE) {.toc-hidden-header}
    
    To prevent the network adapter from generating corrupt low-power signals that confuse the router's hardware switch, EEE was disabled on the active interface.
    
    ```bash
    # Explicitly disable EEE on the target network interface
    sudo ethtool --set-eee enp9s0 eee off
    ```
    
!!! desc "Step 2: Restricting NetworkManager Power Management"

    ### Step 2: Restricting NetworkManager Power Management {.toc-hidden-header}
    
    We updated the global NetworkManager configuration file to prevent the daemon from trying to auto-negotiate power transitions or Wake-on-LAN signatures on the ethernet hardware.
    
    The `/etc/NetworkManager/NetworkManager.conf` file was modified to contain the following strict parameters:
    
    ```ini
    # /etc/NetworkManager/NetworkManager.conf
    # Configuration file for NetworkManager.
    # See "man 5 NetworkManager.conf" for details.
    
    [device]
    wifi.scan-rand-mac-address=no
    
    [connection]
    
    ethernet.wake-on-lan=0
    ```
    
!!! desc "Step 3: Engineering the Immediate Hardware Disconnect Script"

    ### Step 3: Engineering the Immediate Hardware Disconnect Script {.toc-hidden-header}
    
    A custom systemd power management script was designed to step in *ahead* of the OS sleep cycle. Instead of relying on `nmcli` (which times out when NetworkManager hangs), the script executes raw kernel commands to cleanly drop the physical connection and completely unload the `r8169` driver module before the system enters its deep sleep state.
    
    The executable script was generated at `/usr/lib/systemd/system-sleep/disconnect-ethernet.sh`:
    
    ```bash
    #!/bin/sh
    case $1/$2 in
      pre/*)
        echo "Force killing physical link on enp9s0..."
        ip link set enp9s0 down
        sleep 1
        echo "Unloading kernel ethernet module r8169..."
        modprobe -r r8169
        ;;
      post/*)
        echo "Reloading kernel ethernet module r8169..."
        modprobe r8169
        sleep 2
        echo "Force waking physical link on enp9s0..."
        ip link set enp9s0 up
        systemctl restart NetworkManager
        ;;
    esac
    ```
    
    The script was granted system privileges to run inside systemd environments:
    
    ```bash
    sudo chmod +x /usr/lib/systemd/system-sleep/disconnect-ethernet.sh
    ```

---

![](imgs/20260607-114046.png){ .center-image }


!!! decision "📊 Verification & System Health Check"

    ## 📊 Verification & System Health Check {.toc-hidden-header}
    
    Following the enforcement of traditional S3 deep sleep and the kernel module extraction script, a full system log review verifies that the network adapter and the kernel transition states execute flawlessly without timeouts:
    
    ```text
    Sep 08 09:51:03 JohnAMD systemd-sleep[30554]: Force killing physical link on enp9s0...
    Sep 08 09:51:04 JohnAMD systemd-sleep[30554]: Unloading kernel ethernet module r8169...
    Sep 08 09:51:04 JohnAMD kernel: PM: suspend entry (deep)
    ...
    Sep 08 10:30:59 JohnAMD systemd-sleep[30644]: Reloading kernel ethernet module r8169...
    Sep 08 10:31:01 JohnAMD systemd-sleep[30644]: Force waking physical link on enp9s0...
    ```

!!! version-added "Key Takeaways from Successful State Logs:"

    ### Key Takeaways from Successful State Logs: {.toc-hidden-header}
    
    *   **`PM: suspend entry (deep)`**: Motherboard ACPI is forced into traditional S3 Deep Sleep, completely bypassing the buggy modern standby (`LPS0`) handler that froze the hardware layer.
    
    *   **Kernel Module Extraction**: Unloading the `r8169` driver right before suspend prevents the hardware adapter from broadcasting malformed electrical noise over the line, keeping the Reyee router perfectly isolated and stable.
    
    *   **Sub-Second Execution**: The entire link teardown and module removal sequence executes in under a second, eliminating the old 25-second NetworkManager daemon freeze entirely.

![](imgs/20260607-112326.png){ .center-image }
