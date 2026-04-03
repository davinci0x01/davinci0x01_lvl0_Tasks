import subprocess

subprocess.run("net stop spooler", shell=True)
subprocess.run("net start spooler", shell=True)