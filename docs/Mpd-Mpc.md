---
title: ncmpcpp++
icon: material/music
---

![](imgs/20250916-232438.png)

<div markdown="1" align="center">

# **[NCurses Music Player Client (Plus Plus)](https://rybczak.net/ncmpcpp/)**

</div>

<center><h1><b>ncmpcpp++</b></h1></center>

<kbd> <br> [<b>ncmpcpp++</b>](https://rybczak.net/ncmpcpp/) ↗️ <br> </kbd>

### This guide provides a step-by-step tutorial for setting up mpd, ncmpcpp, and mpc on Arch Linux for beginners. It covers installation, configuration, and basic usage. 
This video demonstrates installing mpd and ncmpcpp on Arch Linux:

<iframe width="560" height="315" src="https://www.youtube.com/embed/WzieM6Mqixs?si=NdL7oXlm-J8MFVMg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

[Installation of mpd and ncmpcpp](https://youtu.be/WzieM6Mqixs?si=6FKfrqzCgcB00M1p)

-----

### ncmpcpp + mpd + mpc step-by-step tutorial for someone who has never attempted setting this up in Arch Linux

Setting up `ncmpcpp`, `mpd`, and `mpc` on Arch Linux for the first time can seem a bit daunting, but it's a very rewarding experience for a minimalist, powerful music setup. `mpd` (Music Player Daemon) is the backend server that plays your music, `ncmpcpp` is a powerful terminal-based client for `mpd`, and `mpc` is a simple command-line client used for quick actions and scripting.

Here's a step-by-step tutorial:

**Prerequisites:**

  * **Arch Linux installed:** You should have a working Arch Linux installation.
  * **Basic terminal familiarity:** You'll be using the command line extensively.
  * **A directory for your music:** Make sure you have a place where your music files are stored (e.g., `~/Music`).

-----

### Step 1: Install MPD, ncmpcpp, and mpc

First, let's install the necessary packages. These are available in the official Arch Linux repositories.

```bash
sudo pacman -S mpd ncmpcpp mpc
```

**Video Resource:**
For a general installation overview on Arch-based systems, you might find this helpful:

  * [ArchMerge : 206 installation of mpd and ncmpcpp and how to use it](https://www.youtube.com/watch?v=WzieM6Mqixs) (Note: While titled for ArchMerge, the installation steps for MPD/ncmpcpp are largely similar for Arch Linux).

-----

### Step 2: Configure MPD (Music Player Daemon)

MPD needs to be configured to know where your music is, where to store its database, and how to output audio. It's generally recommended to run MPD as a user service.

1:  **Create MPD configuration directory and files:**
    It's good practice to keep MPD's configuration and related files in `~/.config/mpd/`.

```   
mkdir -p ~/.config/mpd/playlists
mkdir -p ~/.local/state/mpd  # Recommended for state_file
touch ~/.config/mpd/database
touch ~/.config/mpd/log
touch ~/.config/mpd/pid
touch ~/.config/mpd/state
touch ~/.config/mpd/sticker.sql
```
2:  **Copy the example configuration file:**
    MPD provides a good starting point for its configuration.
    
```
cp /usr/share/doc/mpd/mpdconf.example ~/.config/mpd/mpd.conf
```

3:  **Edit `mpd.conf`:**
    Open the copied configuration file with your favorite text editor (e.g., `nano`, `vim`):

```
nano ~/.config/mpd/mpd.conf
```

You'll need to modify or uncomment the following lines. Make sure to adjust paths to match your system.

*  **`music_directory`**: This is crucial. Point it to where your music files are.

```
music_directory "~/Music"
```

*Self-Correction:* If your music is on an external drive or in multiple locations, you can use symbolic links within your `music_directory` and ensure `follow_outside_symlinks` is set to `yes`.

 * **`playlist_directory`**: Where MPD will save your playlists.

```
playlist_directory "~/.config/mpd/playlists"
```

 * **`db_file`**: Path to the music database file.

```
db_file "~/.config/mpd/database"
```

 * **`log_file`**: Path to MPD's log file.

```
log_file "~/.config/mpd/log"
```

* **`pid_file`**: Path to the process ID file.

```
pid_file "~/.config/mpd/pid"
```

* **`state_file`**: Path to the file where MPD saves its state (e.g., current playlist, playback position).

```
state_file "~/.local/state/mpd/state"
```

* **`sticker_file`**: Path to the sticker database.

```
sticker_file "~/.config/mpd/sticker.sql"
```

* **`bind_to_address`**: Unless you want MPD to be accessible from other machines on your network, keep it local.

```
bind_to_address "localhost"
```

or

```
bind_to_address "127.0.0.1"
```

* **`port`**: The default is `6600`. You usually don't need to change this.

```
port "6600"
```

* **`auto_update`**: This is very useful. MPD will automatically update its database when changes are detected in your `music_directory`.

```
auto_update "yes"
```

* **`audio_output`**: This is where you configure how MPD outputs sound.

       * **PulseAudio (recommended for desktop users):**
 
```
            audio_output {
                type "pulse"
                name "My Pulse Audio"
            }
```
If you are using PulseAudio (which is common on modern Linux desktops), this is the simplest way.

   * **ALSA (Alternative):**
```
audio_output {
   type "alsa"
   name "My ALSA Output"
   # device "hw:0,0" # Uncomment and adjust if you have issues with default ALSA device
   # mixer_type "software" # Optional: Can help with volume control issues
            }
```
If you prefer ALSA directly, use this block.

  * **`restore_paused`**: If you want MPD to resume playback where you left off.

```
restore_paused "yes"
```

Save and close the `mpd.conf` file.



**Video Resource:**

   * For a deeper dive into MPD configuration and why certain settings are chosen, consider watching: [why I use music player daemon (mpd), + my config](https://www.youtube.com/watch?v=6EAID9yopIE) (This video provides a good conceptual overview, even if not exclusively Arch-focused for every command).
      * Another helpful guide on basic MPD setup on Arch: [Easy MPD (Arch Linux)](https://www.youtube.com/watch?v=wjW6nDhlEN8)

4:  **Start and Enable MPD as a user service:**
    This ensures MPD starts automatically when you log in.

    
    systemctl --user enable mpd.service
    systemctl --user start mpd.service
    

5:  **Update MPD's music database:**
    Now that MPD is running, tell it to scan your music directory.

    
    mpc update
    
This command can take some time if you have a large music collection.
You won't see much output until it's done.
        
Why I use music player daemon (mpd), + my config:
<iframe width="560" height="315" src="https://www.youtube.com/embed/6EAID9yopIE?si=gS0vrztqM9MSy4uT" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe> 


---
### Step 3: Configure ncmpcpp

`ncmpcpp` is the client you'll interact with most often. It has a rich set of features and is highly customizable.

1:  **Create ncmpcpp configuration directory and copy example config:**

```
mkdir -p ~/.config/ncmpcpp
cp /usr/share/doc/ncmpcpp/config ~/.config/ncmpcpp/config
```

2:  **Edit `ncmpcpp/config`:**
    Open the configuration file:

```
nano ~/.config/ncmpcpp/config
```

 At a minimum, ensure these lines match your MPD setup:

   * **`mpd_host`**: Should match your `mpd.conf`.

```
mpd_host = "localhost"
```

   * **`mpd_port`**: Should match your `mpd.conf`.

```
mpd_port = "6600"
```

   * **`mpd_music_dir`**: This path is important for ncmpcpp to correctly display file paths and enable features like the tag editor. It *must* match the `music_directory` you set in `mpd.conf`.

```
mpd_music_dir = "~/Music"
```

**Optional (but highly recommended) ncmpcpp customizations:**

   * **Visualizer:** To enable the audio visualizer (like a spectrum analyzer), you need to configure MPD to output audio data to a FIFO (named pipe) and then tell ncmpcpp to read from it.

       * **Edit `~/.config/mpd/mpd.conf` again:** Add this `audio_output` block *in addition* to your regular audio output (PulseAudio/ALSA):
          
```
            audio_output {
                type "fifo"
                name "my_fifo"
                path "/tmp/mpd.fifo"
                format "44100:16:2"
            }
```

##### Save and restart MPD:
            
```
systemctl --user restart mpd.service
```
Then, edit `~/.config/ncmpcpp/config`:

```
visualizer_data_source = "/tmp/mpd.fifo"
visualizer_output_name = "my_fifo"
visualizer_in_stereo = "yes"
visualizer_type = "spectrum" # Or "wave", "ellipse", "wave_filled"
visualizer_look = "+|" # Customize how the visualizer bars look
```

   * **Layout and Colors:** `ncmpcpp` is extremely customizable.<br>
Explore the `ncmpcpp/config` file for options like:

     * `song_list_format`: How songs are displayed in lists.
     * `now_playing_screen_artwork`: For displaying album art (requires additional setup like `coverart-mpd` or `mpd-cover` and `chafa`).
     * `colors_enabled`: Set to `yes` for colored interface.
     * `progressbar_look`: Customize the progress bar.
     * `lines_separator`: Visual separators.<br>
<br>
    Save and close the `ncmpcpp/config` file.
    
       
    **Video Resource:**

      * For visual examples of ncmpcpp customization and specific features like the visualizer: [How to configure mpd and ncmpcpp on Linux](https://computingforgeeks.com/how-to-configure-mpd-and-ncmpcpp-on-linux/) (This link is to an article that also contains a video walkthrough that covers customization including the visualizer.)


##### Easy MPD (Arch Linux)

<iframe width="560" height="315" src="https://www.youtube.com/embed/_GLOKTd-8tA?si=yr1LRI_6y3k_zf-P" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

-----

### Step 4: Using ncmpcpp and mpc

1.  **Start ncmpcpp:**
    Simply type `ncmpcpp` in your terminal:

    ```
    ncmpcpp
    ```

      * **Initial Database Scan:** If you just updated the MPD database, `ncmpcpp` might show a progress bar at the bottom indicating the database update. Once it's done, you should see your music library.<br>
      <br>
      * **Navigation:**
          * Press `F1` for a help screen with keybindings.
          * `1` to `8` (or `F1` to `F8`) switch between different views (playlist, browser, search, tag editor, etc.).
          * `u`: Update database.
          * `j`/`k` or arrow keys: Move up/down.
          * `spacebar`: Play/pause.
          * `s`: Stop.
          * `[`/`]`: Volume down/up.
          * `add` (or `a` in browser view): Add selected item to playlist.
          * `p`: Previous song.
          * `n`: Next song.
          * `q`: Quit ncmpcpp.
-----

2.  **Using mpc (MPD client):**
    `mpc` is a command-line tool for quick control over MPD.

      * **Play/Pause:**
        ```
        mpc toggle
        ```
      * **Next song:**
        ```
        mpc next
        ```
      * **Previous song:**
        ```
        mpc prev
        ```
      * **Set volume:**
        ```
        mpc volume 70 # Sets volume to 70%
        ```
      * **Show current song:**
        ```
        mpc current
        ```
      * **Update database:**
        ```
        mpc update
        ```
      * **List all commands:**
        ```
        mpc help
        ```
------

    **Video Resource:**

      * For controlling music playback using `mpc` and other tools, see: [Control music playback - sxhkd, ncmpcpp, mpc and mpd](https://www.youtube.com/watch?v=7CnQaVD67ko) (This video focuses on integrating `mpc` with keyboard shortcuts, which is a common use case).

#### Troubleshooting Tips.

  * **"Connection refused" error in `ncmpcpp`:**
      * Make sure <b>`mpd.service`</b> is running: <b>`systemctl --user status mpd.service`</b>.
      * Check your <b>`mpd_host`</b> and <b>`mpd_port`</b> in <b>`~/.config/ncmpcpp/config`</b> and <b>`mpd.conf`</b>. They must match.
      * Ensure no other process is using port <b>`6600`</b> (or whatever port you configured). You can check with <b>`ss -tunelp | grep 6600`</b>.
  * **No music appearing in `ncmpcpp`:**
      * Double-check your <b>`music_directory`</b> in <b>`~/.config/mpd/mpd.conf`</b>.
      * Make sure <b>`mpd.service`</b> has write permissions to the <b>`db_file`, `log_file`</b>, etc., and read permissions for your <b>`music_directory`</b>. Since you're running it as a user service, this is usually not an issue, but worth checking.
      * Run <b>`mpc update`</b> again.
  * **No sound:**
      * Verify your <b>`audio_output`</b> configuration in <b>`mpd.conf`</b>.
      * Ensure your sound system (PulseAudio/ALSA) is working correctly outside of MPD.
      * Check <b>`mpd`</b> logs: <b>`journalctl --user -u mpd.service`</b>.
  * **Visualizer not working:**
      * Did you add the `fifo` audio output block to <b>`mpd.conf`</b> *and* restart <b>`mpd.service`</b>?
      * Are the <b>`visualizer_data_source`</b> and <b>`visualizer_output_name`</b> correct in <b>`ncmpcpp/config`</b>?

-----

This step-by-step guide, now with integrated video resources, should get you up and running with <b>`mpd`, `ncmpcpp`</b>, and <b>`mpc`</b> on your Arch Linux system. Enjoy your music\!

---
#### Ncmpcpp: The Best MPD Client With The Worst Name

<iframe width="560" height="315" src="https://www.youtube.com/embed/KZM9efTQxTc?si=60bEM-8YeKC2ppLZ" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

---
#### Control mpd and ncmpcpp like a pro!

<iframe width="560" height="315" src="https://www.youtube.com/embed/7CnQaVD67ko?si=wNaDuLjZPnCreZR5" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>
