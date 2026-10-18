---
title: ncmpcpp Rybczak
icon: material/music
---
![](imgs/20250916-232438.png)

<div markdown="1" align="center">

# **[NCurses Music Player Client (Plus Plus)](https://rybczak.net/ncmpcpp/)**

</div>

<center><h1><b>ncmpcpp++</b></h1></center>

<kbd> <br> [<b>ncmpcpp++</b>](https://rybczak.net/ncmpcpp/) ↗️ <br> </kbd>

**Main Features:**

<div class="grid cards cols-3" markdown>

-   <span style="color: #2094f3">:material-palette:</span> **Tag-Editor**
    [:octicons-arrow-right-24: View Guide](#tag-editor){ .md-button style="border-color: #2094f3; color: #2094f3" }
    
    Get your music files looking professional.

-   <span style="color: #2094f3">:material-format-font:</span> **Playlist-Editor**
    [:octicons-arrow-right-24: View Guide](#playlist-editor){ .md-button style="border-color: #2094f3; color: #2094f3" }
    
    As the name implies edit and change to your hearts content.

-   <span style="color: #2094f3">:material-translate:</span> **Search-Engine**
    [:octicons-arrow-right-24: View Guide](#search-engine){ .md-button style="border-color: #2094f3; color: #2094f3" }
    
    Search for what you need, to play, edit or change.

-   <span style="color: #00e5ff">:material-emoticon-happy-outline:</span> **Media-Library**
    [:octicons-arrow-right-24: View Guide](#media-library){{ .md-button style="border-color: #00e5ff; color: #00e5ff" }
    
    Switch between two/three columns mode and more.

-   <span style="color: #00e5ff">:material-shield-check:</span> **Movement**
    [:octicons-arrow-right-24: View Guide](#movement){ .md-button style="border-color: #00e5ff; color: #00e5ff" }
    
    Show music visualizer (8).

-   <span style="color: #00e5ff">:material-compass:</span> **last.fm**
    [:octicons-arrow-right-24: Go To Site](http://last.fm/){ .md-button style="border-color: #00e5ff; color: #00e5ff" }
    
    Ability to fetch artist info from last.fm.

-   <span style="color: #4caf50">:material-magnify:</span> **Display Mode**
    [:octicons-arrow-right-24: View Guide](#global){ .md-button style="border-color: #4caf50; color: #4caf50" }
    
    New Display Mode, Toggle display mode.
    
-   <span style="color: #4caf50">:material-chart-bar:</span> **User Interface**
    [:octicons-arrow-right-24: View Guide](#alternative-interfaces-and-modes){ .md-button style="border-color: #4caf50; color: #4caf50" }
    
    Alternative User Interface, Toggle user interface.

-   <span style="color: #4caf50">:material-page-layout-header:</span> **Browse**
    [:octicons-arrow-right-24: View Guide](#browser){ .md-button style="border-color: #4caf50; color: #4caf50" }
    
    Ability to browse, add files from outside of MPD music dir.

</div>

!!! desc "Main Features"

    Main Features:
    
    - [Tag Editor](#tag-editor)
    - [Playlist Editor](#playlist-editor)
    - [Easy to use Search Engine](#search-engine)
    - [Media Library](#media-library_1)
    - [Music Visualizer](#movement)
    - Ability to fetch artist info from <a href="http://last.fm">last.fm</a></li>
    - [New Display Mode](#global)
    - [Alternative User Interface](#alternative-interfaces-and-modes)
    - Ability to browse and [add files from outside](#browse-outside-the-mpd-music-directory) of the MPD music directory.
    
    …and a lot more minor functions.
    
    
    !!! recommendation "Dependencies"
    
        Dependencies:
        
        <ul>
        
        <li><a href="http://www.boost.org">Boost Library</a></li>
        <li><a href="http://www.gnu.org/software/ncurses/ncurses.html">ncurses library</a></li>
        <li><a href="https://tiswww.case.edu/php/chet/readline/rltop.html">Readline library</a></li>
        <li><a href="http://curl.haxx.se/">curl library</a> (For fetching lyrics and last.fm data)</li>
        <li><a href="http://www.fftw.org/">fftw library</a> (Optional, required for frequency spectrum music visualization mode)</li>
        <li><a href="http://developer.kde.org/~wheeler/taglib.html">Tag library</a> (Optional, required for tag editing)</li>
        
        </ul>
        

### Stable Version:

!!! ex "Stable Version"

    Most of the popular Linux/*BSD distributions have ncmpcpp in their repositories, so it can be easily installed with your package manager.
    
    Alternatively, you can download the latest stable version here and compile and install it manually (`Note:`{.red} that if you’re using a binary distribution such as Ubuntu, you will need to install several *-dev packages for the compilation step). After you’ve downloaded and unpacked the code, run ./configure in the main directory (./configure --help to inspect available configuration options) and when it passes, make and make install.
    
    After you’re done with the installation, grab default configuration and bindings, tailor them to suit your needs and have fun!
    
    !!! tip "NOTE:"
    
        After you start the application, press F1 to switch to help screen that lists all the available actions along with their key bindings.
        
### Development Version:

!!! version-added "Development Version"

    If you like to get the newest features quickly or you would like to contribute to ncmpcpp, you should get live development version from the git repository. It’s usually pretty stable, although may be a little rough around the edges.
    
    [Ncmpcpp](https://rybczak.net/ncmpcpp) is an [mpd](https://wiki.archlinux.org/title/Mpd "Mpd") client (compatible with [mopidy](https://mopidy.com/)) with a UI very similar to *ncmpc*, but it provides new useful features such as support for regular expressions for library searches, extended song format, items filtering, the ability to sort playlists, and a local filesystem browser.
    
    To use it, a functional *mpd* must be present on the system since *ncmpcpp*/*mpd* work together in a client/server relationship.
    
### Installation:

!!! instruction "Installation"

    [Install](https://wiki.archlinux.org/title/Ncmpcpp#Installation) the [ncmpcpp](https://archlinux.org/packages/extra/x86_64/ncmpcpp/) package.
    
### Basic Configuration:

!!! desc "Basic Configuration"
    The main repository is at https://github.com/arybczak/ncmpcpp. Alternatively you can use one of the mirrors: [repo.or.cz/ncmpcpp.git](http://repo.or.cz/ncmpcpp.git) found at [repo.or.cz](https://repo.or.cz/). | [Git HomePage](https://git-scm.com/)
    
    The steps to install are the same as for the stable version with the exception of having to generate configuration scripts by running ./autogen.sh in the main directory.
    
    The shell "GUI" for *ncmpcpp* is highly customizable. Edit `$XDG_CONFIG_HOME/ncmpcpp/config` to your liking. If, after installation, `$XDG_CONFIG_HOME/ncmpcpp/config` has not been created, simply copy the sample config, [change owner](https://wiki.archlinux.org/title/File_permissions_and_attributes#Changing_ownership "File permissions and attributes") and edit at the very least the following three configuration options:
    
    - **mpd_host** - Should point to the host on which *mpd* resides, can be "localhost", "127.0.0.1" or "::1" if on the same machine. To connect with a password, write "*password*@*host*"
    - **mpd_port** - The default of *mpd* should be "6600"
    - **mpd_music_dir** - The same directory value as specified in "music_directory" in `mpd.conf`
    
    For inspiration, see the following resources:
    
    - Sample configuration file in `/usr/share/doc/ncmpcpp/config`.
    - [Show your .ncmpcpp/config with screenshot forum thread](https://bbs.archlinux.org/viewtopic.php?id=66488)

### Enabling Visualization:

!!! abstract "Enabling Visualization"
    For visualization, add a few lines to `/etc/mpd.conf` or `~/.config/mpd/mpd.conf` to enable the generation of the [fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform "wikipedia:Fast Fourier transform") data for the visualization:
    
    ```zsh
    audio_output {
        type "fifo"
        name "my_fifo"
        path "/tmp/mpd.fifo"
        format "44100:16:2"
    }
    ```
    
    **Note:** You may need to add an `audio_output` section for the normal audio output. See [Music Player Daemon#Audio configuration](https://wiki.archlinux.org/title/Music_Player_Daemon#Audio_configuration "Music Player Daemon") for details.
    
    Additional lines need to be added to `$XDG_CONFIG_HOME/ncmpcpp/config`
    
    ```zsh
    visualizer_data_source = "/tmp/mpd.fifo"
    visualizer_output_name = "my_fifo"
    visualizer_in_stereo = "yes"
    visualizer_type = "spectrum"
    visualizer_look = "+|"
    ```
    
    - **visualizer_type** - Set the visualization to either a `spectrum`/`ellipse`/`wave_filled` analyzer or `wave` form.
    - **visualizer_look** - Set the visualizer's look (string has to be exactly 2 characters long: first one is for wave and whereas second for frequency spectrum, wave_filled and ellipse).
    
    **Note:** If you experience synchronization issues, change the `buffer_time` in your `mpd` configuration to [100000 or less](https://github.com/ncmpcpp/ncmpcpp/blob/master/doc/config).
    
    If you use [mopidy](https://docs.mopidy.com/en/latest/installation/arch/), visualization is handled via [gstreamer's udpsink](https://github.com/ncmpcpp/ncmpcpp/commit/fb886f687014e22b2fe1477da855be5201063ea8). Edit the `output` in the `[audio]` block of your `mopidy.conf`:
    
    ```zsh
    output = tee name=t ! queue ! autoaudiosink t. ! queue ! audio/x-raw,rate=44100,channels=2,format=S16LE ! udpsink host=localhost port=5555
    ```
    
    This forwards the audio data to port `5555`. For `ncmpcpp` to read from this port, change its `visualizer_data_source` accordingly:
    
    ```zsh
    visualizer_data_source = "localhost:5555"
    ```
    
##Tips and Tricks.

### Browse Outside the MPD Music Directory

!!! desc "How to Browse Outside the MPD Music Directory"

    1. Use the Filesystem Browser Tab (1 or 2):
        • By default, pressing 1 or 2 (depending on your layout/tab setup) switches you to the browser view.
        • If you press the browse tab key twice (or navigate to the local filesystem view), ncmpcpp can display the local filesystem.
        • Note: Adding files from completely outside the MPD music_directory requires MPD to either recognize them via symbolic links or accept them if they fall under MPD's permitted paths/stream/IPC capabilities.
        
    2. Using Symbolic Links (Recommended Workaround):
        • MPD natively indexes only what is inside its music_directory unless you place symbolic links inside that directory pointing to external folders on your drive or external mounts.
        • Ensure that your mpd.conf has follow_symlinks "yes" enabled so MPD follows and indexes those external paths.
        
    3. Direct Add via mpc or CLI:
        • If a file is completely outside MPD's reach and cannot be added to the database directly, you can load individual files or use mpc add with file paths or URIs if MPD's configuration permits.
        
###Remapping Keys:

!!! abstract "Tip"

    * A listing of _Key Bindings_ and their respective functions are available from within npmpcpp itself via hitting `F1`.

    * Users may remap any of the default keys by simply copying <b>`/usr/share/doc/ncmpcpp/bindings`</b> to <b>`$XDG_CONFIG_HOME/ncmpcpp/`</b> and editing it.
    

### Autoset Tags from Filename and vice versa

!!! education "Autoset Tags from Filename and `vice versa`"
    In the Tag Editor you can select a directory with music and then select the `Filename` option in the middle section. This opens a little window with two options: `Get Tags from Filename` and `Rename files`. If you choose `Get Tags From Filename`, a popup with two windows is shown. On the left side you can enter a pattern that extracts the selected information from the filenames. You can also hit `Preview` to see what the result would look like. On the right side you can see the legend containing all the possible keywords to be used for extraction.
    
    A simple Example would be the pattern: `%a - %t`. If your files are named according to this pattern (Artist - Title) then this pattern would extract this information and set the Tags for the File.
    
    The other option `Rename Files` does the exact opposite. It takes the Tags from the audio files and creates a Filename from them.

###Notification on Song Change:

!!! tip "Notification on Song Change:"
    *notify-send* can be used in the `execute_on_song_change` command to generate notifications whenever the song changes (and upon application launch). This is contingent upon having a [Desktop Notification Server installed and configured](https://wiki.archlinux.org/title/Desktop_notifications).

### Notify-Send

!!! info "Notify-Send"
    As an example:
    
    ```zsh
    execute_on_song_change = notify-send "Now Playing" "\$(mpc --format '%title% \n%artist% - %album%' current)"
    ```

### With Album Art:

!!! education "With Album Art:"
    If you want song change notifications to have the album art of the currently playing song, you can use this script. Album art previews will be stored in `$XDG_CONFIG_HOME/ncmpcpp/previews` by default, scaled to 128x128. Preview filenames are the album names encoded in base64, so no duplicate previews should be saved.
    
    Assuming `~/.local/bin` is in your `$PATH`, create (and make executable):
    
    ```sh
    # ~/.local/bin/songinfo
    #!/bin/sh
    
    music_dir="\$HOME/Music"
    previewdir="\$XDG_CONFIG_HOME/ncmpcpp/previews"
    filename="(mpc --format "music_dir"/%file% current)"
    previewname="previewdir/(mpc --format %album% current | base64).png"
    
    [ -e "\(previewname" ] \vert{}\vert{} ffmpeg -y -i "\)filename" -an -vf scale=128:128 "\$previewname" > /dev/null 2>&1
    
    notify-send -r 27072 "Now Playing" "\((mpc --format '\%title\% \n\%artist\% - \%album\%' current)" -i "\)previewname"
    ```
    
    ---
    
    and add this to your ncmpcpp config:
    
    ```zsh
    execute_on_song_change = songinfo
    ```

## `cheat.sheets:ncmpcpp` {.toc-hidden-header}

### ncmpcpp

---

!!! abstract "NOTE" 
    **NOTE:**
    
    An mpd client (compatible with mopidy) with a UI very similar to ncmpc, but it provides new useful features such as support for regular expressions for library searches, extended song format, items filtering, the ability to sort playlists, and a local filesystem browser.

---

### Configure ncmpcpp

!!! info "Configure ncmpcpp"
    
    ```bash
    mkdir ~/.ncmpcpp
    cat <<EOF > ~/.ncmpcpp/config
    ncmpcpp_directory = "~/.ncmpcpp"
    mpd_host = "127.0.0.1"
    mpd_port = "6600"
    mpd_music_dir = "/var/lib/mpd/music/"
    EOF
    ```

## Movement

!!! info "Movement"
    
    ```text {.no-copy}
    Up k               Move cursor up
    Down j             Move cursor down
    [                  Move cursor up one album
    ]                  Move cursor down one album
    {                  Move cursor up one artist
    }                  Move cursor down one artist
    Page Up            Page up
    Page Down          Page down
    Home               Home
    End                End
    ```
    
    ---

    ```text {.no-copy}
    Tab                Switch to next screen in sequence
    Shift-Tab          Switch to previous screen in sequence
    F1                 Show help
    1                  Show playlist
    2                  Show browser
    3                  Show search engine
    4                  Show media library
    5                  Show playlist editor
    6                  Show tag editor
    7                  Show outputs
    8                  Show music visualizer
    =                  Show clock
    @                  Show server info
    ```

## Alternative Interfaces and Modes

!!! desc " Alternative Interfaces and Modes"

    - Beyond the standard playlist view, ncmpcpp includes several alternative screens that can also be customized.
    
    - The tag editor allows users to modify music metadata directly from the terminal. The appearance of this editor, including which fields are displayed and how they are highlighted, is configurable. The media library screen, which presents music in a hierarchical tree structure, can have its expansion characters and color coding altered.
    
    - Even the clock screen, which might seem entirely superfluous, can be customized to display time in different formats or act as a stopwatch. Ensuring that the keybindings seamlessly transition the user between these different modes is critical for a cohesive experience.
    
## Global

!!! abstract "Global"
    
    ```text {.no-copy}
    s                  Stop
    p                  Pause
    >                  Next track
    <                  Previous track
    Ctrl-H Backspace   Replay playing song
    f                  Seek forward in playing song
    b                  Seek backward in playing song
    - Left             Decrease volume by 2%
    Right +            Increase volume by 2%
    ```
    
    ---
    
    ```text {.no-copy}
    t                  Toggle space mode (select/add)
    T                  Toggle add mode (add or remove/always add)
    |                  Toggle mouse support
    v                  Reverse selection
    V                  Remove selection
    B                  Select songs of album around the cursor
    a                  Add selected items to playlist
    `                  Add random items to playlist
    r                  Toggle repeat mode
    z                  Toggle random mode
    y                  Toggle single mode
    R                  Toggle consume mode
    Y                  Toggle replay gain mode
    #                  Toggle bitrate visibility
    Z                  Shuffle playlist
    x                  Toggle crossfade mode
    X                  Set crossfade
    ```
    
    ---
    
    ```text {.no-copy}
    u                  Start music database update
    :                  Execute command
    Ctrl-F             Apply filter
    /                  Find item forward
    ?                  Find item backward
    ,                  Jump to previous found item
    .                  Jump to next found item
    w                  Toggle find mode (normal/wrapped)
    G                  Locate song in browser
    ~                  Locate song in media library
    ```
    
    ---
    
    ```text {.no-copy}
    Ctrl-L             Lock/unlock current screen
    Left h             Switch to master screen (left one)
    Right l            Switch to slave screen (right one)
    ```
    
    ---
    
    ```text {.no-copy}
    E                  Locate song in tag editor
    P                  Toggle display mode
    \                  Toggle user interface
    !                  Toggle displaying separators between albums
    g                  Jump to given position in playing song (formats: mm:ss, x%)
    i                  Show song info
    I                  Show artist info
    L                  Toggle lyrics fetcher
    F                  Toggle fetching lyrics for playing songs in background
    q                  Quit
    ```

## Playlist

!!! abstract "Playlist"


    ```text {.no-copy}
    Enter              Play selected item
    Delete             Delete selected item(s) from playlist
    c                  Clear playlist
    C                  Clear playlist except selected item(s)
    Ctrl-P             Set priority of selected items
    Ctrl-K m           Move selected item(s) up
    n Ctrl-J           Move selected item(s) down
    M                  Move selected item(s) to cursor position
    A                  Add item to playlist
    e                  Edit song
    S                  Save playlist
    Ctrl-V             Sort playlist
    Ctrl-R             Reverse playlist
    o                  Jump to current song
    U                  Toggle playing song centering
    ```
    
## Browser

!!! abstract "Browser"

    ```text {.no-copy}
    Enter              Enter directory/Add item to playlist and play it
    Space              Add item to playlist/select it
    e                  Edit song/directory/playlist name
    2                  Browse MPD database/local filesystem
    `                  Toggle sort mode
    o                  Locate playing song
    Ctrl-H Backspace   Jump to parent directory
    Delete             Delete selected items from disk
    G                  Jump to playlist editor (playlists only)
    ```
    
## Search Engine

!!! abstract "Search Engine"

    ```text {.no-copy}
    Enter              Add item to playlist and play it/change option
    Space              Add item to playlist
    e                  Edit song
    y                  Start searching
    3                  Reset search constraints and clear results
    ```
    
## Media Library

!!! abstract "Media Library" 
    
    ```text {.no-copy}
    4                  Switch between two/three columns mode
    Left h             Previous column
    Right l            Next column
    Enter              Add item to playlist and play it
    Space              Add item to playlist
    e                  Edit song
    e                  Edit tag (left column)/album (middle/right column)
    `                  Toggle type of tag used in left column
    m                  Toggle sort mode
    ```

## Playlist editor

!!! abstract "Playlist Editor"
    
    ```text {.no-copy}
    Left h             Previous column
    Right l            Next column
    Enter              Add item to playlist and play it
    Space              Add item to playlist/select it
    e                  Edit song/playlist name
    Ctrl-K m           Move selected item(s) up
    n Ctrl-J           Move selected item(s) down
    Delete             Delete selected playlists (left column)
    C                  Clear playlist except selected item(s)
    Ctrl-P             Set priority of selected items
    Ctrl-K m           Move selected item(s) up
    n Ctrl-J           Move selected item(s) down
    M                  Move selected item(s) to cursor position
    A                  Add item to playlist
    e                  Edit song
    S                  Save playlist
    Ctrl-V             Sort playlist
    Ctrl-R             Reverse playlist
    o                  Jump to current song
    U                  Toggle playing song centering
    ```

## Browser

!!! abstract "Browser"
    
    ```text {.no-copy}
    Enter              Enter directory/Add item to playlist and play it
    Space              Add item to playlist/select it
    e                  Edit song
    e                  Edit directory name
    e                  Edit playlist name
    2                  Browse MPD database/local filesystem
    `                  Toggle sort mode
    o                  Locate playing song
    Ctrl-H Backspace   Jump to parent directory
    Delete             Delete selected items from disk
    G                  Jump to playlist editor (playlists only)
    ```

## Search Engine

!!! abstract "Search Engine" 
    
    ```text {.no-copy}
    Enter              Add item to playlist and play it/change option
    Space              Add item to playlist
    e                  Edit song
    y                  Start searching
    3                  Reset search constraints and clear results
    ```

## Media Library

!!! abstract "Media Library"
    
    ```text {.no-copy}
    4                  Switch between two/three columns mode
    Left h             Previous column
    Right l            Next column
    Enter              Add item to playlist and play it
    Space              Add item to playlist
    e                  Edit song/tag (left column)/album (middle/right column)
    `                  Toggle type of tag used in left column
    m                  Toggle sort mode
    ```

## Playlist Editor

!!! abstract "Playlist Editor"
    
    ```text {.no-copy}
    Left h             Previous column
    Right l            Next column
    Enter              Add item to playlist and play it
    Space              Add item to playlist/select it
    e                  Edit song/playlist name
    Ctrl-K m           Move selected item(s) up
    n Ctrl-J           Move selected item(s) down
    Delete             Delete selected playlists (left column)
    Delete             Delete selected item(s) from playlist (right column)
    c                  Clear playlist
    C                  Clear playlist except selected items
    ```

## Lyrics

!!! abstract "Lyrics"
    
    ```text {.no-copy}
    Space              Toggle reloading lyrics upon song change
    e                  Open lyrics in external editor
    `                  Refetch lyrics
    ```

## Tiny Tag Editor

!!! abstract "Tiny Tag Editor"
    
    ```text {.no-copy}
    Enter              Edit tag
    y                  Save
    ```

## Tag Editor

!!! abstract "Tag Editor"

    ```text {.no-copy}
    Enter              Edit tag/filename of selected item (left column)
    Enter              Perform operation on all/selected items (middle column)
    Space              Switch to albums/directories view (left column)
    Space              Select item (right column)
    Left h             Previous column
    Right l            Next column
    Ctrl-H Backspace   Jump to parent directory (left column, directories view)
    ```

## $tldr:ncmpcpp

### `ncmpcpp`

!!! ex "ncmpcpp"

    A command-line music player client for the Music Player Daemon.
    
    More information: <https://rybczak.net/ncmpcpp>.
    
    Connect to a music player daemon on a given host and port:
    
    `ncmpcpp --host ip --port port`
    
    Display metadata of the current song to console:
    
    `ncmpcpp --current-song`
    
    Use a specified configuration file:
    
    `ncmpcpp --config file`
    
    Use a different set of key bindings from a file:
    
    `ncmpcpp --bindings file`
    
    ---
    
    ```text {.no-copy}
    This is the example bindings file. Copy it to $XDG_CONFIG_HOME/ncmpcpp/bindings or ~/.ncmpcpp/bindings
    ## and set up your preferences.
    ```
    
!!! instruction "General Rules"

    1.
    
    ```zsh {.no-copy}
    ##    Because each action has runtime checks whether it's ok to run it, a few actions can be bound
    ##    to one key. Actions will be bound in order given in configuration file. When a key is pressed,
    ##    first action in order will test itself whether it's possible to run it. If  test succeeds,
    ##    action is executed and other actions bound to this key are ignored. If it doesn't,
    ##    next action in order tests itself etc.
    ```
    
    2.
    
    ```zsh {.no-copy}
    ##    It's possible to bind more that one action at once to a key.
    ##    It can be done using the following syntax:
    ##
    ##    def_key "key"
    ##     action1
    ##     action2
    ##    ...
    ##
    ##    This creates a chain of actions. When such chain is executed, each action in chain is run
    ##    until the end of chain is reached or one of its actions fails to execute due to its
    ##    requirements not being met. If multiple actions and/or chains are bound to the same
    ##    key, they will be consecutively run until one of them gets fully executed.
    ```
     
    3.
    
    ```zsh {.no-copy}
    ##    When ncmpcpp starts, bindings configuration file is parsed and then ncmpcpp provides
    ##    "missing pieces" of default keybindings. If you want to disable some bindings, there is a
    ##    special action called 'dummy' for that purpose. Eg. if you want to disable ability to crop
    ##    playlists, you need to put the following into configuration file:
    ##
    ##    def_key "C"
    ##    dummy
    ##
    ##    After that ncmpcpp will not bind any default action to this key.
    ```
    
    4.
    
    ```szh {.no-copy}
    ##    To let you write simple macros, the following special actions are provided:
    ##    - push_character "character" - pushes given special character into input queue,
    ##    so it will be immediately picked by ncmpcpp upon next call to readKey function.
    ##    Accepted values: mouse, up, down, page_up, page_down, home, end, space, enter,
    ##    insert, delete, left, right, tab, ctrl-a, ctrl-b, ..., ctrl-z, ctrl-[, ctrl-\\,
    ##    ctrl-], ctrl-^, ctrl-_, f1, f2, ..., f12, backspace. In addition, most of these names can be
    ##    prefixed with alt-/ctrl-/shift- to be recognized with the appropriate modifier key(s).
    ##
    ##    - push_characters "string" - pushes given string into input queue.
    ##
    ##    - require_runnable "action" - checks whether given action is runnable and fails if it
    ##    isn't. This is especially useful when mixed with previous two functions. Consider the
    ##    following macro definition:
    ##
    ##      def_key "key"
    ##        push_characters "custom_filter"
    ##        apply_filter
    ##
    ##      If apply_filter can't be currently run, we end up with sequence of characters in input
    ##    queue which will be treated just as we typed them. This may lead to unexpected
    ##    results (in this case 'c' will most likely clear current playlist, 'u' will trigger database
    ##    update, 's' will stop playback etc.). To prevent such thing from happening, we need
    ##    to change above definition to this one:
    ##
    ##      def_key "key"
    ##        require_runnable "apply_filter"
    ##        push_characters "custom_filter"
    ##        apply_filter
    ##
    ##      Here, first we test whether apply_filter can be actually run before we stuff characters
    ##    into input queue, so if condition is not met, whole chain is aborted and we're fine.
    ##
    ##    - require_screen "screen" - checks whether given screen is currently active. accepted
    ##    values:browser, clock, help, media_library, outputs, playlist, playlist_editor, search_engine,
    ##    tag_editor, visualizer, last_fm, lyrics, selected_items_adder, server_info, song_info,
    ##    sort_playlist_dialog, tiny_tag_editor.
    ##
    ##    - run_external_command "command" - runs given command using system() function.
    ##
    ##    - run_external_console_command "command" - runs given console command using
    ##    system() function.
    ```
    
    5.
    
    ```zsh {.no-copy}
    ##    In addition to binding to a key, you can also bind actions
    ##    or chains of actions to a command. If it comes to commands,
    ##    syntax is very similar to defining keys. Here goes example
    ##    definition of a command:
    ##
    ##      def_command "quit" [deferred]
    ##        stop
    ##        quit
    ##
    ##    If you execute the above command (which can be done by
    ##    invoking action execute_command, typing 'quit' and pressing
    ##    enter), ncmpcpp will stop the player and then quit. Note the
    ##    presence of word 'deferred' enclosed in square brackets. It
    ##    tells ncmpcpp to wait for confirmation (ie. pressing enter)
    ##    after you typed quit. Instead of 'deferred', 'immediate'
    ##    could be used. Then ncmpcpp will not wait for confirmation
    ##    (enter) and will execute the command the moment it sees it.
    ##
    ##    Note: while command chains are executed, internal environment
    ##    update (which includes current window refresh and mpd status
    ##    update) is not performed for performance reasons. However, it
    ##    may be desirable to do so in some situration. Therefore it's
    ##    possible to invoke by hand by performing 'update enviroment'
    ##    action.
    ##
    ## Note: There is a difference between:
    ##
    ##         def_key "key"
    ##           action1
    ##
    ##         def_key "key"
    ##           action2
    ##
    ##       and
    ##
    ##         def_key "key"
    ##           action1
    ##           action2
    ##
    ##      First one binds two single actions to the same key whilst
    ##      second one defines a chain of actions. The behavior of
    ##      these two is different and is described in (1) and (2).
    ##
    ## Note: Function def_key accepts non-ascii characters.
    ##
    ##### List of unbound actions #####
    ##
    ## The following actions are not bound to any key/command:
    ##
    ##  - set_volume
    ##  - load
    ##
    #
    #def_key "mouse"
    #  mouse_event
    #
    #def_key "up"
    #  scroll_up
    #
    #def_key "shift-up"
    #  select_item
    #  scroll_up
    #
    #def_key "down"
    #  scroll_down
    #
    #def_key "shift-down"
    #  select_item
    #  scroll_down
    #
    #def_key "["
    #  scroll_up_album
    #
    #def_key "]"
    #  scroll_down_album
    #
    #def_key "{"
    #  scroll_up_artist
    #
    #def_key "}"
    #  scroll_down_artist
    #
    #def_key "page_up"
    #  page_up
    #
    #def_key "page_down"
    #  page_down
    #
    #def_key "home"
    #  move_home
    #
    #def_key "end"
    #  move_end
    #
    #def_key "insert"
    #  select_item
    #
    #def_key "enter"
    #  enter_directory
    #
    #def_key "enter"
    #  toggle_output
    #
    #def_key "enter"
    #  run_action
    #
    #def_key "enter"
    #  play_item
    #
    #def_key "space"
    #  add_item_to_playlist
    #
    #def_key "space"
    #  toggle_lyrics_update_on_song_change
    #
    #def_key "space"
    #  toggle_visualization_type
    #
    #def_key "delete"
    #  delete_playlist_items
    #
    #def_key "delete"
    #  delete_browser_items
    #
    #def_key "delete"
    #  delete_stored_playlist
    #
    #def_key "right"
    #  next_column
    #
    #def_key "right"
    #  slave_screen
    #
    #def_key "right"
    #  volume_up
    #
    #def_key "+"
    #  volume_up
    #
    #def_key "left"
    #  previous_column
    #
    #def_key "left"
    #  master_screen
    #
    #def_key "left"
    #  volume_down
    #
    #def_key "-"
    #  volume_down
    #
    #def_key ":"
    #  execute_command
    #
    #def_key "tab"
    #  next_screen
    #
    #def_key "shift-tab"
    #  previous_screen
    #
    #def_key "f1"
    #  show_help
    #
    #def_key "1"
    #  show_playlist
    #
    #def_key "2"
    #  show_browser
    #
    #def_key "2"
    #  change_browse_mode
    #
    #def_key "3"
    #  show_search_engine
    #
    #def_key "3"
    #  reset_search_engine
    #
    #def_key "4"
    #  show_media_library
    #
    #def_key "4"
    #  toggle_media_library_columns_mode
    #
    #def_key "5"
    #  show_playlist_editor
    #
    #def_key "6"
    #  show_tag_editor
    #
    #def_key "7"
    #  show_outputs
    #
    #def_key "8"
    #  show_visualizer
    #
    #def_key "="
    #  show_clock
    #
    #def_key "@"
    #  show_server_info
    #
    #def_key "s"
    #  stop
    #
    #def_key "p"
    #  pause
    #
    #def_key ">"
    #  next
    #
    #def_key "<"
    #  previous
    #
    #def_key "ctrl-h"
    #  jump_to_parent_directory
    #
    #def_key "ctrl-h"
    #  replay_song
    #
    #def_key "backspace"
    #  jump_to_parent_directory
    #
    #def_key "backspace"
    #  replay_song
    #
    #def_key "backspace"
    #  play
    #
    #def_key "f"
    #  seek_forward
    #
    #def_key "b"
    #  seek_backward
    #
    #def_key "r"
    #  toggle_repeat
    #
    #def_key "z"
    #  toggle_random
    #
    #def_key "y"
    #  save_tag_changes
    #
    #def_key "y"
    #  start_searching
    #
    #def_key "y"
    #  toggle_single
    #
    #def_key "R"
    #  toggle_consume
    #
    #def_key "Y"
    #  toggle_replay_gain_mode
    #
    #def_key "T"
    #  toggle_add_mode
    #
    #def_key "|"
    #  toggle_mouse
    #
    #def_key "#"
    #  toggle_bitrate_visibility
    #
    #def_key "Z"
    #  shuffle
    #
    #def_key "x"
    #  toggle_crossfade
    #
    #def_key "X"
    #  set_crossfade
    #
    #def_key "u"
    #  update_database
    #
    #def_key "ctrl-s"
    #  sort_playlist
    #
    #def_key "ctrl-s"
    #  toggle_browser_sort_mode
    #
    #def_key "ctrl-s"
    #  toggle_media_library_sort_mode
    #
    #def_key "ctrl-r"
    #  reverse_playlist
    #
    #def_key "ctrl-f"
    #  apply_filter
    #
    #def_key "ctrl-_"
    #  select_found_items
    #
    #def_key "/"
    #  find
    #
    #def_key "/"
    #  find_item_forward
    #
    #def_key "?"
    #  find
    #
    #def_key "?"
    #  find_item_backward
    #
    #def_key "."
    #  next_found_item
    #
    #def_key ","
    #  previous_found_item
    #
    #def_key "w"
    #  toggle_find_mode
    #
    #def_key "e"
    #  edit_song
    #
    #def_key "e"
    #  edit_library_tag
    #
    #def_key "e"
    #  edit_library_album
    #
    #def_key "e"
    #  edit_directory_name
    #
    #def_key "e"
    #  edit_playlist_name
    #
    #def_key "e"
    #  edit_lyrics
    #
    #def_key "i"
    #  show_song_info
    #
    #def_key "I"
    #  show_artist_info
    #
    #def_key "g"
    #  jump_to_position_in_song
    #
    #def_key "l"
    #  show_lyrics
    #
    #def_key "ctrl-v"
    #  select_range
    #
    #def_key "v"
    #  reverse_selection
    #
    #def_key "V"
    #  remove_selection
    #
    #def_key "B"
    #  select_album
    #
    #def_key "a"
    #  add_selected_items
    #
    #def_key "c"
    #  clear_playlist
    #
    #def_key "c"
    #  clear_main_playlist
    #
    #def_key "C"
    #  crop_playlist
    #
    #def_key "C"
    #  crop_main_playlist
    #
    #def_key "m"
    #  move_sort_order_up
    #
    #def_key "m"
    #  move_selected_items_up
    #
    #def_key "n"
    #  move_sort_order_down
    #
    #def_key "n"
    #  move_selected_items_down
    #
    #def_key "M"
    #  move_selected_items_to
    #
    #def_key "A"
    #  add
    #
    #def_key "S"
    #  save_playlist
    #
    #def_key "o"
    #  jump_to_playing_song
    #
    #def_key "G"
    #  jump_to_browser
    #
    #def_key "G"
    #  jump_to_playlist_editor
    #
    #def_key "~"
    #  jump_to_media_library
    #
    #def_key "E"
    #  jump_to_tag_editor
    #
    #def_key "U"
    #  toggle_playing_song_centering
    #
    #def_key "P"
    #  toggle_display_mode
    #
    #def_key "\\"
    #  toggle_interface
    #
    #def_key "!"
    #  toggle_separators_between_albums
    #
    #def_key "L"
    #  toggle_lyrics_fetcher
    #
    #def_key "F"
    #  fetch_lyrics_in_background
    #
    #def_key "alt-l"
    #  toggle_fetching_lyrics_in_background
    #
    #def_key "ctrl-l"
    #  toggle_screen_lock
    #
    #def_key "`"
    #  toggle_library_tag_type
    #
    #def_key "`"
    #  refetch_lyrics
    #
    #def_key "`"
    #  add_random_items
    #
    #def_key "ctrl-p"
    #  set_selected_items_priority
    #
    #def_key "q"
    #  quit
    #
    ```
    
