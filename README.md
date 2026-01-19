# Notice from fork creator (lot of text warning)

Hello! The name is SpeedRunHunter, or just Hunter if you don't have much time. I'm just a goof software dev, with too much time on their hands, wanting to play some games on Linux through Lutris. Said games may be ROMS, but not from the TOSEC project. This causes Lutris to not recognize said ROMS, hence I can't use the ROM drag and drop method, thus needing them to be manually added one after another. And given I'm trying RetroAchievement hunting, I don't know, have you seen how many Sonic games - retail, homebrew or hacks - have cheevos? Nevermind some games that have subsets.

After trying the original script, downloaded through `pypi`, and it not working, because of a missing `steam_id` column in the `games` table in the sqlite `pga.db` file - which is happening because the table has since been changed to a `service` and `service_id` setup, where to replace `steam_id`, `service` will hold the value of `"steam"` and the id will be the actual steam store ID of the game in question -, and seeing some other open issues on the repository, and having recently gotten more familiarized with Python - admitedly through "The Farmer Was Replaced" game, and not some other more proper means -, I thought to take this repo and code as a base, and fix it up for modern Lutris.

I will say this much though; I'm not about to vibe code update this. I may know more Java than Python, because we used and started with Java in high school and I disliked Python, largely because of the different syntax and dynamic typing. But I won't just take an AI to do the job for me because of that. Especially if I explicitly played "The Farmer Was Replaced" to try and like Python, might as well put that to some better use now, and learn even more Python.

I don't know what else I'll do with this code beyond updating it. Should issues come up, I'll try to fix them obviously, but I don't really have my own ideas for additional features. Well maybe one:
- what if you want the ROM in question to be loaded by libretro, a.k.a RetroArch, besides specifying `libretro` as the runner, and the console platform, like "Sony Playstation 2", you could also maybe specify the libretro core, like `LRPS2`
  - I guess if I could provide a list of cores in the case of RetroArch, what about being able to provide a list for runners too?
  - and for that matter, what are the chances that someone importing games is going to think precisely about whether they want their PS2 games loaded with standalone PCSX2 or retroarch's libretro fork LRPS2? If they want to choose, I believe they should be able to, but if the user otherwise can't/doesn't care, as long as at least a supported platform is provided, the script could just pick a default
  - and even in the case of providing a default option, what is the guarantee the user has the agiven runner or core installed? - or in other words, this would also involve probing directories; which I guess this script messes around with a sqlite file too, so... ¯\_(ツ)_/¯

But that's about the only thing I could come up with for now.

Either way,<br/>
Thanks for reading.

#### The original `README.md` is as follows

---
<br/>

# `lutris-bulk-adder`

## Description

This is a simple Python script to import a directory of ROM files into Lutris.  The directory must contain only games from one platform.  I have only tested this on my own computer for a limited number of platforms.

I don't really know what will happen if Lutris is open during the import, so make sure to restart Lutris immediately after importing, or close it before the import - this script will write directly to Lutris's SQLite database, so proceed with caution.

## Requirements

- `PyYAML`

## Installation

`pip install --user --upgrade lutris-bulk-adder`

## Usage

### Required arguments

`-d` / `--directory`: Directory to scan for ROM files.

`-r` / `--runner`: Slug name of Lutris runner to use (e.g. `dolphin`, `snes9x`)

`-p` / `--platform`: Platform name.  A list of platform names is included in the script, but if one is not included, you can figure it out by looking at the Lutris [runner class definitions](https://github.com/lutris/lutris/tree/master/lutris/runners) for the value(s) listed under the `platforms` member.

### Lutris path arguments

These default to the default locations that Lutris will install to.

`-ld` / `--lutris-database`: Path to the Lutris SQLite database.  Default: `~/.local/share/lutris/pga.db`

`-ly` / `--lutris-yml-dir`: Directory containing Lutris installed game YAML files.  Default: `~/.config/lutris/games`

`-lg` / `--lutris-game-dir`: Lutris games installation directory.  This shouldn't do anything as ROMs aren't installed, but the Lutris database needs it.  Default: `~/Games`

### Other arguments

`-f` / `--file-types`: Space-separated list of file types to scan for.  Defaults to `iso,zip,sfc,gba,gbc,gb,md,n64,nes,32x,gg,sms`

`-o` / `--game-options`: Additional options to write to the YAML file under the "game" key (e.g. platform number as required for Dolphin)

`-s` / `--strip-filename`: Space-separated list of strings to strip from filenames when generating game names.

`-n` / `--no-write`: Do not write YML files or alter Lutris database, only print data to be written out to stdout. (i.e. dry run)

### Example

`lutris_bulk_adder -d /data/Emulation/Wii -r dolphin -s '(USA)' -p "Nintendo Wii" -o platform=1`

Adds all files in `/data/Emulation/Wii` to the `dolphin` runner, ignoring substrings containing `(USA)` in the filename when deriving the game name, for the `Nintendo Wii` platform, and adds `platform: '1'` to the `game` key in the YAML file.
