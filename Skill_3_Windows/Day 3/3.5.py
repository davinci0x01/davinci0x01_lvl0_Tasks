import shutil
from datetime import date

src = input("Source folder: ")
dst = input("Backup base folder: ")

shutil.copytree(src, f"{dst}\\backup_{date.today()}")
print("Backup created")