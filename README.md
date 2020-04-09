# Poppo

簡易コマンドラインアプリ開発フレームワーク

## 使い方

newコマンドにより、コマンドクラスが作成される。

```shell

$ python main.py new mycommand

```

commandフォルダにコマンドクラスのファイルが作成される。

```python
from .. import Command


class MyCommand(Command):
    def __init__(self, options, argv):
        # initializer
    
    def exec(self):
        # execute

```

## コマンドクラスの実装

execに処理を定義する。
コマンドライン引数とオプション("-"で始まる引数)はそれぞれargvとoptionsにリストで格納される。

```python
class MyCommand(Command):
    def __init__(self, options, argv):
        # "-"ハイフンの引数はoptionsに格納される
        self.options = options

        # 引数の最初とハイフン以外はコマンドの引数として格納される
        self.argv = argv
    
        # TODO オプションに対する引数の対応。

    def exec(self):
        # 実装。
```

## コマンドの実行

```shell
$ python main.py mycommand arg -o
```

## その他の機能

### コマンドのエイリアス作成

#### ailiasフォルダのalias.yamlにリリース先のパスを設定

```yaml
path:
  user: "C:Users..."
  desktop: "C:Users..."
  mypath: "C:Users..."
```

#### リリースコマンドを実行

```shell
$ python main.py alias mycommand user
```

バッチファイルが指定のパスに作成されるため、

リリース先で実行可能

```shell
$ ./mycommand arg -o
```

### コマンドの削除

```shell
$ python main.py delete mycommand
```

---

## newコマンドで作成されるものたち

### 作成したコマンドのフォルダの__init__.pyを作成

```python
from command.mycommand.mycommand import *
```

### commandフォルダの__init__.pyにコマンドクラスのインポートを追加

```python
from .mycommand import *
```

### application.yamlにコマンドを設定

```yaml
commands:
  - mycommand

```

### command_factory.pyでコマンドとコマンドクラスを対応させる

```python
commands_dict["mycommand"] = cmd.MyCommand

```
