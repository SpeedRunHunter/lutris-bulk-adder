import re
import os
import argparse

from constants import PLATFORMS

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
    
    cores = platform["cores"]
    default_runner = platform["default_runner"]
    print("{}:".format(platform_info))
    print("\tRunners: {}".format(', '.join(platform["runners"])))
    print("\tDefault runner: {}".format(default_runner))
    if cores:
        print("\t\tLibretro cores: {}".format(', '.join(cores)))
        if default_runner == "libretro": print("\t\tDefault libretro core: {}".format(platform["default_core"]))

class MissingRequiredDataError(ValueError):
    pass

class DefaultValueNotInListOfValuesError(ValueError):
    pass

class ExpectedValueMissingInListOfValuesError(ValueError):
    pass

class MisconfiguredDefaultsError(ValueError):
    pass

class InvalidDataError(ValueError):
    pass

class PlatformData():
    """A simple wrapper class in place of the nested dictionaries stored in the PLATFORMS dictionary\n
    
    Note:
        All attributes store string(s) and all strings fed to the constructor must be in a case that perfectly matches for file names and internal identifiers for things like runners and cores.
        For example, Lutris stores the specified runner for a game in its SQLite database file in lowercase. Likewise every and all Python script file for the runner, or the json file for json-based runners are also in lowercase. And in my interpretation, the case of letters in the name of the runner stored in the database for a game is maintained to match with the python/json file.
        In that same vain, for a game that's ran by retroarch, the game's YAML file will contain the name of the retroarch core for the game to be loaded with. This is treated as an option in the game yml object. And this core association string is written to file by taking the filename of the libretro core, stripping the `_libretro.so` part at the end, and only keeping the main core identifier. Thus, for example PS2 games loaded with retroarch will have a core identifier in the yml of `pcsx2`, because the libretro core filename is `pcsx2_libretro.so`, instead of say `lrps2`.
        Almost all libretro cores follow this convention for filenaming, except for DoubleCherryGB... for some reason. Thus, that's the only exception in the almost overall rule, where all runners and cores are store in lowercase.

    Attributes:
        runners (required): A list of names for Lutris runners.
        default_runner (required): The default lutris runner assigned for this platform. This runner must be included in the runners list.
        cores (required by default_core attribute, requires libretro to be in runners list): A list of libretro cores available for the platform.
        default_core (optional, requires libretro to be the default_runner attribute's value): The default libretro core assigned for this platform.
    """
    runners: list[str]
    default_runner: str
    cores: list[str] | None = None
    default_core: str | None = None

    def __init__(
            self,
            runners: list[str], default_runner: str,
            cores: list[str] | None = None, default_core: str | None = None
    ):
        """Initialize the class and before that ensure no foul play with the input data.

        Args:
            self: The current class instance. Used to reference the attributes of the class.
            runners (required): A list of names for Lutris runners.
            default_runner (required): The default lutris runner assigned for this platform. This runner must be included in the runners list.
            cores (required by default_core attribute, requires libretro to be in runners list): A list of libretro cores available for the platform.
            default_core (optional, requires libretro to be the default_runner attribute's value): The default libretro core assigned for this platform.

        Raises:
            MissingRequiredDataError: If the required arguments - runners and default_runner - aren't specified, or if a dependency argument - cores for default_core - isn't specified.
            DefaultValueNotInListOfValuesError: If a supplied default value - default_runner or default_core - cannot find its entry in its respective list of values - runners or cores respectively.
            ExpectedValueMissingInListOfValuesError: If a certain argument - cores - is supplied to the init function, but a specific value - "libretro" - in a list of values - runners - is missing.
            MisconfiguredDefaultsError: If default values are supplied - default_core and default_runner - but one of the arguments for the default value is incorrect for the other default value - a default_core is specified, but the default_runner is not libretro.
        """

        # missing runners or default_runner
        if runners == None or default_runner == None: 
            raise MissingRequiredDataError('{} cannot be a None value and are required'.format(
        "'Runners' and 'default_runner'" if not runners and not default_runner 
        else ("'Runners'" if not runners else "'Default_runner'")
            ))
        
        # default_runner not a value in runners
        if default_runner not in runners:
            raise DefaultValueNotInListOfValuesError('The default_runner must be a value that can be found in runners')
        
        # default_core is specified but not cores
        if default_core and cores == None:
            raise MissingRequiredDataError('There cannot be a default_core specified if there are no cores specified')
        
        # cores is specified but libretro is not in runners
        if cores and ("libretro" not in runners):
            raise ExpectedValueMissingInListOfValuesError('There cannot be a cores list if libretro is not specified in the runners list')
        
        # default_core not a value in cores
        if cores != None and default_core != None: 
            if default_core not in cores:
                raise DefaultValueNotInListOfValuesError('The default_core must be a value that can be found in cores')
        
        # default_core specified but libretro is not the default_runner
        if default_core and "libretro" != default_runner:
            raise MisconfiguredDefaultsError('There cannot be a default_core association if the default_runner is not libretro')

        # basic validation
        invalidations: list[str] = []

        # runner invalidations:
        # 1. isn't a list
        # 2. is an empty list
        # 3. contains a list of empty strings that may or may not contain whitespaces only
        if type(runners) != list: invalidations.append("The runners input must be a list")
        else:
            if len(runners) == 0: invalidations.append("The runners list mustn't be empty")
            else: 
                if len(''.join(runners).replace(" ", "")) == 0: invalidations.append("The items in the runners list mustn't be empty")

        # cores invalidations:
        # 1. isn't a list
        # 2. is an empty list
        # 3. contains a list of empty strings that may or may not contain whitespaces only
        if cores != None:
            if type(cores) != list: invalidations.append("The cores input must be a list")
            else:
                if len(cores) == 0: invalidations.append("The cores list mustn't be empty")
                else: 
                    if len(''.join(cores).replace(" ", "")) == 0: invalidations.append("The items in the cores list mustn't be empty")

        # default_runner invalidations:
        # 1. isn't a str
        # 2. is an empty str that may or may not contain whitespaces only
        if type(default_runner) != str: invalidations.append("The default_runner input must be a string")
        else:
            if len(default_runner.replace(" ", "")) == 0: invalidations.append("The default_runner string mustn't be empty")

        # default_core invalidations:
        # 1. isn't a str
        # 2. is an empty str that may or may not contain whitespaces only
        if default_core != None:
            if type(default_core) != str: invalidations.append("The default_core input must be a string")
            else:
                if len(default_core.replace(" ", "")) == 0: invalidations.append("The default_core string mustn't be empty")

        # print all invalidations if any
        if len(invalidations) > 0:
            raise InvalidDataError("""One or multiple basic validation failures have occoured with the constructor inputs:
                {}
            """.format(
                '\n\t\t'.join(invalidations)
            ))

        self.cores = cores
        self.default_core = default_core
        self.default_runner = default_runner
        self.runners = runners