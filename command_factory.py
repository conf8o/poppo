import yaml
from typing import Type, Dict
from .command import *

command_map: Dict[str, Type[Command]] = {c: None
                                         for c
                                         in yaml.load(open(f"{__file__}/../application.yaml"),
                                                      Loader=yaml.BaseLoader)["commands"]}


def commander_of(command: str) -> Type[Command]:
    return command_map[command]


command_map["alias"] = Alias
command_map["new"] = New
command_map["delete"] = Delete
command_map["memo"] = Memo
command_map["timecalc"] = Timecalc
command_map["routine"] = Routine
command_map["diff"] = Diff
command_map["calendar"] = Calendar
command_map["translate"] = Translate
command_map["dev"] = Dev
