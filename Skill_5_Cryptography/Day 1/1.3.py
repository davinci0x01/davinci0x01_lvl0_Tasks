import hashlib

file_path = "1.1.py"

with open(file_path, "rb") as file:
    data = file.read()

md5_hash = hashlib.md5(data).hexdigest()

print("MD5 Hash:", md5_hash)
