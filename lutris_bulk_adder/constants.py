# I plan to put this into the platforms dict for each platform

DEFAULT_ROM_FILE_EXTS = ['iso', 'zip', 'sfc', 'gba', 'gbc', 'gb', 'md', 'n64',
                         'nes', '32x', 'gg', 'sms', 'bin', 'chd']

# note from Hunter:
# this is in no way an exhaustive list
# or dictionary as it has become
# but I argue it's more comprehensive than before
# I pretty much just went through each core in retroarch
# noted the platform the core was for
# and unless the list already contained it, I added it
# then filled in some addittional ones for standalone emulators
# like e.g. Yuzu/Ryujinx and their forks, Cemu, XEMU, Xenia, RPCS3, etc.
# but then, because I want to provide runner and retroarch core selections, and defaults
# as mentioned, this list needs to be a dictionary now instead
# mapping to another dictionary inside to multiple values

# I'm absolutely open to changing defaults
# my principles in choosing were:
# - if available, pick retroarch, as its the easiest
# - for retroarch pick the best possible core as in
#   to pick the newest and most up to date core
# - if there is a standalone option, and retroarch
#   doesn't have a combined option for all of them
#   (looking at you vice), just pick the standalone
# - and if retroarch is not an option,
#   just pick the standalone one obviously
# - if it's very specific, like scummvm, even if
#   there is a retroarch core, just use the standalone anyway
PLATFORMS = {
    '3DO': {
        "runners": ["libretro"],
        "cores": ["opera"],
        "default_runner": "libretro",
        "default_core": "opera"
    },
    'Amstrad CPC': {
        "runners": ["libretro"],
        "cores": ["cap32", "crocods"],
        "default_runner": "libretro",
        "default_core": "cap32"
    },
    'Amstrad GX4000': {
        "runners": ["libretro"],
        "cores": ["cap32"],
        "default_runner": "libretro",
        "default_core": "cap32"
    },
    'Arcade': {
        "runners": ["mame", "libretro"],
        "cores": ["daphne", "dice", "fbalpha2012", "fbneo", "hbmame", "mame2000", "mame2003", "mame2003_midway", "mame2003_plus", "mame2009", "mame2010", "mame2015", "mame2016", "mame", "mamearcade"],
        "default_runner": "libretro",
        "default_core": "mame"
    },
    'Arduboy': {
        "runners": ["libretro"],
        "cores": ["ardens, arduous"],
        "default_runner": "libretro",
        "default_core": "ardens"
    },
    'Atari 2600': {
        "runners": ["libretro", "stella"],
        "cores": ["stella", "stella2014", "stella2023"],
        "default_runner": "libretro",
        "default_core": "stella"
    },
    'Atari 5200': {
        "runners": ["libretro", "a5200"],
        "cores": ["atari800", "a5200"],
        "default_runner": "libretro",
        "default_core": "atar800"
    },
    'Atari 7800': {
        "runners": ["libretro"],
        "cores": ["prosystem"],
        "default_runner": "libretro",
        "default_core": "prosystem"
    },
    'Atari 400': {
        "runners": ["libretro"],
        "cores": ["atari800"],
        "default_runner": "libretro",
        "default_core": "atari800"
    },
    'Atari 800': {
        "runners": ["libretro"],
        "cores": ["atari800"],
        "default_runner": "libretro",
        "default_core": "atari800"
    },
    'Atari 600XL': {
        "runners": ["libretro"],
        "cores": ["atari800"],
        "default_runner": "libretro",
        "default_core": "atari800"
    },
    'Atari 800XL': {
        "runners": ["libretro"],
        "cores": ["atari800"],
        "default_runner": "libretro",
        "default_core": "atari800"
    },
    'Atari 130XE': {
        "runners": ["libretro"],
        "cores": ["atari800"],
        "default_runner": "libretro",
        "default_core": "atari800"
    },
    'Atari Jaguar': {
        "runners": ["libretro", "virtualjaguar"],
        "cores": ["virtualjaguar"],
        "default_runner": "libretro",
        "default_core": "virtualjaguar"
    },
    'Atari Lynx': {
        "runners": ["libretro", "mednafen"],
        "cores": ["handy", "holani", "mednafen_lynx"],
        "default_runner": "libretro",
        "default_core": "mednafen_lynx"
    },
    'Atari ST': {
        "runners": ["libretro", "hatari"],
        "cores": ["hatari"],
        "default_runner": "libretro",
        "default_core": "hatari"
    },
    'Atari STE': {
        "runners": ["libretro", "hatari"],
        "cores": ["hatari"],
        "default_runner": "libretro",
        "default_core": "hatari"
    },
    'Atari TT': {
        "runners": ["libretro"],
        "cores": ["hatari"],
        "default_runner": "libretro",
        "default_core": "hatari"
    },
    'Atari Falcon': {
        "runners": ["libretro"],
        "cores": ["hatari"],
        "default_runner": "libretro",
        "default_core": "hatari"
    },
    'Bandai WonderSwan': {
        "runners": ["libretro"],
        "cores": ["mednafen_wswan"],
        "default_runner": "libretro",
        "default_core": "mednafen_wswan"
    },
    'Bandai WonderSwan Color': {
        "runners": ["libretro"],
        "cores": ["mednafen_wswan"],
        "default_runner": "libretro",
        "default_core": "mednafen_wswan"
    },
    'Capcom CPS-1': {
        "runners": ["libretro"],
        "cores": ["fbalpha2012_cps1", "fbneo_cps12"],
        "default_runner": "libretro",
        "default_core": "fbneo_cps12"
    },
    'Capcom CPS-2': {
        "runners": ["libretro"],
        "cores": ["fbalpha2012_cps2", "fbneo_cps12"],
        "default_runner": "libretro",
        "default_core": "fbneo_cps12"
    },
    'Capcom CPS-3': {
        "runners": ["libretro"],
        "cores": ["fbalpha2012_cps3"],
        "default_runner": "libretro",
        "default_core": "fbalpha2012_cps3"
    },
    'ChaiLove': {
        "runners": ["libretro"],
        "cores": ["chailove"],
        "default_runner": "libretro",
        "default_core": "chailove"
    },
    'CHIP-8': {
        "runners": ["libretro"],
        "cores": ["jaxe"],
        "default_runner": "libretro",
        "default_core": "jaxe"
    },
    'ColecoVision': {
        "runners": ["libretro", "colem"],
        "cores": ["gearcoleco", "jollycv"],
        "default_runner": "libretro",
        "default_core": "jollycv"
    },
    'CreatiVision': {
        "runners": ["libretro"],
        "cores": ["jollycv"],
        "default_runner": "libretro",
        "default_core": "jollycv"
    },
    'MyVision': {
        "runners": ["libretro"],
        "cores": ["jollycv"],
        "default_runner": "libretro",
        "default_core": "jollycv"
    },
    'Commodore Amiga': {
        "runners": ["libretro", "fsuae"],
        "cores": ["puae", "puae2021"],
        "default_runner": "libretro",
        "default_core": "puae"
    },
    'Commodore 128': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_x128"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore 16/Plus/4': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_xplus4"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore 64': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_x64", "vice_x64sc", "x64sdl"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore 64 Direct-to-TV': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_x64dtv"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore 64 SuperCPU': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_xscpu64"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore CBM-II 5x0': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_xcbm5x0"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore CBM-II 6x0': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_xcbm2"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore PET': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_xpet"],
        "default_runner": "vice",
        "default_core": None
    },
    'Commodore VIC-20': {
        "runners": ["libretro", "vice"],
        "cores": ["vice_xvic"],
        "default_runner": "vice",
        "default_core": None
    },
    'Elektronika BK-0010': {
        "runners": ["libretro"],
        "cores": ["bk"],
        "default_runner": "libretro",
        "default_core": "bk"
    },
    'Elektronika BK-0010.01': {
        "runners": ["libretro"],
        "cores": ["bk"],
        "default_runner": "libretro",
        "default_core": "bk"
    },
    'Elektronika BK-0011 (M)': {
        "runners": ["libretro"],
        "cores": ["bk"],
        "default_runner": "libretro",
        "default_core": "bk"
    },
    'Enterprise 64': {
        "runners": ["libretro"],
        "cores": ["ep128emu"],
        "default_runner": "libretro",
        "default_core": "ep128emu"
    },
    'Enterprise 128': {
        "runners": ["libretro"],
        "cores": ["ep128emu"],
        "default_runner": "libretro",
        "default_core": "ep128emu"
    },
    'Fairchild Channel F': {
        "runners": ["libretro"],
        "cores": ["freechaf"],
        "default_runner": "libretro",
        "default_core": "freechaf"
    },
    'GAM4980': {
        "runners": ["libretro"],
        "cores": ["gam4980"],
        "default_runner": "libretro",
        "default_core": "gam4980"
    },
    'GCE Vectrex': {
        "runners": ["libretro"],
        "cores": ["vecx"],
        "default_runner": "libretro",
        "default_core": "vecx"
    },
    'Infocom Z-Machine': {
        "runners": ["libretro", "frotz"],
        "cores": ["mojozork"],
        "default_runner": "libretro",
        "default_core": "mojozork"
    },
    'Java ME': {
        "runners": ["libretro"],
        "cores": ["squirreljme"],
        "default_runner": "libretro",
        "default_core": "squirreljme"
    },
    'Magnavox Odyssey 2': {
        "runners": ["libretro", "o2em"],
        "cores": ["o2em"],
        "default_runner": "libretro",
        "default_core": "o2em"
    },
    'Philips Videopac+': {
        "runners": ["libretro", "o2em"],
        "cores": ["o2em"],
        "default_runner": "libretro",
        "default_core": "o2em"
    },
    'Mattel Intellivision': {
        "runners": ["libretro", "jzintv"],
        "cores": ["freeintv"],
        "default_runner": "libretro",
        "default_core": "freeintv"
    },
    'Mega Duck': {
        "runners": ["libretro"],
        "cores": ["sameduck"],
        "default_runner": "libretro",
        "default_core": "sameduck"
    },
    'Cougar Boy': {
        "runners": ["libretro"],
        "cores": ["sameduck"],
        "default_runner": "libretro",
        "default_core": "sameduck"
    },
    'MS-DOS': {
        "runners": ["libretro", "dosbox", "86box", "pcem"],
        "cores": ["dosbox_core", "dosbox_pure", "dosbox_svn", "virtualxt"],
        "default_runner": "libretro",
        "default_core": "dosbox_core"
    },
    'Microsoft MSX': {
        "runners": ["libretro", "openmsx"],
        "cores": ["fmsx"],
        "default_runner": "libretro",
        "default_core": "fmsx"
    },
    'Microsoft MSX2': {
        "runners": ["libretro", "openmsx"],
        "cores": ["fmsx"],
        "default_runner": "libretro",
        "default_core": "fmsx"
    },
    'Microsoft MSX2+': {
        "runners": ["libretro", "openmsx"],
        "cores": ["fmsx"],
        "default_runner": "libretro",
        "default_core": "fmsx"
    },
    'Microsoft XBOX': {
        "runners": [""],
        "cores": [""],
        "default_runner": "",
        "default_core": ""
    },
    'Microsoft XBOX 360': {
        "runners": [""],
        "cores": [""],
        "default_runner": "",
        "default_core": ""
    },
    'NEC PC Engine': {
        "runners": ["libretro", "mednafen"],
        "cores": ["geargrafx", "mednafen_pce", "mednafen_pce_fast"],
        "default_runner": "libretro",
        "default_core": "mednafen_pce"
    },
    'NEC PC Engine CD': {
        "runners": ["libretro", "mednafen"],
        "cores": ["geargrafx", "mednafen_pce", "mednafen_pce_fast"],
        "default_runner": "libretro",
        "default_core": "mednafen_pce"
    },
    'NEC PC Engine SuperGrafx': {
        "runners": ["libretro", "mednafen"],
        "cores": ["geargrafx", "mednafen_pce", "mednafen_supergrafx"],
        "default_runner": "libretro",
        "default_core": "mednafen_pce"
    },
    'NEC PC-8000': {
        "runners": ["libretro"],
        "cores": ["quasi88"],
        "default_runner": "libretro",
        "default_core": "quasi88"
    },
    'NEC PC-8800': {
        "runners": ["libretro"],
        "cores": ["quasi88"],
        "default_runner": "libretro",
        "default_core": "quasi88"
    },
    'NEC PC-98': {
        "runners": ["libretro"],
        "cores": ["nekop2", "np2kai"],
        "default_runner": "libretro",
        "default_core": "nekop2"
    },
    'NEC PC-FX': {
        "runners": ["libretro", "mednafen"],
        "cores": ["mednafen_pcfx"],
        "default_runner": "libretro",
        "default_core": "mednafen_pcfx"
    },
    'Nintendo 3DS': {
        "runners": ["libretro", "citra"],
        "cores": ["citra", "citra2018"],
        "default_runner": "libretro",
        "default_core": "citra"
    },
    'Nintendo 64': {
        "runners": ["libretro", "mupen64plus", "rosaliesmupengui"],
        "cores": ["mupen64plus-next", "parallei_n64"],
        "default_runner": "libretro",
        "default_core": "parallei_n64"
    },
    'Nintendo DS': {
        "runners": ["libretro", "melonds", "desmume"],
        "cores": ["desmume", "desmume2015", "melonds", "melondsds", "noods", "skyemu"],
        "default_runner": "libretro",
        "default_core": "melonds"
    },
    'Nintendo Famicom': {
        "runners": ["libretro", "mednafen"],
        "cores": ["fceumm", "mesen", "nestopia", "quicknes"],
        "default_runner": "libretro",
        "default_core": "mesen"
    },
    'Nintendo Game Boy': {
        "runners": ["libretro"],
        "cores": ["DoubleCherryGB", "gambatte", "gearboy", "mesen-s",  "sameboy", "skyemu", "tgbdual"],
        "default_runner": "libretro",
        "default_core": "gambatte"
    },
    'Nintendo Game Boy Advance': {
        "runners": ["libretro", "mednafen", "mgba"],
        "cores": ["gpsp", "mgba", "skyemu", "vbam", "vba_next"],
        "default_runner": "libretro",
        "default_core": "mgba"
    },
    'Nintendo Game Boy Color': {
        "runners": ["libretro"],
        "cores": ["DoubleCherryGB", "gambatte", "gearboy", "mesen-s", "sameboy", "skyemu", "tgbdual"],
        "default_runner": "libretro",
        "default_core": "gambatte"
    },
    'Nintendo GameCube': {
        "runners": ["libretro", "dolphin"],
        "cores": ["dolphin"],
        "default_runner": "libretro",
        "default_core": "dolphin"
    },
    'Nintendo Pokemon Mini': {
        "runners": ["libretro"],
        "cores": ["pokemini"],
        "default_runner": "libretro",
        "default_core": "pokemini"
    },
    'Nintendo NES': {
        "runners": ["libretro", "mednafen"],
        "cores": ["fceumm", "mesen", "nestopia", "quicknes"],
        "default_runner": "libretro",
        "default_core": "mesen"
    },
    'Nintendo SNES': {
        "runners": ["libretro", "mednafen", "snes9x"],
        "cores": ["bsnes", "bsnes-jg", "bsnes2014_accuracy", "bsnes2014_balanced", "bsnes2014_performance", "bsnes_hd", "bsnes_mercury_accuracy", "bsnes_mercury_balanced", "bsnes_mercury_performance", "mednafen_supafaust", "snes9x", "snes9x2002", "snes9x2005", "snes9x2005_plus", "snes9x2010", "mesen-s"],
        "default_runner": "libretro",
        "default_core": "mednafen_supafaust"
    },
    'Nintendo Super Famicom': {
        "runners": ["libretro", "mednafen"],
        "cores": ["bsnes", "bsnes-jg", "bsnes2014_accuracy", "bsnes2014_balanced", "bsnes2014_performance", "bsnes_hd", "bsnes_mercury_accuracy", "bsnes_mercury_balanced", "bsnes_mercury_performance", "mednafen_supafaust", "snes9x", "snes9x2002", "snes9x2005", "snes9x2005_plus", "snes9x2010", "mesen-s"],
        "default_runner": "libretro",
        "default_core": "mednafen_supafaust"
    },
    'Nintendo Switch': {
        "runners": ["yuzu", "ryujinx"],
        "cores": None,
        "default_runner": "ryujinx",
        "default_core": None
    },
    'Nintendo Virtual Boy': {
        "runners": ["libretro", "mednafen"],
        "cores": ["mednafen_vb"],
        "default_runner": "libretro",
        "default_core": "mednafen_vb"
    },
    'Nintendo Wii': {
        "runners": ["libretro", "dolphin"],
        "cores": ["dolphin"],
        "default_runner": "libretro",
        "default_core": "dolphin"
    },
    'Nintendo Wii U': {
        "runners": ["cemu"],
        "cores": None,
        "default_runner": "cemu",
        "default_core": None
    },
    'Philips CDi': {
        "runners": ["libretro"],
        "cores": ["same_cdi", "cdi2015"],
        "default_runner": "libretro",
        "default_core": "same_cdi"
    },
    'Philips P2000T': {
        "runners": ["libretro"],
        "cores": ["m2000"],
        "default_runner": "libretro",
        "default_core": "m2000"
    },
    'PICO-8': {
        "runners": ["libretro", "pico8"],
        "cores": ["retro8"],
        "default_runner": "libretro",
        "default_core": "retro8"
    },
    'S-CHIP': {
        "runners": ["libretro"],
        "cores": ["jaxe"],
        "default_runner": "libretro",
        "default_core": "jaxe"
    },
    'ScummVM': {
        "runners": ["libretro", "scummvm"],
        "cores": ["scummvm"],
        "default_runner": "scummvm",
        "default_core": None
    },
    'Sega CD': {
        "runners": ["libretro"],
        "cores": ["clownmdemu", "genesis_plus_gx", "genesis_plus_gx_wide", "picodrive"],
        "default_runner": "libretro",
        "default_core": "picodrive"
    },
    'Sega Dreamcast': {
        "runners": ["libretro", "redream", "reicast"],
        "cores": ["flycast"],
        "default_runner": "libretro",
        "default_core": "flycast"
    },
    'Sega Game Gear': {
        "runners": ["libretro"],
        "cores": ["smsplus", "genesis_plus_gx", "genesis_plus_gx_wide", "picodrive", "gearsystem"],
        "default_runner": "libretro",
        "default_core": "picodrive"
    },
    'Sega Genesis': {
        "runners": ["libretro", "dgen"],
        "cores": ["blastem", "clownmdemu", "genesis_plus_gx", "genesis_plus_gx_wide", "picodrive"],
        "default_runner": "libretro",
        "default_core": "picodrive"
    },
    'Sega Mega CD': {
        "runners": ["libretro"],
        "cores": ["clownmdemu", "genesis_plus_gx", "genesis_plus_gx_wide", "picodrive"],
        "default_runner": "libretro",
        "default_core": "picodrive"
    },
    'Sega Mega Drive': {
        "runners": ["libretro"],
        "cores": ["blastem", "clownmdemu", "genesis_plus_gx", "genesis_plus_gx_wide", "picodrive"],
        "default_runner": "libretro",
        "default_core": "picodrive"
    },
    'Sega Master System': {
        "runners": ["libretro", "osmose"],
        "cores": ["smsplus", "genesis_plus_gx", "genesis_plus_gx_wide", "picodrive", "gearsystem"],
        "default_runner": "libretro",
        "default_core": "picodrive"
    },
    'Sega Naomi': {
        "runners": ["libretro", "redream", "reicast"],
        "cores": ["flycast"],
        "default_runner": "libretro",
        "default_core": "flycast"
    },
    'Sega PICO': {
        "runners": ["libretro"],
        "cores": ["picodrive"],
        "default_runner": "libretro",
        "default_core": "picodrive"
    },
    'Sega Saturn': {
        "runners": ["libretro", "mednafen"],
        "cores": ["kronos", "mednafen_saturn", "yabasanshiro", "yabause"],
        "default_runner": "libretro",
        "default_core": "mednafen_saturn"
    },
    'Sega SG-1000': {
        "runners": ["libretro"],
        "cores": ["gearsystem"],
        "default_runner": "libretro",
        "default_core": "gearsystem"
    },
    'Sega Titan Video': {
        "runners": ["libretro"],
        "cores": ["kronos"],
        "default_runner": "libretro",
        "default_core": "kronos"
    },
    'Sharp X1': {
        "runners": ["libretro"],
        "cores": ["x1"],
        "default_runner": "libretro",
        "default_core": "x1"    
    },
    'Sharp X68000': {
        "runners": ["libretro"],
        "cores": ["px68k"],
        "default_runner": "libretro",
        "default_core": "px68k" 
    },
    'Sinclair ZX81': {
        "runners": ["libretro"],
        "cores": ["81"],
        "default_runner": "libretro",
        "default_core": "81" 
    },
    'Sinclair ZX Spectrum': {
        "runners": ["libretro", "speccy"],
        "cores": ["fuse"],
        "default_runner": "libretro",
        "default_core": "fuse" 
    },
    'SNK Neo Geo AES': {
        "runners": ["libretro"],
        "cores": ["fbalpha2012_neogeo", "fbneo_neogeo"],
        "default_runner": "libretro",
        "default_core": "fbneo_neogeo"
    },
    'SNK Neo Geo CD': {
        "runners": ["libretro"],
        "cores": ["fbalpha2012_neogeo", "fbneo_neogeo"],
        "default_runner": "libretro",
        "default_core": "fbneo_neogeo"
    },
    'SNK Neo Geo MVS': {
        "runners": ["libretro"],
        "cores": ["fbalpha2012_neogeo", "fbneo_neogeo"],
        "default_runner": "libretro",
        "default_core": "fbneo_neogeo"
    },
    'SNK Neo Geo Pocket': {
        "runners": ["libretro", "mednafen"],
        "cores": ["mednafen_ngp", "race"],
        "default_runner": "libretro",
        "default_core": "mednafen_ngp"
    },
    'SNK Neo Geo Pocket Color': {
        "runners": ["libretro", "mednafen"],
        "cores": ["mednafen_ngp", "race"],
        "default_runner": "libretro",
        "default_core": "mednafen_ngp"
    },
    'Sony PlayStation': {
        "runners": ["libretro", "mednafen", "duckstation"],
        "cores": ["mednafen_psx", "mednafen_psx_hw", "pcsx_rearmed", "swanstation"],
        "default_runner": "libretro",
        "default_core": "mednafen_psx_hw"
    },
    'Sony PlayStation 2': {
        "runners": ["libretro", "pcsx2"],
        "cores": ["pcsx2"],
        "default_runner": "libretro",
        "default_core": "pcsx2"
    },
    'Sony PlayStation 3': {
        "runners": ["rpcs3"],
        "cores": None,
        "default_runner": "rpcs3",
        "default_core": None
    },
    'Sony PlayStation Portable': {
        "runners": ["libretro", "ppsspp"],
        "cores": ["ppsspp"],
        "default_runner": "libretro",
        "default_core": "ppsspp"
    },
    'Sony PlayStation Vita': {
        "runners": ["vita3k"],
        "cores": None,
        "default_runner": "vita3k",
        "default_core": None
    },
    'Tamagachi P1': {
        "runners": ["libretro"],
        "cores": ["tamalibretro"],
        "default_runner": "libretro",
        "default_core": "tamalibretro"
    },
    'Texas Instruments TI-83': {
        "runners": ["libretro"],
        "cores": ["numero"],
        "default_runner": "libretro",
        "default_core": "numero"
    },
    'Thomson MO/TO': {
        "runners": ["libretro"],
        "cores": ["theodore"],
        "default_runner": "libretro",
        "default_core": "theodore"
    },
    'TIC-80': {
        "runners": ["libretro"],
        "cores": ["tic80"],
        "default_runner": "libretro",
        "default_core": "tic80"
    },
    'Uzebox': {
        "runners": ["libretro"],
        "cores": ["uzem"],
        "default_runner": "libretro",
        "default_core": "uzem"
    },
    'VaporSpec': {
        "runners": ["libretro"],
        "cores": ["vaporspec"],
        "default_runner": "libretro",
        "default_core": "vaporspec"
    },
    'Vircon32': {
        "runners": ["libretro"],
        "cores": ["vircon32"],
        "default_runner": "libretro",
        "default_core": "vircon32"
    },
    'WASM-4': {
        "runners": ["libretro"],
        "cores": ["wasm4"],
        "default_runner": "libretro",
        "default_core": "wasm4"
    },
    'Watara Supervision': {
        "runners": ["libretro"],
        "cores": ["potator"],
        "default_runner": "libretro",
        "default_core": "potator"
    },
    'XO-CHIP': {
        "runners": ["libretro"],
        "cores": ["jaxe"],
        "default_runner": "libretro",
        "default_core": "jaxe"
    }
}