import hashlib

user_input = input("Enter a string to hash: ")

print("MD5:", hashlib.md5(user_input.encode()).hexdigest())
