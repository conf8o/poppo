from .. import Command
import yaml
import os
import subprocess
from poppo.lib import explorer

class Memo(Command):
    LIST_OPTIONS = {"-l", "--list"}
    HELP_OPTIONS = {"-h", "--help"}
    EXPLORER_OPTIONS = {"-x", "--explorer"}
    NEWFILE_OPTIONS = {"-n", "--newfile"}
    CONFIG = yaml.load(open(f"{__file__}/../memo.yaml", "r"), Loader=yaml.BaseLoader)

    def __init__(self, options, argv):
        self.options = options
        self.argv = argv
        self.root = Memo.CONFIG["root"]
        self.extensions = Memo.CONFIG["extensions"]

    def exec(self):
        if len(self.options) > 1:
            print(f"options expected 1 when needed. given {len(self.options)}.")
            return

        option = None if not self.options else self.options[0]
        if option in Memo.LIST_OPTIONS:
            self._print_memos()
            return
        elif option in Memo.HELP_OPTIONS:
            self._print_helps()
            return
        elif option in Memo.EXPLORER_OPTIONS:
            explorer.open(self.root)
        elif option in Memo.NEWFILE_OPTIONS:
            explorer.open(self.root)
            self._newfile()
        else:
            self._open(self.argv)

    def _print_helps(self):
        return

    def _open(self, argv):
        for arg in argv:
            for e in self.extensions:
                file_name = f"{self.root}\\{arg}{e}"
                if os.path.exists(file_name):
                    print(file_name)
                    if e in {".html", ".url"}:
                        subprocess.Popen(["explorer", file_name], shell=True)
                    elif e == ".txt":
                        subprocess.Popen(["notepad", file_name], shell=True)
                    else:
                        print(f"unsuppoerted extension. check config of memo command. ({e})")
                else:
                    print(f"{file_name}: not found")

    def _newfile(self):
        newfile = f"{self.root}\\newfile.txt"
        open(newfile, "w").write("")
        subprocess.Popen(["start", "notepad", newfile], shell=True)

    def _print_memos(self):
        filenames = os.listdir(self.root)
        longestname_count = len(max(filenames, key=lambda s: len(s)))
        for filename in filenames:
            path = f"{self.root}\\{filename}"
            print(f"{filename.rjust(longestname_count)} -> {open(path).readline().strip()}")
                
