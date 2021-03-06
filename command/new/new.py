from .. import Command
import os


def _make_template(cmd, d):
    temp = open(f"{__file__}/../template", "r").read()
    open(f"{d}/{cmd}.py", "w").write(temp.format(cmd.capitalize()))


class New(Command):
    def __init__(self, options, argv):
        self.options = options
        self.argv = argv
        self.dirs = [f"{__file__}/../../{arg}" for arg in argv]

    def exec(self):
        if not self.argv:
            print("'new' command needs 1 or more arguments, given 0") 
            return
        self._make_files()
        # TODO エラー発生時の削除処理

    def _make_files(self):
        for cmd in self.argv:
            # コマンドのディレクトリ作成
            d = f"{__file__}/../../{cmd}"
            os.mkdir(d)
            open(f"{d}/__init__.py", "w").write(f"from .{cmd} import {cmd.capitalize()}\n")
            _make_template(cmd, d)

            # コマンドの紐づけ
            # commandフォルダ直下の__init__.pyにコマンドを追加
            d = f"{__file__}/../../__init__.py"
            open(d, "a").write(f"from .{cmd} import {cmd.capitalize()}\n")
            # yamlにコマンドを追加
            d = f"{__file__}/../../../application.yaml"
            open(d, "a").write(f"    - {cmd}\n")
            # factoryにコマンドを追加
            d = f"{__file__}/../../../command_factory.py"
            open(d, "a").write(f'command_map["{cmd}"] = {cmd.capitalize()}\n')
            print(f"'{cmd}' command has been created.")
            print(f"Please command 'python -m poppo {cmd}' to check the command which you have just created.")
