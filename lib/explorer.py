import subprocess

def open(path):
    subprocess.run(f"explorer {path}", shell=True)