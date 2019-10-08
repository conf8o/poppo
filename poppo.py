import yaml
from typing import List, Type
from command_factory import commander_of
from command import Command


class Poppo:
    CONFIG = yaml.load(open(f"{__file__}/../application.yaml"), Loader=yaml.BaseLoader)

    def __init__(self, Commander: Type[Command], options: List[str], argv: List[str]):
        self.Commander = Commander
        self.options = options
        self.argv = argv

    def __call__(self):
        self.Commander(options=self.options, argv=self.argv).exec()

    @staticmethod
    def get_command(args: List[str]) -> Type[Command]:
        config_commands: List[str] = Poppo.CONFIG["commands"]
        commands = list(filter(lambda c: c in config_commands, args))
        if not commands:
            print(f"Invalid command.")
            print(f"Valid commands below:")
            print(*config_commands, sep="\n")
            exit()

        return commander_of(commands[0])

    @staticmethod
    def get_options(args: List[str]) -> List[str]:
        options = list(filter(lambda c: c.count("-") > 0, args))
        return options


def main(args: List[str]):
    command: Type[Command] = Poppo.get_command(args)
    options = Poppo.get_options(args)
    argv = [arg for arg in args if arg not in options][1:]
    poppo = Poppo(command, options, argv)
    poppo()
