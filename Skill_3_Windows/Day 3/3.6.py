import os

path = input("Enter folder path: ")
target = input("Enter file name: ")

for root, dirs, files in os.walk(path):
    if target in files:
        print("Found:", os.path.join(root, target))