import random

chars = "!@#$%&*"
letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
password = ""

while len(password) < 12:
    password += random.choice(chars + letters + digits)

print(password)