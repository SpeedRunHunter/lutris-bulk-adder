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