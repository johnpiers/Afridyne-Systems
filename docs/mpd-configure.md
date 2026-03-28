---
icon: material/music-circle-outline
---

<div style="display: none;">
  <h1>Header</h1>
</div>
![](imgs/20260102-150121.png){: .center-image}

<center><h2>MPD-configure</h2></center>

 [**README.md**](https://gitlab.com/sonida/mpd-configure/-/blob/master/README.md?ref_type=heads)

```
Layout: post.
Title: README for mpd-configure.
```

[**README for mpd-configure**](https://gitlab.com/sonida/mpd-configure#readme-for-mpd-configure)

The `mpd-configure` bash script creates a valid configuration file for [mpd](http://www.musicpd.org/ "Music Player Daemon (external website)"), optimised for bit perfect playback of any digital audio file, including those of high resolution.

With default settings the script uses the first available alsa audio interface by using its hardware address (in the form of `hw:x,y`), and has automagic procedures for things like the music directory and directory where files are stored, the number of items in the music direcory and the UPNP name. When multiple audio interfaces are found, the user is presented with a choice.

More information is available at the following pages:

- [audiophile-mpd](https://www.ap-linux.com/tag/mpd "mpd-configure: automatically turn Linux into an audiophile music player")
- [detect-alsa-output-capabilities](https://lacocina.nl/detect-alsa-output-capabilities "Alsa-capabilities shows which digital audio formats your USB DA-converter supports")

## [](https://gitlab.com/sonida/mpd-configure#basic-usage)Basic usage

### [](https://gitlab.com/sonida/mpd-configure#getting-the-script)Getting the script

The latest stable version of the script may be cloned from gitlab using `git`:

```
git clone https://gitlab.com/sonida/mpd-configure.git
```

Using git has the added benefit that updating the script to the latest version is as easy as:

```
## cd /path/to/git-clone
git pull
```

Alternatively, [the tarball of the current stable master](https://www.musicpd.org/download.html) can be downloaded and unpacked in the current directory using `wget` and `tar`:

```
wget https://www.musicpd.org/download/mpd/0.23/mpd-0.23.12.tar.xz | tar --strip-components=1 -zxf -
```

### [](https://gitlab.com/sonida/mpd-configure#running-the-script)Running the script

Run the script with default settings to display the contents of the resulting mpd configuration file:

```
bash mpd-configure
```

### [](https://gitlab.com/sonida/mpd-configure#storing-the-output-of-the-script-in-a-file)Storing the output of the script in a file

The output of the scripts can simply be redirected to a file (in this example `mympd.conf`):

```
bash mpd-configure > mympd.conf
```

Although the same may be achieved by using the `-o` or `--output` command line parameters or setting `CONF_MPD_CONFFILE` on the command line. This has the benefit that the script detects if the target file exists, in which case the user is prompted to overwrite it, while making an automated *backup* of the original file:

```
bash mpd-configure -o "mympd.conf"
# or:
CONF_MPD_CONFFILE="mympd.conf" ./mpd-configure
```

### [](https://gitlab.com/sonida/mpd-configure#more-advanced-usage-example)More advanced usage example

Additional setting are available using environment variables or using the file [`./mpd-configure.conf`](https://gitlab.com/sonida/mpd-configure/-/blob/master/mpd-configure.conf) and configuration snippet files in the [`./confs-available/`](https://gitlab.com/sonida/mpd-configure/-/tree/master/confs-available) directory.

For example to specify `CONF_MPD_MUSICDIR` which sets the `music_directory` and saving the resulting mpd configuration file in `mympd.conf`, use:

```
CONF_MPD_MUSICDIR="/srv/media/music" ./mpd-configure -o "/etc/mpd.conf"
```

By default `mpd-configure` prompts the user to overwrite the specified file if it exists, and makes a backup of it.

### [](https://gitlab.com/sonida/mpd-configure#fully-automated-usage-example)Fully automated usage example

A fully automated example which does not prompt the user (`-n`), uses the first available USB Audio Class interface (`-l u`) and sets some paths, while creating a backup of the original `/etc/mpd.conf` in case it exists:

```
CONF_MPD_MUSICDIR="/srv/media/music" CONF_MPD_HOMEDIR="/var/lib/mpd" \
bash mpd-configure -l u -n -o "/etc/mpd.conf"
```

To see all available command line options run the script with `-h` or `--help`:

```
bash mpd-configure -h
```

Also see

- [Detailed usage instructions](https://gitlab.com/sonida/mpd-configure#detailed-usage-instructions) for more information on the usage and available settings.
- [Usage a as systemd service](https://gitlab.com/sonida/mpd-configure#usage-a-as-systemd-service)

## [](https://gitlab.com/sonida/mpd-configure#about-the-alsa-capabilities-helper-script)About the alsa-capabilities helper script

[`mpd-configure`](https://gitlab.com/sonida/mpd-configure/-/blob/master/mpd-configure) relies on the accompanying bash script [`alsa-capabilities`](https://gitlab.com/sonida/alsa-capabilities) for getting information about the available audio output interfaces from alsa.

## [](https://gitlab.com/sonida/mpd-configure#about-the-mpd-monitor-helper-script)About the mpd-monitor helper script

The `mpd-monitor` script in this project is replaced by a separate project on gitlab.

See: [mpd-monitor](https://gitlab.com/ronalde/mpd-monitor/)

## [](https://gitlab.com/sonida/mpd-configure#background)Background

Music Player Daemon (MPD) is a flexible, powerful, server-side application for playing music. Through plugins and libraries it can play a variety of sound files while being controlled by its network protocol. See the article. [How to turn Music Player Daemon (mpd) into an audiophile music player](https://mpd.readthedocs.io/en/stable/user.html#).

It does this by creating a proper formatted `audio_output` configuration snippet for mpd's [alsa audio output plugin](http://www.musicpd.org/doc/user/config_audio_outputs.html) using the sound cards hardware address and turning all options off which might cause mpd to alter the incoming sound. For example:

```
## start processing `01_output-audio-alsa.conf'
audio_output {
        type             "alsa"
        name             "Peachtree 24/192 USB X - USB Audio"
        device           "hw:1,0"
        auto_resample    "no"
        auto_format      "no"
        auto_channels    "no"
}
replaygain                 "off"
mixer_type                 "none"
## done processing
```

## [](https://gitlab.com/sonida/mpd-configure#detailed-usage-instructions)Detailed usage instructions

After creating a mpd configuration file, `mpd` can be told to use this configuration file with:

```
    mpd ./mpd.conf
```

To use the generated configuration file system wide, it can be copied to the system wide mpd configuration file when you want to run `mpd` as a system daemon:

```
    sudo bash mpd-configure -o "/etc/mpd.conf"
    sudo systemctl restart mpd
```

## [](https://gitlab.com/sonida/mpd-configure#more-complex-usage)More complex usage

For debugging or testing purposes one may set the `INCLUDE_COMMENTS` and/or `DEBUG` parameters through the `mpd-configure.conf` file or on the command line, eg:

```
    DEBUG="True" INCLUDE_COMMENTS="True" bash mpd-configure
```

In dynamic environments in which hardware may be altered each boot, connected to whatever USB DAC, the script could be put in a logon script or systemd service file.

## [](https://gitlab.com/sonida/mpd-configure#usage-a-as-systemd-service)Usage a as systemd service

The script is fast and stable enough to function as a systemd service. By setting `Before=mpd.service` and `Wants=mpd.service` in the service file systemd makes sure mpd-configure is run before mpd is started, and tries to start mpd.

- See: [./examples/systemd_mpd-configure.service](https://gitlab.com/sonida/mpd-configure/-/blob/master/examples/systemd_mpd-configure.service)

### [](https://gitlab.com/sonida/mpd-configure#usage-from-within-another-bash-or-sh-script)Usage from within another bash or sh script

The bash script [./examples/bash-example.sh](https://gitlab.com/sonida/mpd-configure/-/blob/master/examples/bash-example.sh) demonstrates the way alsa-capabilities can be used from another bash script.

This demo script returns the monitoring file of the file specified as an argument:

```
bash examples/bash-example.sh hw:1,0
```

Result:

```
the audio card with alsa hardware address hw:1,0 can be monitored with:
/proc/asound/card1/stream0
```

### [](https://gitlab.com/sonida/mpd-configure#usage-from-within-python)Usage from within python

Assuming your in the `mpd-configure` directory, run:

```
    python examples/get-interfaces.py
```

The python script [./examples/get-interfaces.py](https://gitlab.com/sonida/mpd-configure/-/blob/master/examples/get-interfaces.py) uses a helper bash script ([./examples/get-interfaces-for-python.sh](https://gitlab.com/sonida/mpd-configure/-/blob/master/examples/get-interfaces-for-python.sh)), which in turn sources `alsa-capabilities`.

### [](https://gitlab.com/sonida/mpd-configure#ltsp-specific-auto-logon-sample)LTSP-specific auto logon sample

For my LTPS-environments the script directory can be copied to the home directory of the auto logon user specified in `/var/lib/tftpboot/ltsp/i386/lts.conf`. It's `~/.profile` should be edited to run the script and start `mpd` using the script generated `~/.mpd/mpd.conf`, ie:

```
    systemctl stop mpd && \
    CONF_MPD_MUSICDIR="/srv/media/music" CONF_MPD_HOMEDIR="/var/lib/mpd" \
    bash ~/mpd-configure/mpd-configure -l usb -n -q --nobackup -o "~/.mpd/mpd.conf"  && \
    systemctl start mpd
```

## [](https://gitlab.com/sonida/mpd-configure#preferences)Preferences

Preferences can be set in the file `mpd-configure.conf`. By default all preferences are commented out.

The script uses configuration file snippets in the [`./confs-available/`](https://gitlab.com/sonida/mpd-configure/-/tree/master/confs-available) directory. By symlinking them to the [`./confs-enabled/`](https://gitlab.com/sonida/mpd-configure/-/tree/master/confs-enabled) directory, they will be included by `mpd-configure` in the resulting mpd configuration file. Any bash variable in those configuration snippets, will be expanded to their calculated values by the script.

### [](https://gitlab.com/sonida/mpd-configure#general-environment-variables)General environment variables

`DEBUG` Output values of variables and program flow to std_err for easier debugging. Possible values:

- commented out: disabled (Default).
- `1` (or non-empty): enabled.

`INCLUDE_COMMENTS` Include commented and empty lines from configuration snippet files in the generated mpd configuration file:

- commentend out: disabled (Default).
- `1` (or non-empty): enabled

`CONF_MPD_CONFFILE` Path to where the generated mpd configuration file will be written. Possible values:

- commented out: don't write to a file (Default). One may redirect the output of the script using:
  
  bash mpd-configure > /path/to/mpd.conf
  
- `/path/to/mpd.conf`: use the path specified.
  

### [](https://gitlab.com/sonida/mpd-configure#alsa-and-sound)Alsa and sound

`LIMIT_INTERFACE_TYPE` A keyword which limits the type of alsa interfaces to be returned:

Possible values:

- `usb`, `digital` or `analog`
- Comment it out (or leave it empty) to prevent filtering.

Default value:

- commented out (or empty ""): do not limit the interfaces that will be found.

`LIMIT_INTERFACE_FILTER` The available output devices (after filtering with `LIMIT_INTERFACE_TYPE` when applicable) may be further limited using a regular expression (which thus is case sensentive) which should match the output of:

```
LANG=C aplay -l | grep ^card
```

If for example the output is like this:

```
card 0: MID [HDA Intel MID], device 0: HDMI 0 [HDMI 0]
card 1: receiv [Pink Faun USB 32/384 USB receiv], device 0: USB Audio [USB Audio]
```

... you could use one of the following values to match the *second* line (which in this example matches the alsa `hw:1,1` interface, eg. the second interface of the second sound card):

```
"USB Audio"
"[uU][sS][bB] \w+ "
```

but not

```
"USB audio"
```

Possible values:

- empty or commented out: no filtering is applied
- `Some regular expression`: use the (first) interface which matches the regexp.

Default value:

- commented out (or empty ""): use the first available interface.

Handling of pulseaudio `OPT_DISABLE_PULSEAUDIO` Disable pulseaudio by modifyin the current users' `~/.pulseaudio/client.conf`

Possible values:

- non-empty (`1` or "True") disables pulseaudio.
- Comment it out (or leave it empty) to prevent disabling of pulseaudio.

Default value:

- commented out (or empty ""): do not disable it.

`OPT_STOP_PULSEAUDIO` Temporary disable and stop pulseaudio during detection of alsa interfaces. After the script pulseaudio's client configuration and run state will restored.

Possible values:

- non-empty (`1` or "True") temporary disables and stops pulseaudio.
- Comment it out (or leave it empty) to prevent temporary disabling and stopping of pulseaudio.

Default value:

- commented out (or empty ""): do not disable it.

See the configuration snippet files and accompanying `README` in `./confs-available` for additional parameters and and explanation for their functions.

## [](https://gitlab.com/sonida/mpd-configure#reference)Reference for both MPD/LTSP.

MPD specific:

- [How to turn Music Player Daemon (mpd) into an audiophile music player](https://ideatrash.net/2020/06/weekend-project-whole-house-and-streaming-audio-for-free-with-mpd.html).
- [What digital audio format does your USB DA-converter support and use?](https://forum.manjaro.org/t/howto-set-up-a-hi-res-audiophile-usb-dac-cambridge-audio/80724)
- [Music Player Daemon (MPD)](http://www.musicpd.org/)

LTSP specific:

- [How to setup a bit-perfect digital audio streaming client with free software (with LTSP and MPD)](https://blog.desdelinux.net/en/music-player-daemon-simple-configuration-and-some-extra-uses/)
- [Linux Terminal Server Project (LTSP)](http://www.ltsp.org/)