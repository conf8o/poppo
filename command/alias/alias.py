from .. import Command
import yaml
import os


def _alias(cmd, path):
    text = f"@echo off\ncd {__file__}\\..\\..\\..\\..\npython -m poppo {cmd} %*\ncd {__file__}\\..\\..\\..\\..\\.."
    open(f"{path}/{cmd}.bat", "w").write(text)


class Alias(Command):
    def __init__(self, options, argv):
        self.options = options
        self.argv = argv
        config = yaml.load(open(f"{__file__}/../alias.yaml"), Loader=yaml.BaseLoader)
        self.path = config["path"]
        self.default_path = self.path["default"]
        poppo_config = yaml.load(open(f"{__file__}/../../../application.yaml"), Loader=yaml.BaseLoader)
        self.poppo_commands = poppo_config["commands"]

    def exec(self):
        cmds = self._find_commands()
        if not cmds:
            print("Alias command needs commands.\nValid commands are below:")
            print(*self.poppo_commands, sep="\n")
            return

        paths = self._find_paths()
        if not paths:
            print("There is no valid paths to make aliases.")
            print(f"Would you like to make alias(es) in the default path?: {self.default_path}")
            ans = input("[y/n] >>")
            if ans in {"Y", "y"}:
                paths = [self.default_path]
            else:
                print("Making alias was canceled.")
                return
        
        for cmd in cmds:
            for path in paths:
                _alias(cmd, path)
                print(f"'{cmd}' alias has been made into {path}")

    def _find_commands(self):
        return [cmd for cmd in self.argv if cmd in self.poppo_commands]

    def _find_paths(self):
        shortcuts = set(self.path.keys())
        paths = [self.path[s] for s in self.argv if s in shortcuts]
        paths += [path for path in self.argv if os.path.isdir(path) and path not in self.poppo_commands]
        return paths
