import os
import time

path = input("Enter folder path: ")
now = time.time()

for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        if now - os.path.getmtime(full_path) <= 86400:
            print("Modified:", full_path)