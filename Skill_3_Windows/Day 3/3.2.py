import shutil

src = input("Source file path: ")
dst = input("Destination path: ")

shutil.copy(src, dst)
print("File copied successfully")