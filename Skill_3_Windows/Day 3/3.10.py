import os

path = input("Enter folder path: ")
limit = 100 * 1024 * 1024  # 100MB in bytes

for root, dirs, files in os.walk(path):
    for file in files:
        full_path = os.path.join(root, file)
        if os.path.getsize(full_path) > limit:
            print("Large file:", full_path)