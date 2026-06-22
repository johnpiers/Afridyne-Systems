---
icon: material/music-circle-outline
---

<div style="display: none;">
  <h1>Header</h1>
</div>

![](imgs/20251231-210314.png){: .center-image}

<div style="display: flex; justify-content: center;">
  <h2><a href="https://wiki.archlinux.org/title/Music_Player_Daemon/"><b>Music Player Daemon</b></a></h2>
</div>

**[MPD](https://www.musicpd.org/)** (music player daemon) is an audio player that has a server-client architecture. It plays audio files, organizes playlists and maintains a music database, all while using very few resources. In order to interface with it, a separate [client](https://wiki.archlinux.org/title/Music_Player_Daemon#Clients) is needed.

## Installation

[Install](https://wiki.archlinux.org/title/Install "Install") the [mpd](https://archlinux.org/packages/?name=mpd) package, or [mpd-git](https://aur.archlinux.org/packages/mpd-git/) AUR for the development version.

## Configuration

MPD is able to run in [#Per-user configuration](https://wiki.archlinux.org/title/Music_Player_Daemon#Per-user_configuration) or [#System-wide configuration](https://wiki.archlinux.org/title/Music_Player_Daemon#System-wide_configuration) mode (settings apply to all users). Also it is possible to run multiple instances of MPD in a [#Multi-MPD setup](https://wiki.archlinux.org/title/Music_Player_Daemon#Multi-MPD_setup). The way of setting up MPD depends on the way it is intended to be used: a local per-user configuration is easier to set up and may prove more adapted on a desktop system. The system-wide setup might be better suited for a always-on audio server with multiple users but a shared MPD instance.

In order for MPD to be able to playback audio, [ALSA](https://wiki.archlinux.org/title/ALSA "ALSA"), optionally with [PulseAudio](https://wiki.archlinux.org/title/PulseAudio "PulseAudio") or [PipeWire](https://wiki.archlinux.org/title/PipeWire "PipeWire"), must be set up and working. The [#Audio configuration](https://wiki.archlinux.org/title/Music_Player_Daemon#Audio_configuration) section thereafter describes the parameters needed for *ALSA*, *PulseAudio* or *PipeWire*.

MPD is configured in the file [mpd.conf(5)](https://man.archlinux.org/man/mpd.conf.5) which can be located in various paths depending on the setup chosen (system-wide or per-user). In short, the two common locations used are:

1. `~/.config/mpd/mpd.conf` in per-user configuration mode, this is the first location searched,
2. `/etc/mpd.conf` in system-wide configuration.

These are some of the most commonly used configuration options:

- `pid_file` - The file where MPD stores its process ID
- `db_file` - The music database
- `state_file` - MPD's current state is noted here
- `playlist_directory` - The directory where playlists are saved into
- `music_directory` - The directory that MPD scans for music
- `sticker_file` - The sticker database

###### Per-user configuration

MPD can be configured per-user. Running it as a normal user has the benefits of:

- Regrouping into one single directory `~/.config/mpd/` (or any other directory under `$HOME`) all the MPD configuration files.
- Avoiding unforeseen directory and file permission errors.

###### Configure the location of files and directories

In user mode, the configuration is read from `$XDG_CONFIG_HOME/mpd/mpd.conf`. We will assume here `$XDG_CONFIG_HOME` equals the [default](https://specifications.freedesktop.org/basedir-spec/latest/) of `~/.config`.

To build the user configuration, the [MPD configuration example](https://raw.githubusercontent.com/MusicPlayerDaemon/MPD/master/doc/mpdconf.example) included in the package is a good starting point, copy it using the following lines:

*$ mkdir -p ~/.config/mpd*

*$ cp /usr/share/doc/mpd/mpdconf.example ~/.config/mpd/mpd.conf*

A good practice is to use this newly created `~/.config/mpd/` directory to store, together with the configuration file, other MPD related files like the database or the playlists. The user must have read write access to this directory.

Then edit the configuration file in order to specify the required and optional files and directories:

*~/.config/mpd/mpd.conf*

###### Recommended location for database

db_file "~/.config/mpd/database"

###### If running mpd using systemd, delete this line to log directly to systemd.

log_file "syslog"

###### The music directory is by default the XDG directory, uncomment to amend and choose a different directory

music_directory "~/music"

###### Uncomment to refresh the database whenever files in the music_directory are changed

auto_update "yes"

###### Uncomment to enable the functionalities

`playlist_directory "~/.config/mpd/playlists"`

`pid_file "~/.config/mpd/pid"`

`state_file "~/.local/state/mpd/state"`

`sticker_file "~/.config/mpd/sticker.sql"`

###### If playlists are enabled in the configuration, the specified playlist directory must be created:

`$ mkdir ~/.config/mpd/playlists`

###### If `state_file` is set, the specified directory must be created:

`$ mkdir -p ~/.local/state/mpd`

###### MPD can now be started (an optional custom location for the configuration file can be specified):

`$ mpd *[config_file]*`

In order to build the database file, MPD must scan into the `music_directory` defined above. To request this task, one of the MPD [clients](https://wiki.archlinux.org/title/Music_Player_Daemon#Clients) must be used. For example with *mpc* the command is:

`$ mpc update`

or alternatively one can set the option `auto_update` to `"yes"` in the configuration to refresh the database whenever files are changed in `music_directory`.

###### Audio configuration

If [ALSA](https://wiki.archlinux.org/title/ALSA "ALSA") is used, **autodetection** of the default device should work out of the box without any particular setting. If not, the syntax for ALSA audio output definition is provided thereafter; the required `name` parameter specifies a unique name for the audio output. The exact device as displayed using `aplay --list-pcm` from the package [alsa-utils](https://archlinux.org/packages/?name=alsa-utils) can optionally be indicated with the `device` option.

~/.config/mpd/mpd.conf

`audio_output {
 type "alsa"
 name "*ALSA sound card*"
 # Optional
 #device "*iec958:CARD=Intel,DEV=0*"
 #mixer_control "PCM"
}`

**Users of [PulseAudio](https://wiki.archlinux.org/title/PulseAudio "PulseAudio") will need to make the following modification:**

`~/.config/mpd/mpd.conf`

`audio_output {
 type "pulse"
 name "*pulse audio*"
}`

**Output with [PipeWire](https://wiki.archlinux.org/title/PipeWire "PipeWire") can also be configured:**

`~/.config/mpd/mpd.conf`

`audio_output {
 type "pipewire"
 name "*PipeWire Sound Server*"
}`

#### Autostart with systemd

The [mpd](https://archlinux.org/packages/?name=mpd) package provides a [user service](https://wiki.archlinux.org/title/Systemd/User "Systemd/User") file. The service starts the process as user, there is no need to change permission nor use the `user` and `group` variables in the MPD configuration file.

[Start/enable](https://wiki.archlinux.org/title/Start/enable "Start/enable") the user unit `mpd.service` (i.e. with the `--user` flag).

**Note:** The configuration file is read from `~/.config/mpd/mpd.conf`, see [systemd#Editing provided units](https://wiki.archlinux.org/title/Systemd#Editing_provided_units "Systemd") if you would like to indicate a custom configuration file path.

###### Autostart on tty login

To start MPD on login add the following to `~/.profile` or another [autostart file](https://wiki.archlinux.org/title/Autostarting "Autostarting"):

###### MPD daemon start (***if no other user instance exists***)

[ ! -s ~/.config/mpd/pid ] && mpd

#### Scripted configuration

The [mpd-configure](https://gitlab.com/sonida/mpd-configure) tool creates a MPD configuration optimized for [bit perfect](https://www.musicpd.org/doc/user/advanced_usage.html#bit_perfect) audio playback, without any resampling or conversion, using the ALSA interface hardware address (hw:x,y).

### System-wide configuration

**Note:** Users of PulseAudio with a system-wide MPD configuration have to implement a [workaround](https://wiki.archlinux.org/title/Music_Player_Daemon/Tips_and_tricks#Local_(with_separate_mpd_user) "Music Player Daemon/Tips and tricks") in order to run MPD as its own user!

The default `/etc/mpd.conf` keeps the setup in `/var/lib/mpd` which is assigned to user as well as primary group MPD.

#### Music directory

The music directory is defined by the option `music_directory` in the configuration file `/etc/mpd.conf`.

MPD needs to have execute permission on *all* parent directories of the music collection and also read access to all directories containing music files. This may conflict with the default configuration of the user directory, like `~/Music`, where the music is stored.

While there are several solutions to this issue, one of these should be most practical:

- Switch to the [#Per-user configuration](https://wiki.archlinux.org/title/Music_Player_Daemon#Per-user_configuration) mode instead
- Add the `mpd` user to the user's group and grant group execute permission to the user directory. This way the `mpd` user has permission to open the user directory:

#### gpasswd -a mpd *user_group_name*

`$ chmod 710 /home/user_directory`

- Store the music collection in a different path, either:
  - By moving it entirely,
  - With a bind mount,
  - Or with [Btrfs#Subvolumes](https://wiki.archlinux.org/title/Btrfs#Subvolumes "Btrfs") (you should make this change persistent with an entry to `/etc/fstab` ).

The MPD configuration file must define only one music directory. If the music collection is contained under multiple directories, create symbolic links under the main music directory in `/var/lib/mpd`. Remember to set permissions accordingly on the directories being linked.

To exclude a file - or files - from the update, create a file called `.mpdignore` in its parent directory. Each line of that file may contain a list of shell wildcards. Matching files in the current directory and all subdirectories are then excluded from subsequent updates.

**Note:** MPD is capable of reading music files within some archive file formats, and will add those during an update if they are in the music directory; tar is known to be an exception.

#### Start with systemd

MPD can be controlled with `mpd.service` [using systemd](https://wiki.archlinux.org/title/Systemd#Using_units "Systemd"). The first startup can take some time as MPD will scan your music directory.

Test everything by starting a client application ([ncmpc](https://archlinux.org/packages/?name=ncmpc) is a light and easy to use client), and play some music!

##### Socket activation

[mpd](https://archlinux.org/packages/?name=mpd) provides a `mpd.socket` unit. If `mpd.socket` is enabled (and `mpd.service` is disabled), systemd will not start MPD immediately, it will just listen to the appropriate sockets. Then, whenever an MPD client attempts to connect to one of these sockets, systemd will start `mpd.service` and transparently hand over control of these ports to the MPD process.

If you prefer to listen to different UNIX sockets or network ports (even multiple sockets of each type), or if you prefer not to listen to network ports at all, [edit](https://wiki.archlinux.org/title/Edit "Edit") the `mpd.socket` unit appropriately **and** modify `/etc/mpd.conf` to match the configuration (see [mpd.conf(5)](https://man.archlinux.org/man/mpd.conf.5) for details).

#### User id startup workflow

MPD should never run as *root*; you may use the `user` option in the configuration to make MPD change its user id after initialization. Do not use this option if you start MPD as an unprivileged user. To describe how MPD drops its superuser privileges and switch to those of the user set in the configuration, the steps of a normal MPD startup are listed thereafter:

1. Since MPD is started as *root* by systemd, it first reads the `/etc/mpd.conf` file.
2. MPD reads the `user` variable in the configuration, and changes from *root* to this user.
3. MPD then reads the rest of the configuration file and configures itself accordingly. Uses of `~` in the configuration file points to the home user's directory, and not root's directory.

### Multi-MPD setup

#### Running an Icecast server

For a second MPD (e.g. with [Icecast](https://wiki.archlinux.org/title/Icecast "Icecast") output to share music over the network) using the same music and playlist as the one above, simply copy the above configuration file and make a new file (e.g., `/home/username/.mpd/config-icecast`), and only change the `log_file`, `error_file`, `pid_file`, and `state_file` parameters (e.g. `mpd-icecast.log`, `mpd-icecast.error`, and so on). Using the same directory paths for the music and playlist directories would ensure that this second MPD uses the same music collection as the first one, e.g. creating and editing a playlist under the first daemon would affect the second daemon as well. Users do not have to create the same playlists all over again for the second daemon. Call this second daemon the same way from `~/.xinitrc` above - but be sure to have a different port number, avoiding a conflict with the first MPD daemon.

#### Satellite setup

The method described in [#Running an Icecast server](https://wiki.archlinux.org/title/Music_Player_Daemon#Running_an_Icecast_server) works, but at least in theory could lead to issues with the database, when both MPD instances try to write to the same database file concurrently. MPD has a [satellite mode](https://www.musicpd.org/doc/user/advanced_config.html#satellite) where one instance can receive the database from an already running MPD instance.

In your `config-icecast` add this, where host and port reflect your primary MPD server:

`database {
 plugin "proxy"
 host "localhost"
 port "6600"
}`
