import command as cmd
import yaml
from typing import Type, Dict


command_map: Dict[str, Type[cmd.Command]] = {c: None for c in
                                             yaml.load(open(f"{__file__}/../application.yaml"),
                                                       Loader=yaml.BaseLoader)["commands"]}


def commander_of(command: str) -> Type[cmd.Command]:
    return command_map[command]


command_map["alias"] = cmd.Alias
command_map["new"] = cmd.New
command_map["delete"] = cmd.Delete
