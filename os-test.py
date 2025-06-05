import os
import subprocess


print(os.environ.get("HOME"), end="\n\n")
os.environ.pop("USER")
print(os.environ.get('USER'))
print(os.environ.get('SHELL'))

print(os.environ.get('PWD'))
subprocess.run(["echo hello && echo World!"], shell=True)