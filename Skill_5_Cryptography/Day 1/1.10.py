import hashlib

text = input("Enter text: ")
data = text.encode()

md5_hash = hashlib.md5(data).hexdigest()
sha1_hash = hashlib.sha1(data).hexdigest()
sha256_hash = hashlib.sha256(data).hexdigest()

print("MD5   :", md5_hash)
print("SHA1  :", sha1_hash)
print("SHA256:", sha256_hash)
