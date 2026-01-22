from lutris_bulk_adder.classes import PlatformData

# I plan to put this into the platforms dict for each platform

DEFAULT_ROM_FILE_EXTS = ['iso', 'zip', 'sfc', 'gba', 'gbc', 'gb', 'md', 'n64',
                         'nes', '32x', 'gg', 'sms', 'bin', 'chd']

# A single place for the message of the key error that may occour
# when trying to lookup a platform from the dictionary

KEY_ERR_MSG = """Error trying to {} platform {}; did you make a typo perhaps?

Also note that Python is case-sensitive with dictionaries, so you must ensure proper case format in your input platform's name.
        For example, instead of 'sega genesis' try 'Sega Genesis'."""
        
ARG_ERR_MSG = "Error trying to find the specified {selection} {arg} in the platform's list of {selection} known by the script; did you make a typo perhaps?"

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
    '3DO': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['opera'], 
		default_core='opera'
    ),
    'Amstrad CPC': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['cap32', 'crocods'], 
		default_core='cap32'
    ),
    'Amstrad GX4000': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['cap32'], 
		default_core='cap32'
    ),
    'Arcade': PlatformData(
		runners=['mame', 'libretro'], 
		default_runner='libretro', 
		cores=[
            'daphne', 'dice', 'fbalpha2012', 
            'fbneo', 'hbmame', 'mame2000', 
            'mame2003', 'mame2003_midway', 
            'mame2003_plus', 'mame2009', 
            'mame2010', 'mame2015', 'mame2016', 
            'mame', 'mamearcade'
        ], 
		default_core='mame'
    ),
    'Arduboy': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['ardens', 'arduous'], 
		default_core='ardens'
    ),
    'Atari 2600': PlatformData(
		runners=['libretro', 'stella'], 
		default_runner='libretro', 
		cores=['stella', 'stella2014', 'stella2023'], 
		default_core='stella'
    ),
    'Atari 5200': PlatformData(
		runners=['libretro', 'a5200'], 
		default_runner='libretro', 
		cores=['atari800', 'a5200'], 
		default_core='atari800'
    ),
    'Atari 7800': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['prosystem'], 
		default_core='prosystem'
    ),
    'Atari 400': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['atari800'], 
		default_core='atari800'
    ),
    'Atari 800': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['atari800'], 
		default_core='atari800'
    ),
    'Atari 600XL': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['atari800'], 
		default_core='atari800'
    ),
    'Atari 800XL': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['atari800'], 
		default_core='atari800'
    ),
    'Atari 130XE': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['atari800'], 
		default_core='atari800'
    ),
    'Atari Jaguar': PlatformData(
		runners=['libretro', 'virtualjaguar'], 
		default_runner='libretro', 
		cores=['virtualjaguar'], 
		default_core='virtualjaguar'
    ),
    'Atari Lynx': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['handy', 'holani', 'mednafen_lynx'], 
		default_core='mednafen_lynx'
    ),
    'Atari ST': PlatformData(
		runners=['libretro', 'hatari'], 
		default_runner='libretro', 
		cores=['hatari'], 
		default_core='hatari'
    ),
    'Atari STE': PlatformData(
		runners=['libretro', 'hatari'], 
		default_runner='libretro', 
		cores=['hatari'], 
		default_core='hatari'
    ),
    'Atari TT': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['hatari'], 
		default_core='hatari'
    ),
    'Atari Falcon': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['hatari'], 
		default_core='hatari'
    ),
    'Bandai WonderSwan': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['mednafen_wswan'], 
		default_core='mednafen_wswan'
    ),
    'Bandai WonderSwan Color': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['mednafen_wswan'], 
		default_core='mednafen_wswan'
    ),
    'Capcom CPS-1': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['fbalpha2012_cps1', 'fbneo_cps12'], 
		default_core='fbneo_cps12'
    ),
    'Capcom CPS-2': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['fbalpha2012_cps2', 'fbneo_cps12'], 
		default_core='fbneo_cps12'
    ),
    'Capcom CPS-3': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['fbalpha2012_cps3'], 
		default_core='fbalpha2012_cps3'
    ),
    'ChaiLove': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['chailove'], 
		default_core='chailove'
    ),
    'CHIP-8': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['jaxe'], 
		default_core='jaxe'
    ),
    'ColecoVision': PlatformData(
		runners=['libretro', 'colem'], 
		default_runner='libretro', 
		cores=['gearcoleco', 'jollycv'], 
		default_core='jollycv'
    ),
    'CreatiVision': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['jollycv'], 
		default_core='jollycv'
    ),
    'MyVision': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['jollycv'], 
		default_core='jollycv'
    ),
    'Commodore Amiga': PlatformData(
		runners=['libretro', 'fsuae'], 
		default_runner='libretro', 
		cores=['puae', 'puae2021'], 
		default_core='puae'
    ),
    'Commodore 128': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_x128'], 
		default_core=None
    ),
    'Commodore 16/Plus/4': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_xplus4'], 
		default_core=None
    ),
    'Commodore 64': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_x64', 'vice_x64sc', 'x64sdl'], 
		default_core=None
    ),
    'Commodore 64 Direct-to-TV': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_x64dtv'], 
		default_core=None
    ),
    'Commodore 64 SuperCPU': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_xscpu64'], 
		default_core=None
    ),
    'Commodore CBM-II 5x0': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_xcbm5x0'], 
		default_core=None
    ),
    'Commodore CBM-II 6x0': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_xcbm2'], 
		default_core=None
    ),
    'Commodore PET': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_xpet'], 
		default_core=None
    ),
    'Commodore VIC-20': PlatformData(
		runners=['libretro', 'vice'], 
		default_runner='vice', 
		cores=['vice_xvic'], 
		default_core=None
    ),
    'Elektronika BK-0010': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['bk'], 
		default_core='bk'
    ),
    'Elektronika BK-0010.01': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['bk'], 
		default_core='bk'
    ),
    'Elektronika BK-0011 (M)': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['bk'], 
		default_core='bk'
    ),
    'Enterprise 64': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['ep128emu'], 
		default_core='ep128emu'
    ),
    'Enterprise 128': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['ep128emu'], 
		default_core='ep128emu'
    ),
    'Fairchild Channel F': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['freechaf'], 
		default_core='freechaf'
    ),
    'GAM4980': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['gam4980'], 
		default_core='gam4980'
    ),
    'GCE Vectrex': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['vecx'], 
		default_core='vecx'
    ),
    'Infocom Z-Machine': PlatformData(
		runners=['libretro', 'frotz'], 
		default_runner='libretro', 
		cores=['mojozork'], 
		default_core='mojozork'
    ),
    'Java ME': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['squirreljme'], 
		default_core='squirreljme'
    ),
    'Magnavox Odyssey 2': PlatformData(
		runners=['libretro', 'o2em'], 
		default_runner='libretro', 
		cores=['o2em'], 
		default_core='o2em'
    ),
    'Philips Videopac+': PlatformData(
		runners=['libretro', 'o2em'], 
		default_runner='libretro', 
		cores=['o2em'], 
		default_core='o2em'
    ),
    'Mattel Intellivision': PlatformData(
		runners=['libretro', 'jzintv'], 
		default_runner='libretro', 
		cores=['freeintv'], 
		default_core='freeintv'
    ),
    'Mega Duck': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['sameduck'], 
		default_core='sameduck'
    ),
    'Cougar Boy': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['sameduck'], 
		default_core='sameduck'
    ),
    'MS-DOS': PlatformData(
		runners=['libretro', 'dosbox', '86box', 'pcem'], 
		default_runner='libretro', 
		cores=['dosbox_core', 'dosbox_pure', 'dosbox_svn', 'virtualxt'], 
		default_core='dosbox_core'
    ),
    'Microsoft MSX': PlatformData(
		runners=['libretro', 'openmsx'], 
		default_runner='libretro', 
		cores=['fmsx'], 
		default_core='fmsx'
    ),
    'Microsoft MSX2': PlatformData(
		runners=['libretro', 'openmsx'], 
		default_runner='libretro', 
		cores=['fmsx'], 
		default_core='fmsx'
    ),
    'Microsoft MSX2+': PlatformData(
		runners=['libretro', 'openmsx'], 
		default_runner='libretro', 
		cores=['fmsx'], 
		default_core='fmsx'
    ),
    'Microsoft XBOX': PlatformData(
		runners=['xemu'], 
		default_runner='xemu', 
		cores=None, 
		default_core=None
    ),
    'NEC PC Engine': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['geargrafx', 'mednafen_pce', 'mednafen_pce_fast'], 
		default_core='mednafen_pce'
    ),
    'NEC PC Engine CD': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['geargrafx', 'mednafen_pce', 'mednafen_pce_fast'], 
		default_core='mednafen_pce'
    ),
    'NEC PC Engine SuperGrafx': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['geargrafx', 'mednafen_pce', 'mednafen_supergrafx'], 
		default_core='mednafen_pce'
    ),
    'NEC PC-8000': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['quasi88'], 
		default_core='quasi88'
    ),
    'NEC PC-8800': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['quasi88'], 
		default_core='quasi88'
    ),
    'NEC PC-98': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['nekop2', 'np2kai'], 
		default_core='nekop2'
    ),
    'NEC PC-FX': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['mednafen_pcfx'], 
		default_core='mednafen_pcfx'
    ),
    'Nintendo 3DS': PlatformData(
		runners=['libretro', 'citra'], 
		default_runner='libretro', 
		cores=['citra', 'citra2018'], 
		default_core='citra'
    ),
    'Nintendo 64': PlatformData(
		runners=['libretro', 'mupen64plus', 'rosaliesmupengui'], 
		default_runner='libretro', 
		cores=['mupen64plus-next', 'parallei_n64'], 
		default_core='parallei_n64'
    ),
    'Nintendo DS': PlatformData(
		runners=['libretro', 'melonds', 'desmume'], 
		default_runner='libretro', 
		cores=[
            'desmume', 'desmume2015', 'melonds', 
            'melondsds', 'noods', 'skyemu'
        ], 
		default_core='melonds'
    ),
    'Nintendo Famicom': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['fceumm', 'mesen', 'nestopia', 'quicknes'], 
		default_core='mesen'
    ),
    'Nintendo Game Boy': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=[
            'DoubleCherryGB', 'gambatte', 'gearboy', 
            'mesen-s', 'sameboy', 'skyemu', 'tgbdual'
        ], 
		default_core='gambatte'
    ),
    'Nintendo Game Boy Advance': PlatformData(
		runners=['libretro', 'mednafen', 'mgba'], 
		default_runner='libretro', 
		cores=['gpsp', 'mgba', 'skyemu', 'vbam', 'vba_next'], 
		default_core='mgba'
    ),
    'Nintendo Game Boy Color': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=[
            'DoubleCherryGB', 'gambatte', 'gearboy', 
            'mesen-s', 'sameboy', 'skyemu', 'tgbdual'
        ], 
		default_core='gambatte'
    ),
    'Nintendo GameCube': PlatformData(
		runners=['libretro', 'dolphin'], 
		default_runner='libretro', 
		cores=['dolphin'], 
		default_core='dolphin'
    ),
    'Nintendo Pokemon Mini': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['pokemini'], 
		default_core='pokemini'
    ),
    'Nintendo NES': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['fceumm', 'mesen', 'nestopia', 'quicknes'], 
		default_core='mesen'
    ),
    'Nintendo SNES': PlatformData(
		runners=['libretro', 'mednafen', 'snes9x'], 
		default_runner='libretro', 
		cores=[
            'bsnes', 'bsnes-jg', 'bsnes2014_accuracy', 
            'bsnes2014_balanced', 'bsnes2014_performance', 
            'bsnes_hd', 'bsnes_mercury_accuracy', 
            'bsnes_mercury_balanced', 'bsnes_mercury_performance', 
            'mednafen_supafaust', 'snes9x', 'snes9x2002', 
            'snes9x2005', 'snes9x2005_plus', 'snes9x2010', 'mesen-s'
        ], 
		default_core='mednafen_supafaust'
    ),
    'Nintendo Super Famicom': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro',
		cores=[
            'bsnes', 'bsnes-jg', 'bsnes2014_accuracy', 
            'bsnes2014_balanced', 'bsnes2014_performance', 
            'bsnes_hd', 'bsnes_mercury_accuracy', 
            'bsnes_mercury_balanced', 'bsnes_mercury_performance', 
            'mednafen_supafaust', 'snes9x', 'snes9x2002', 
            'snes9x2005', 'snes9x2005_plus', 'snes9x2010', 'mesen-s'
        ], 
		default_core='mednafen_supafaust'
    ),
    'Nintendo Switch': PlatformData(
		runners=['yuzu', 'ryujinx'], 
		default_runner='ryujinx', 
		cores=None, 
		default_core=None
    ),
    'Nintendo Virtual Boy': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['mednafen_vb'], 
		default_core='mednafen_vb'
    ),
    'Nintendo Wii': PlatformData(
		runners=['libretro', 'dolphin'], 
		default_runner='libretro', 
		cores=['dolphin'], 
		default_core='dolphin'
    ),
    'Nintendo Wii U': PlatformData(
		runners=['cemu'], 
		default_runner='cemu', 
		cores=None, 
		default_core=None
    ),
    'Philips CDi': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['same_cdi', 'cdi2015'], 
		default_core='same_cdi'
    ),
    'Philips P2000T': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['m2000'], 
		default_core='m2000'
    ),
    'PICO-8': PlatformData(
		runners=['libretro', 'pico8'], 
		default_runner='libretro', 
		cores=['retro8'], 
		default_core='retro8'
    ),
    'S-CHIP': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['jaxe'], 
		default_core='jaxe'
    ),
    'ScummVM': PlatformData(
		runners=['libretro', 'scummvm'], 
		default_runner='scummvm', 
		cores=['scummvm'], 
		default_core=None
    ),
    'Sega 32X': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['picodrive'], 
		default_core='picodrive'
	),
    'Sega CD': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['clownmdemu', 'genesis_plus_gx', 'genesis_plus_gx_wide', 'picodrive'], 
		default_core='picodrive'
    ),
    'Sega Dreamcast': PlatformData(
		runners=['libretro', 'redream', 'reicast'], 
		default_runner='libretro', 
		cores=['flycast'], 
		default_core='flycast'
    ),
    'Sega Game Gear': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['smsplus', 'genesis_plus_gx', 'genesis_plus_gx_wide', 'picodrive', 'gearsystem'], 
		default_core='picodrive'
    ),
    'Sega Genesis': PlatformData(
		runners=['libretro', 'dgen'], 
		default_runner='libretro', 
		cores=['blastem', 'clownmdemu', 'genesis_plus_gx', 'genesis_plus_gx_wide', 'picodrive'], 
		default_core='picodrive'
    ),
    'Sega Mega CD': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['clownmdemu', 'genesis_plus_gx', 'genesis_plus_gx_wide', 'picodrive'], 
		default_core='picodrive'
    ),
    'Sega Mega Drive': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['blastem', 'clownmdemu', 'genesis_plus_gx', 'genesis_plus_gx_wide', 'picodrive'], 
		default_core='picodrive'
    ),
    'Sega Master System': PlatformData(
		runners=['libretro', 'osmose'], 
		default_runner='libretro', 
		cores=['smsplus', 'genesis_plus_gx', 'genesis_plus_gx_wide', 'picodrive', 'gearsystem'], 
		default_core='picodrive'
    ),
    'Sega Naomi': PlatformData(
		runners=['libretro', 'redream', 'reicast'], 
		default_runner='libretro', 
		cores=['flycast'], 
		default_core='flycast'
    ),
    'Sega PICO': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['picodrive'], 
		default_core='picodrive'
    ),
    'Sega Saturn': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['kronos', 'mednafen_saturn', 'yabasanshiro', 'yabause'], 
		default_core='mednafen_saturn'
    ),
    'Sega SG-1000': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['gearsystem'], 
		default_core='gearsystem'
    ),
    'Sega Titan Video': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['kronos'], 
		default_core='kronos'
    ),
    'Sharp X1': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['x1'], 
		default_core='x1'
    ),
    'Sharp X68000': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['px68k'], 
		default_core='px68k'
    ),
    'Sinclair ZX81': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['81'], 
		default_core='81'
    ),
    'Sinclair ZX Spectrum': PlatformData(
		runners=['libretro', 'speccy'], 
		default_runner='libretro', 
		cores=['fuse'], 
		default_core='fuse'
    ),
    'SNK Neo Geo AES': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['fbalpha2012_neogeo', 'fbneo_neogeo'], 
		default_core='fbneo_neogeo'
    ),
    'SNK Neo Geo CD': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['fbalpha2012_neogeo', 'fbneo_neogeo'], 
		default_core='fbneo_neogeo'
    ),
    'SNK Neo Geo MVS': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['fbalpha2012_neogeo', 'fbneo_neogeo'], 
		default_core='fbneo_neogeo'
    ),
    'SNK Neo Geo Pocket': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['mednafen_ngp', 'race'], 
		default_core='mednafen_ngp'
    ),
    'SNK Neo Geo Pocket Color': PlatformData(
		runners=['libretro', 'mednafen'], 
		default_runner='libretro', 
		cores=['mednafen_ngp', 'race'], 
		default_core='mednafen_ngp'
    ),
    'Sony PlayStation': PlatformData(
		runners=['libretro', 'mednafen', 'duckstation'], 
		default_runner='libretro', 
		cores=['mednafen_psx', 'mednafen_psx_hw', 'pcsx_rearmed', 'swanstation'], 
		default_core='mednafen_psx_hw'
    ),
    'Sony PlayStation 2': PlatformData(
		runners=['libretro', 'pcsx2'], 
		default_runner='libretro', 
		cores=['pcsx2'], 
		default_core='pcsx2'
    ),
    'Sony PlayStation 3': PlatformData(
		runners=['rpcs3'], 
		default_runner='rpcs3', 
		cores=None, 
		default_core=None
    ),
    'Sony PlayStation Portable': PlatformData(
		runners=['libretro', 'ppsspp'], 
		default_runner='libretro', 
		cores=['ppsspp'], 
		default_core='ppsspp'
    ),
    'Sony PlayStation Vita': PlatformData(
		runners=['vita3k'], 
		default_runner='vita3k', 
		cores=None, 
		default_core=None
    ),
    'Tamagachi P1': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['tamalibretro'], 
		default_core='tamalibretro'
    ),
    'Texas Instruments TI-83': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['numero'], 
		default_core='numero'
    ),
    'Thomson MO/TO': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['theodore'], 
		default_core='theodore'
    ),
    'TIC-80': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['tic80'], 
		default_core='tic80'
    ),
    'Uzebox': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['uzem'], 
		default_core='uzem'
    ),
    'VaporSpec': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['vaporspec'], 
		default_core='vaporspec'
    ),
    'Vircon32': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['vircon32'], 
		default_core='vircon32'
    ),
    'WASM-4': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['wasm4'], 
		default_core='wasm4'
    ),
    'Watara Supervision': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['potator'], 
		default_core='potator'
    ),
    'XO-CHIP': PlatformData(
		runners=['libretro'], 
		default_runner='libretro', 
		cores=['jaxe'], 
		default_core='jaxe'
    )
}