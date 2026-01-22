import re
import os
import argparse

from lutris_bulk_adder.constants import PLATFORMS

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
    """Takes a list and converts it into a list of nested lists with n number of items in said nested lists. This function will take n number of items from the original list, put them into a new list of n items, and nest that into a new list that will be returned. Should the original list run out of items before the n amount of items is achieved, the nested list will be n-k items smaller than required, where k is the amount of items missing.

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
        list (Required): List of items to convert and format.

        format_str (Required): The format based on which the items in the list will be joined together.

        print_multiple_lines (Optional): Whether or not the function should print everything into individual lines. My original use case dictated to have the result be in multiple lines. But realizing that it may not be desirable to do that, and also relying on the other coder to supply a line feed ('\\n') in the format string to ensure multi line output, the function now assumes a multi line output is wanted by default, but can be controlled. So the default value is True.

        multiple_items_per_line (Optional): Boolean to whether or not as to have multiple items from the list in one line chained together. Default False.

        num_items_per_line (Optional): The number of the items from the list that will be added to a single line. Default 5 items per line of text.

        format_between_items (Optional): If we format the list to have multiple items in one line, what should the formatting be when joining the items together. The default format is: ', '
    
    Returns:
        final_str: A single str of the items, either one item per line or multiple items per line.
    
    Raises:
        ValueError: If `print_multiple_lines` is false but `multiple_items_per_line` is true, that is an irrational expectation, as the function would already be joining everything together into one line.
    """

    if not print_multiple_lines and multiple_items_per_line:
        raise ValueError("There's a bad expectation to not print multiple lines yet print multiple items per line")

    final_str: str = ''

    if multiple_items_per_line:
        for nested_list in split_list(list, num_items_per_line):
            final_str += format_between_items.join(nested_list) + '\n' + format_str
    else:
        if print_multiple_lines: format_str += '\n'
        final_str += format_str.join(list)

    return final_str

def print_info_for_platform(platform_info: str):
    """Given a name for a platform, print all the available information about it - runners, libretro cores, if libretro is available as a runner, and default runner and core, if the default runner is libretro
    
    Args:
        platform_info: A string literal of the platform in question. This is treated as a key into the `PLATFORMS` dictionary.

    Raises:
        KeyError: the input platform string could not be found in the PLATFORMS dictionary.
    """

    platform = PLATFORMS[platform_info]
    
    cores = platform.cores
    default_runner = platform.default_runner
    print("{}:".format(platform_info))
    print("\tRunners: {}".format(', '.join(platform.runners)))
    print("\tDefault runner: {}".format(default_runner))
    if cores:
        print("\t\tLibretro cores: {}".format(', '.join(cores)))
        if default_runner == "libretro": print("\t\tDefault libretro core: {}".format(platform.default_core))