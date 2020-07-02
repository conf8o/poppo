from .. import Command
import subprocess

class Routine(Command):
    def __init__(self, options, argv):
        # initialize
        return
    
    def exec(self):
        morning()
        return

def morning():
    f = f"{__file__}/../morning.txt"
    subprocess.Popen(["notepad", f], shell=False)