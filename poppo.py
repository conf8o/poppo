import yaml
from typing import List, Callable
from command_factory import commander_of
from command import Command

CommandClass = Callable[[List[str]], Command]

class Poppo:
    CONFIG = yaml.load(open(f"{__file__}/../application.yaml"), Loader=yaml.BaseLoader)
    def __init__(self, Command: CommandClass, options: List[str], argv: List[str]):
        self.Command = Command
        self.options = options
        self.argv = argv

    def __call__(self):
        self.Command(options=self.options, argv=self.argv).exec()

    @staticmethod
    def get_command(args: List[str]) -> Command:
        config_commands = set(Poppo.CONFIG["commands"])
        commands = list(filter(lambda c: c in config_commands, args))
        if len(commands) == 0:
            print(f"Invalid command.")
            print(f"Valid commands below:")
            print(*list(config_commands), sep="\n")
            exit()

        return commander_of(commands[0])

    @staticmethod
    def get_options(args: List[str]) -> List[str]:
        options = list(filter(lambda c: c.count("-") > 0, args))
        return options

def main(args: List[str]):
    command = Poppo.get_command(args)
    options = Poppo.get_options(args)
    argv = [arg for arg in args if arg not in options][1:]
    poppo = Poppo(command, options, argv)
    poppo()