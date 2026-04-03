import hashlib

text = input("Enter text: ")

data = text.encode()

sha1_hash = hashlib.sha1(data).hexdigest()

print("SHA1 Hash:", sha1_hash)
