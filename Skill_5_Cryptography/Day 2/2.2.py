from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

key = b'1234567890abcdef'

message = input("Enter message: ").encode()

iv = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

encrypted = cipher.encrypt(pad(message, AES.block_size))

print("Encrypted:", encrypted)
print("IV:", iv)

cipher2 = AES.new(key, AES.MODE_CBC, iv)

decrypted = unpad(cipher2.decrypt(encrypted), AES.block_size)

print("Decrypted:", decrypted.decode())
