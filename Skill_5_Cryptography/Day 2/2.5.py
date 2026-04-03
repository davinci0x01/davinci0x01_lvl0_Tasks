from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = b'1234567890abcdef'
iv = b'abcdef1234567890'

with open("file.txt", "rb") as f:
    data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)
encrypted = cipher.encrypt(pad(data, AES.block_size))

with open("encrypted.bin", "wb") as f:
    f.write(encrypted)

print("File encrypted successfully")
print(encrypted)

cipher2 = AES.new(key, AES.MODE_CBC, iv)
decrypted = unpad(cipher2.decrypt(encrypted), AES.block_size)

with open("decrypted.txt", "wb") as f:
    f.write(decrypted)

print("File decrypted successfully")
print(decrypted)
