# `lutris-bulk-adder`

## Description

This is a simple Python script to import a directory of ROM files into Lutris.  The directory must contain only games from one platform.  I have only tested this on my own computer for a limited number of platforms.

I don't really know what will happen if Lutris is open during the import, so make sure to restart Lutris immediately after importing, or close it before the import - this script will write directly to Lutris's SQLite database, so proceed with caution.

## Rambling

This is a fork of the original developed by yours truly, SpeedRunHunter - or just Hunter if you don't have much time. In prior commits you can find a different version of the README with a lot more text. I grabbed a load of ROMs for the sake of RetroAchievement hunting, and ran into the problem of not being able to easily import my ROMs - because Lutris only knows of the TOSEC project ROMs' file checksums.

I tried to use the PyPI package version of this script, realizing though that it is outdated compared to the original github repo, which fixed the issue with Lutris's SQLite DB no longer having a `steam_id` columns but instead splitting it into `service` and `service_id` columns. Coupled with some other smaller fixes from @ronicaltech that have pull requests, but weren't upstreamed - if @ronicaltech sees this, I hope you don't mind that I yoinked your fixes; I made sure to include credits to you in code comments, but if you don't like that, I'm absolutely open to figuring something out about it. 

Again, in the previous README, I talked about a new feature I thought to add to this script. It's essentially automatic runner and if necessary libretro core setup for your ROMs. So compared to having to specify a runner with directory and platform when using the script, the runner argument is no longer required. At the same time though, this did require storing a lot of information about platforms in the app, so I figured for users who may want to learn more, they can view this information. At the same time, since libretro, a.k.a. RetroArch is an option for a runner for a lot of platforms, I felt it would be useful to provide the additional option to change what core is used - compared to having to do that via the `game-options` flag.

Let me make something clear: I'm sure that some of the things I'm doing may seem to other people who are better versed in open-source code development, project/version/source/git management, and above all Python development will consider me an utter amateur. Which,
1. firstly, excuse me, but that is a bit harsh to some extent. 

2. Secondly, I'd like to provide a bit of background on me. I graduated from the second best IT trade school in my home country of Hungary and took an additional year of adult education there. Said year primarly consisted of Java with Spring Boot for RESTful APIs and JS with React for frontend development, with a side of MySQL database management, and pretty much self-taught and improvised git management. So, my possibly bad skills speaks either of my defficencies or the quality of the trade school's teachings - I like to believe both is fine, though.

3. Thirdly, as I also admit in my prior README, this is my first attempt at a proper Python project. I have started with Java in trade school, and have always been a Java person. I barely had much if any exposure to Python, and wasn't a big fan especially because of the weird syntax. And to get myself better familiarized with Python, I chose to play the game "The Farmer Was Replaced" - for the uninitiated, basically you control a farmer drone by programming it in a Python-like language, which language isn't 100% Python, but for the sake of the game it might as well be, especially considering in your save, the scripts are saved as `.py` files, and there's also support for external code editors in the game. I explicitly decided to fork this project, update it and expand on it - without overwriting its original functionality - to get a better taste of developing with Python. So yes, I am *functionally* amateur in Python.

4. And finally, back to git stuff, but this time open source related; I don't know how badly one could screw up with this kind of stuff. As far as I can interpret the LICENSE set in place by the original creator, I'm not breaking it by including the original in this repo. And I'm not about to tackle potentially sublicensing or whatever that maybe or change the license to something else. I'm not a lawyer or license expert; I'm just a stupid software dev, that just want's to look at a fancy text-editor and type a boat-load - which is clearly happening.

## Requirements

- `PyYAML`

## Installation

NOTE: This updated script has not yet been published to PyPI. I admit I'm nervous to do so. Also, the original repo had the `setup.py` script use distutils, which I couldn't find information on. I found setuptools instead, although I'm unsure if it's a drop in replacement over distutils. Until this note is removed, the only install method for the script for now is to instead download the script files or clone the git repository.

For future's sake however, this section is updated to contain more information, but may still be subject to some changes - specifically regarding the package name.

---

Basic installation with `pip`:

`pip install --user --upgrade lutris-bulk-adder`

If you are on a system with a Python install that throws the `externally-managed-environment` error when trying to install PyPI packages, which is typical for a Linux system in my experience, and your package manager doesn't have this PyPI package available in it, you have two options:
1. either use a Python virtual environment for the script, and activate that everytime you want to use the script, like so:

```
python3 -m venv path/to/venv
source path/to/venv/bin/activate
# you mustn't install as a user here

# the only way to do that would be changing a
# venv config setting in path/to/venv/pyvenv.cfg
# which would cause pip to install to a folder
# outside of the venv folder
# ask me how I know
pip install --upgarde lutris-bulk-adder
```

2. alternatively, install and use `pipx` instead to install the script; it will automate creating the virtual environment, but will also setup a link to the script in a folder that's on your system's PATH environment variable

`pipx install lutris-bulk-adder`

`pipx` by default already installs PyPI packages for the user only.

To update with `pipx`:

`pipx upgrade lutris-bulk-adder`

You can also install the package globally in `pipx` to install it for every user:

`pipx install --global lutris-bulk-adder`

## Usage

### Required arguments

`-d` / `--directory`: Directory to scan for ROM files.

`-p` / `--platform`: Platform name.

## Optional arguments

`-r` / `--runner`: Slug name of Lutris runner to use (e.g. `dolphin`, `snes9x`, `libretro`)

`-c` / `--core`: Slug name of libretro core to use (e.g. `DoubleCherryGB`, `mednafen_psx_hw`, `picodrive`)

### Lutris path arguments

These default to the default locations that Lutris will install to.

`-ld` / `--lutris-database`: Path to the Lutris SQLite database.  Default: `~/.local/share/lutris/pga.db`

`-ly` / `--lutris-yml-dir`: Directory containing Lutris installed game YAML files.  Default: `~/.local/share/lutris/games`

`-lg` / `--lutris-game-dir`: Lutris games installation directory.  This shouldn't do anything as ROMs aren't installed, but the Lutris database needs it.  Default: `~/Games`

### Informational arguments

`-i` / `--platform-info`: Takes a single string argument - requires single (') or double (") quotes - that matches case-sensitively to the name of a platform known by the script.

`-a` / `--dump-platform-info`: A zero parameter flag that, when set, prints all information of known platforms from the script.

### Other arguments

`-f` / `--file-types`: Space-separated list of file types to scan for.  Defaults to `iso,zip,sfc,gba,gbc,gb,md,n64,nes,32x,gg,sms,chd`

`-o` / `--game-options`: Additional options to write to the YAML file under the "game" key (e.g. platform number as required for Dolphin)

`-s` / `--strip-filename`: Space-separated list of strings to strip from filenames when generating game names.

`-n` / `--no-write`: Do not write YML files or alter Lutris database, only print data to be written out to stdout. (i.e. dry run)

### Examples

`lutris_bulk_adder -d /data/Emulation/Wii -r dolphin -s '(USA)' -p "Nintendo Wii" -o platform=1`

Adds all files in `/data/Emulation/Wii` to Lutris via the `dolphin` runner, ignoring substrings containing `(USA)` in the filename when deriving the game name, for the `Nintendo Wii` platform, and adds `platform: '1'` to the `game` key in the YAML file.

`lutris_bulk_adder -d ~/ROMZZZ/SegaLibrary/MegaDriveLibrary -p "Sega Mega Drive"`

Adds all files in `~/ROMZZZ/SegaLibrary/MegaDriveLibrary` to Lutris via the default runner for the `Sega Mega Drive` platform. For Mega Drive - or Genesis, both names are supported and that includes the Sega CD/Mega CD -, or other platforms where the default may be libretro, which it is for the Mega Drive, as is required and setup usually by Lutris itself, the YAML file will contain the core information for libretro. And in this case whatever the default core is.

<details>
  <summary>Also</summary>

  &nbsp; How did you know I was not American?
  &nbsp; Oh wait, I guess you know I live in Hungary, huh.

</details><br/>

`lutris_bulk_adder -d /run/media/user/CDZZZ/SegaCD -p "Sega CD" -c clowncdemu`

Adds all files in `/run/media/user/CDZZZ/SegaCD` to Lutris via the default runner for the `Sega CD` platform, and use the `clowncdemu` libretro core. In this scenario we make the assumption on the script side - spoiler, correctly as well - that the default runner for the `Sega CD` is RetroArch. If that's not the case, the `-c` flag and its argument are ignored.

<details>
  <summary>Why is it ignored?</summary>

  &nbsp; If we wanted the script to not ignore the the `-c` libretro core setting flag, but the default runner for the given platform is not RetroArch - an example case would be the Commodore 8-bit machines[^1] - we need to make a choice in the implementation of the script as to what it should do. 
  
  &nbsp; We could ignore the flag, like I chose to. Or we could instead make the `-c` flag additionally equivalent to `-r libretro` (or `--runner libretro`) and itself, and therefore silently - without user's explicit knowledge - switch runners.

  &nbsp; Unless we ask for confirmation from the user, even then, if they decline to make the change, then what should happen? Should the script error out, should it respect the user's choice, and stick with the default, at which point getting back to square one basically. Unless they agree to change the runner as well, which does mean smooth sailing.

  &nbsp; Maybe a silent switch like this could be desirable though, but I struggle to see the appeal in my opinion. And I admit I'm probably just overthinking this, but in my opinion again, good software is made to be ready for all situations, and rationale is clearly explained for it. Hence you're reading... well, **this**.

  [^1]: (inside the "Why is it ignored?" details section) in RetroArch the `vice` emulator LR core implementation is split into individual and unique cores for different machines, such as C64, C128, Plus/4, etc., and different sub-configurations for the same machine, whether that's emulation config or additional hardware, like the C64 SuperCPU

</details>