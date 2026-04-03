import os

path = input("Enter folder path: ")

for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        size = os.path.getsize(full_path)
        print(file, "-", size, "bytes")