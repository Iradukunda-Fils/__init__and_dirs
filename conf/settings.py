import sys
import subprocess

APPS = [
    'module1',
    'module2',
    'module3',
]


for mod in APPS:
    print("runned mod")
    sys.path.append(mod)

subprocess.run(["uv", "run", "./main.py"])