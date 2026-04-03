import hashlib

password = input("Enter password: ")

data = password.encode()

hash_value = hashlib.sha256(data).hexdigest()

print("SHA256 Hash:", hash_value)
