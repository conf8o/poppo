import command as cmd
import yaml

command_map = {c: None for c in yaml.load(open(f"{__file__}/../application.yaml"), Loader=yaml.BaseLoader)["commands"]}

def commander_of(command: str) -> cmd.Command:
    return command_map[command]

command_map["alias"] = cmd.Alias
command_map["new"] = cmd.New
command_map["delete"] = cmd.Delete
