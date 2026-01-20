#!/usr/bin/env python3

import re
import os
import sys
import argparse
import yaml
import sqlite3
from datetime import datetime

from constants import PLATFORMS, DEFAULT_ROM_FILE_EXTS

def option_list(options: str):
    """Option list type for argparse

    Args:
        options: String containing space-delimited key-value pairs in the form <name>=<value>
    
    Returns:
        dictionary containing parsed options

    Raises:
        argparse.ArgumentTypeError: Argument is formatted incorrectly
    """

    pairs_raw = re.split(r"\s+", options)
    pairs = {}
    for pair in pairs_raw:
        parsed = pair.split('=', maxsplit=1)
        if len(parsed) < 2:
            raise argparse.ArgumentTypeError("Option \"{}\" is not formatted correctly".format(pair))
        
        pairs.update({parsed[0]: parsed[1]})
    
    return(pairs)


def directory(path: str):
    """Directory type for argparse

    Args:
        path: directory path
    
    Returns:
        directory path

    Raises:
        argparse.ArgumentTypeError: Argument is not a directory
    """
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError("{} is not a directory".format(path))
    else:
        return path


def scan_for_filetypes(dir: directory, types: list[str]):
    """Scans a directory for all files matching a list of extension types.

    Args:
        dir: Directory location to scan.
        types: List of file extensions to include.

    Returns:
        A list of file paths.

    Raises:
        FileNotFoundError: Directory does not exist.
    """

    files = set()
    with os.scandir(dir) as it:
        for entity in it:
            if entity.is_file():
                fn_delimited = entity.name.split(os.extsep)
                try:
                    if(fn_delimited[len(fn_delimited) - 1].lower() in types):
                        files.add(os.path.join(dir, entity.name))
                except IndexError:
                    pass
    return files

def split_list(list: list, nested_list_size: int):
    """Takes a list and converts it into a list of nested lists with n number of items in said nested lists.\n\nThis function will take n number of items from the original list, put them into a new list of n items, and nest that into a new list that will be returned. Should the original list run out of items before the n amount of items is achieved, the nested list will be n-k items smaller than required, where k is the amount of items missing.

    Args:
        list: The combined list of items to be converted.
        nested_list_size: The size of the nested lists.

    Returns:
        ret_list: A list of nested lists of the original items.
    """

    idx = 0
    og_list_len = list.__len__()
    ret_list = []
    
    while idx < og_list_len:
        nested_list = []
        for i in range (idx, min(idx + nested_list_size, og_list_len)):
            nested_list.append(list[i])
        ret_list.append(nested_list)
        idx += nested_list_size

    return ret_list

def format_list(list: list, format_str: str, print_multiple_lines = True, multiple_items_per_line = False, num_items_per_line = 5, format_between_items = ', '):
    """Takes a list and formats it into a string according to some requirements, like the format text, multiple items per line output and how many items should be put into one line

    Note:
        DO NOT supply a line feed ('\\n') to the function in the format_str parameter. I mean, I suppose you can, but this function assumes the results NEED to be returned in multiple lines, therefore the function adds the line feed ('\\n'). Unless you need multiple lines between items, you mustn't supply a line feed ('\\n').
    
    Args:
        Required:
            list: List of items to convert and format.\n
            format_str: The format based on which the items in the list will be joined together.
        Optional:
            print_multiple_lines: Whether or not the function should print everything into individual lines. My original use case dictated to have the result be in multiple lines. But realizing that it may not be desirable to do that, and also relying on the other coder to supply a line feed ('\\n') in the format string to ensure multi line output, the function now assumes a multi line output is wanted by default, but can be controlled. So the default value is True.\n
            multiple_items_per_line: Boolean to whether or not as to have multiple items from the list in one line chained together. Default False.\n
            num_items_per_line: The number of the items from the list that will be added to a single line. Default 5 items per line of text.\n
            format_between_items: If we format the list to have multiple items in one line, what should the formatting be when joining the items together. The default format is: ', '
    
    Returns:
        A single str of the items, either one item per line or multiple items per line.
    """

    final_str: str = ''

    if multiple_items_per_line:
        for nested_list in split_list(list, num_items_per_line):
            final_str += format_between_items.join(nested_list) + ('\n' if print_multiple_lines else '') + format_str
    else:
        format_str += '\n'
        final_str += format_str.join(list)

    return final_str

def main():
    parser = argparse.ArgumentParser(description='Scan a directory for ROMs to add to Lutris.', add_help=False)

    # Custom help - to prettify the platform list printing
    parser.add_argument('-h', "--help", action='store_true',
                        help="show this help message and exit")
    
    # Required arguments
    parser.add_argument('-d', '--directory', type=directory,
                        help='Directory to scan for games.')
    parser.add_argument('-r', '--runner', type=str,
                        help='Name of Lutris runner to use.')
    parser.add_argument('-p', '--platform', type=str, choices=PLATFORMS,
                        help='Platform name.')

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
        print("""usage: lutris_bulk_adder.py [-h] [-d DIRECTORY] [-r RUNNER]
                            [-p PLATFORM (see choices below)]
                            [-ld LUTRIS_DATABASE] [-ly LUTRIS_YML_DIR] [-lg LUTRIS_GAME_DIR] [-i PLATFORM_INFO] [-a] [-f [FILE_TYPES ...]] [-o GAME_OPTIONS] [-s [STRIP_FILENAME ...]]
                            [-n]

Scan a directory for ROMs to add to Lutris.

options:
  -h, --help            show this help message and exit
  -d, --directory DIRECTORY
                        Directory to scan for games.
  -r, --runner RUNNER   Name of Lutris runner to use.
  -p, --platform PLATFORM
                        Platform name.
                        The following platforms are available:
                        {}
  -ld, --lutris-database LUTRIS_DATABASE
                        Path to the Lutris SQLite database.
  -ly, --lutris-yml-dir LUTRIS_YML_DIR
                        Directory containing Lutris yml files.
  -lg, --lutris-game-dir LUTRIS_GAME_DIR
                        Lutris games install dir.
  -i, --platform-info PLATFORM_INFO
                        List information for a given platform (runners, cores if libretro is an option and defaults)
  -f, --file-types [FILE_TYPES ...]
                        Space-separated list of file types to scan for.
  -o, --game-options GAME_OPTIONS
                        Additional options to write to the YAML file under the "game" key (e.g. platform number as required for Dolphin)
  -s, --strip-filename [STRIP_FILENAME ...]
                        Space-separated list of strings to strip from filenames when generating game names.
  -n, --no-write        Do not write YML files or alter Lutris database, only print data to be written out to stdout. (i.e. dry run)"""
              .format(format_list(list(PLATFORMS.keys()), '\t\t\t', multiple_items_per_line=True)))
        sys.exit(0)

    platform_info = args.platform_info
    if platform_info:
        platform = PLATFORMS[platform_info]
        cores = platform["cores"]
        default_runner = platform["default_runner"]
        print("{}:".format(platform_info))
        print("\tRunners: {}".format(', '.join(platform["runners"])))
        print("\tDefault runner: {}".format(default_runner))
        if cores:
            print("\t    Libretro cores: {}".format(', '.join(cores)))
            if default_runner == "libretro": print("\t    Default libretro core: {}".format(platform["default_core"]))
        sys.exit(0);


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
    game_id = cur.fetchone()[0] + 1
    
    # Scan dir for ROMs
    files = scan_for_filetypes(args.directory, args.file_types)
    for file in files:
        ts = int(datetime.utcnow().timestamp())

        # Generate game name and slug from filename
        game = re.sub(r"\..*", "", os.path.basename(file))  # Strip extension
        for token in args.strip_filename:
            game = game.replace(token, "")                  # Strip tokens
        game = re.sub(r"\s+", " ", game).strip(" ")         # Remove excess whitespace

        slug = re.sub(r"[^0-9A-Za-z']", " ", game)          # Split on nonword characters
        slug = slug.replace("'", "")                        # Strip apostrophe
        slug = re.sub(r"\s+", "-", slug).strip("-").lower() # Replace whitespace with dashes

        # Data for YML file
        config_file = '{slug}-{ts}'.format(slug=slug, ts=ts)
        config_file_path = os.path.join(args.lutris_yml_dir, "{}.yml".format(config_file))
        config = {
            args.runner: {},
            "game": {
                "main_file": file
            },
            "system": {}
        }

        if args.game_options is not None:
            config['game'].update(args.game_options)

        # Data for Lutris DB
        values = {
            "id": game_id,
            "name": game,
            "slug": slug,
            "installer_slug": None,
            "parent_slug": None,
            "platform": args.platform,
            "runner": args.runner,
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
            "playtime": None,
            "hidden": 0,
            "service": None,
            "service_id": None
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


if __name__ == '__main__':
    main()
