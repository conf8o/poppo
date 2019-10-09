from .. import Command
import os
import shutil


def _delete(cmd, path):
    lines = open(path, "r").readlines()
    i, _ = next(filter(lambda x: cmd in x[1], enumerate(lines)))
    del lines[i]
    open(path, "w").writelines(lines)


class Delete(Command):
    def __init__(self, options, argv):
        self.options = options
        self.argv = argv
    
    def exec(self):
        if not self.argv:
            print("'delete' command needs 1 or more arguments, given 0")
            return
        self._rm()

    def _rm(self):
        for cmd in self.argv:
            d = f"{__file__}\\..\\..\\{cmd}"
            if os.path.exists(d):
                print(f"Deletes {cmd}'s:")
                shutil.rmtree(d)
                print("    command folder")
            else:
                print(f"No such command: {cmd}")
                return

            _delete(cmd, f"{__file__}/../../__init__.py")
            print("    __init__.py in command folder")

            _delete(cmd, f"{__file__}/../../../application.yaml")
            print("   application.yaml")

            _delete(cmd, f"{__file__}/../../../command_factory.py")
            print("   command_factory.py")
