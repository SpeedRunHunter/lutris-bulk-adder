#!/usr/bin/env python3

import sys
import yaml
import sqlite3
from datetime import datetime, timezone

from constants import DEFAULT_ROM_FILE_EXTS, KEY_ERR_MSG, ARG_ERR_MSG
from lib import *

def main():
    parser = argparse.ArgumentParser(description='Scan a directory for ROMs to add to Lutris.', add_help=False)

    # Custom help - to prettify the platform list printing
    parser.add_argument('-h', "--help", action='store_true',
                        help="show this help message and exit")
    
    # Required arguments
    parser.add_argument('-p', '--platform', type=str, choices=PLATFORMS,
                        help='Platform name.')
    parser.add_argument('-d', '--directory', type=directory,
                        help='Directory to scan for games.')
    
    # Optional arguments
    parser.add_argument('-r', '--runner', type=str,
                        help='Name of Lutris runner to use.')
    parser.add_argument('-c', '--core', type=str,
                        help='Name of libretro core to use.\nWill error out if given platform doesn\'t have Retroarch as an available runner')

    # Lutris paths
    parser.add_argument('-ld', '--lutris-database', type=str,
                        default=os.path.join(os.path.expanduser('~'), '.local', 'share', 'lutris', 'pga.db'),
                        help='Path to the Lutris SQLite database.')
    parser.add_argument('-ly', '--lutris-yml-dir', type=directory,
                        default=os.path.join(os.path.expanduser('~'), '.local', 'share', 'lutris', 'games'),
                        help='Directory containing Lutris yml files.')
    parser.add_argument('-lg', '--lutris-game-dir', type=directory,
                        default=os.path.join(os.path.expanduser('~'), 'Games'),
                        help='Lutris games install dir.')

    # New options
    parser.add_argument('-i', "--platform-info", type=str,
                        help='List information for a given platform (runners, cores if libretro is an option and defaults)')
    parser.add_argument('-a', "--dump-platform-info", action='store_true',
                        help='Dump all available information related to every and all known platforms')
    
    # Other options
    parser.add_argument('-f', '--file-types', type=str, nargs='*', default=DEFAULT_ROM_FILE_EXTS,
                        help='Space-separated list of file types to scan for.')
    parser.add_argument('-o', '--game-options', type=option_list,
                        help='Additional options to write to the YAML file under the "game" key (e.g. platform number as required for Dolphin)')
    parser.add_argument('-s', '--strip-filename', nargs='*', default=[],
                        help='Space-separated list of strings to strip from filenames when generating game names.')
    parser.add_argument('-n', '--no-write', action='store_true',
                        help="""
Do not write YML files or alter Lutris database, only print data to be written out to stdout. (i.e. dry run)
    """)

    args = parser.parse_args()

    help = args.help
    if help:
        print("""usage: lutris_bulk_adder.py [-h] 
                            -p PLATFORM (see choices below) -d DIRECTORY
                            [-r RUNNER] [-c CORE]
                            [-ld LUTRIS_DATABASE] [-ly LUTRIS_YML_DIR] [-lg LUTRIS_GAME_DIR]
                            [-i PLATFORM_INFO] [-a]
                            [-f [FILE_TYPES ...]] [-o GAME_OPTIONS] [-s [STRIP_FILENAME ...]] [-n]

Scan a directory for ROMs to add to Lutris.

options:
  -h, --help            show this help message and exit
              
  -d, --directory DIRECTORY
                        Directory to scan for games.
  -p, --platform PLATFORM
                        Platform name.
                        The following platforms are available:
                        {}
                        The script will exit with an error if the given platform is unknown by the built-in dictionary.
              
  -r, --runner RUNNER   Name of Lutris runner to use.
                        The script will exit with an error if the given runner is unknown by the built-in dictionary for the specified platform.
  -c, --core CORE
                        Name of libretro core to use.
                        The script will ignore this value if libretro isn't selected as a runner for the platform. 
                        The script will exit with an error if the given platform the core is unknown by the built-in dictionary for the specified platform.
              
  -ld, --lutris-database LUTRIS_DATABASE
                        Path to the Lutris SQLite database.
  -ly, --lutris-yml-dir LUTRIS_YML_DIR
                        Directory containing Lutris yml files.
  -lg, --lutris-game-dir LUTRIS_GAME_DIR
                        Lutris games install dir.
              
  -i, --platform-info PLATFORM
                        List information for a given platform (runners, cores if libretro is an option and defaults)
  -a, --dump-platform-info
                        Dump all available information related to every and all known platforms
              
  -f, --file-types [FILE_TYPES ...]
                        Space-separated list of file types to scan for.
  -o, --game-options GAME_OPTIONS
                        Additional options to write to the YAML file under the "game" key (e.g. platform number as required for Dolphin)
  -s, --strip-filename [STRIP_FILENAME ...]
                        Space-separated list of strings to strip from filenames when generating game names.
  -n, --no-write        Do not write YML files or alter Lutris database, only print data to be written out to stdout. (i.e. dry run)"""
              .format(format_list(list(PLATFORMS.keys()), '\t\t\t', multiple_items_per_line=True)))
        sys.exit(0)

    # Dump all information related to platforms
    dump_platform_info = args.dump_platform_info
    if dump_platform_info:
        for platform in list(PLATFORMS.keys()):
            print_info_for_platform(platform)
        sys.exit(0)

    # Print information related to a specific input platform
    platform_info = args.platform_info
    if platform_info:
        try:
            print_info_for_platform(platform_info)
        except KeyError as err:
            print(KEY_ERR_MSG.format("print information for", err))
            sys.exit(-1)
        sys.exit(0);
    
    # Ensure platform and directory is supplied from arguments
    arg_platform = args.platform
    dir = args.directory
    if not arg_platform or not dir:
        print("ERROR: Missing {} argument inputs; they are required for this script to function"
              .format("platform and directory" if not arg_platform and not dir else ("platform" if not arg_platform else "directory")),
              file=sys.stderr)
        sys.exit(-1)

    # Ensure platform can be found in the dictionary
    platform = ''
    try:
        platform = PLATFORMS[arg_platform]
    except KeyError as err:
        print(KEY_ERR_MSG.format("find", err))
        sys.exit(-1)

    # Safety double check to see if somehow platform 
    # ended up being empty for some reason still
    if not platform:
        print("""There was an unknown error trying to grab the exact platform from the built-in dictionary.
              
This shouldn't have happened, because in such event, the attempt at getting an unknown key value platform from the dictionary will throw a Python KeyError which is handled in code via an error message and the program should be exiting right then and there.
              
If you see this message, then you have found a bug.""")
        sys.exit(-999)

    # setup runner
    # use default runner first
    # if available use arg provided runner
    # test if runner is known for this platform
    runner = platform.default_runner
    arg_runner = args.runner
    if arg_runner:
        if arg_runner not in platform.runners:
            print(ARG_ERR_MSG.format(selection = "runner", arg = arg_runner))
            sys.exit(-1)
        runner = arg_runner

    # setup core
    # check if selected runner is libretro
    # use default core first
    # if available use arg provided core
    # test if core is known for this platform
    core = None
    if runner == 'libretro':
        core = platform.default_core
        arg_core = args.core
        if arg_core:
            if arg_core not in platform.cores:
                print(ARG_ERR_MSG.format(selection = "runner", arg = arg_core))
            core = arg_core
    
    # Lutris SQLite db
    if os.path.isfile(args.lutris_database):
        conn = sqlite3.connect(args.lutris_database)
        cur = conn.cursor()
    else:
        print("Error opening database {}".format(args.lutris_database))
        sys.exit(1)

    # Get max game ID to increment from
    try:
        cur.execute("select max(id) from games")
    except sqlite3.OperationalError:
        print("SQLite error, is {} a valid Lutris database?".format(args.lutris_database))
        sys.exit(1)

    # credit to @ronicaltech for this patch
    # link to pr on original repo: https://github.com/hwangeug/lutris-bulk-adder/pull/4
    new_id = cur.fetchone()[0]
    if new_id is None:
        new_id = 0

    game_id = new_id + 1
    
    # Scan dir for ROMs
    files = scan_for_filetypes(dir, args.file_types)
    for file in files:
        ts = int(datetime.now(timezone.utc).timestamp())

        # Generate game name and slug from filename
        game = re.sub(r"\..*", "", os.path.basename(file))  # Strip extension
        for token in args.strip_filename:
            game = game.replace(token, "")                  # Strip tokens

        # credit to @ronicaltech for this patch
        # link to pr on his own repo: https://github.com/ronicaltech/lutris-bulk-adder/pull/2
        # small fix by @speedrunhunter:
        # regex string was missing the prefixed 'r' character
        # which would result in a warning at script runtime
        game = re.sub(r"\(.*?\)|\[.*?\]","",game)            # Strip any textin () or []

        game = re.sub(r"\s+", " ", game).strip(" ")         # Remove excess whitespace

        slug = re.sub(r"[^0-9A-Za-z']", " ", game)          # Split on nonword characters
        slug = slug.replace("'", "")                        # Strip apostrophe
        slug = re.sub(r"\s+", "-", slug).strip("-").lower() # Replace whitespace with dashes

        # Data for YML file
        config_file = '{slug}-{ts}'.format(slug=slug, ts=ts)
        config_file_path = os.path.join(args.lutris_yml_dir, "{}.yml".format(config_file))
        config = {
            "game": {
                "main_file": file
            },
        }
        
        if core:
            config['game']['core'] = core

        if args.game_options is not None:
            config['game'].update(args.game_options)

        # Data for Lutris DB
        values = {
            "id": game_id,
            "name": game,
            "sortname": None,
            "slug": slug,
            "installer_slug": None,
            "parent_slug": None,
            "platform": arg_platform,
            "runner": runner,
            "executable": None,
            "directory": args.lutris_game_dir,
            "updated": None,
            "lastplayed": 0,
            "installed": 1,
            "installed_at": ts,
            "year": None,
            "configpath": config_file,
            "has_custom_banner": None,
            "has_custom_icon": None,
            "has_custom_coverart_big": None,
            "playtime": None,
            "service": None,
            "service_id": None,
            "discord_id": None
        }

        # Output to console
        if args.no_write:
            print("file: {}".format(file))
            print("SQLite:\n{}".format(values)),
            print("YML at {ymlfile}:\n{config}\n".format(ymlfile=config_file_path,
                                                         config=yaml.dump(config, default_flow_style=False)))
        
        # Write to DB/filesystem
        else:
            with open(config_file_path, 'w') as f:
                yaml.dump(config, f, default_flow_style=False)
            
            query = "INSERT INTO games ({columns}) VALUES ({placeholders})".format(
                columns = ','.join(values.keys()),
                placeholders = ','.join('?' * len(values))
            )

            cur.execute(query, list(values.values()))
            conn.commit()

        game_id += 1
        
    print("Success? Check on Lutris now")


if __name__ == '__main__':
    main()
