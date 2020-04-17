import yaml
from typing import List, Type
from .command_factory import commander_of, command_map
from .command import Command
import os


def is_option(s: str):
    return s.count("-") > 0


class Poppo:
    CONFIG = yaml.load(open(f"{__file__}/../application.yaml"), Loader=yaml.BaseLoader)
    LIST_OPTION = {"-l", "--list"}
    def __init__(self, Commander: Type[Command], options: List[str], argv: List[str]):
        self.Commander = Commander
        self.options = options
        self.argv = argv

    def __call__(self):
        if self.Commander is not None:
            self.Commander(options=self.options, argv=self.argv).exec()
        elif len(self.options) > 0:
            self._exec()

    def _exec(self):
        if any(map(lambda o: o in Poppo.LIST_OPTION, self.options)):
            print(*[f"command: {k} => {v}" for k, v in command_map.items()], sep="\n")


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
        options = list(filter(is_option, args))
        return options


def main(args: List[str]):
    command: Type[Command] = None if is_option(args[0]) else Poppo.get_command(args)
    options = Poppo.get_options(args)
    argv = [arg for arg in args if arg not in options][1:]
    poppo = Poppo(command, options, argv)
    poppo()
