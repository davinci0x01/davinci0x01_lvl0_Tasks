from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

key = b'8bytekey'

text = input("Enter text: ").encode()

cipher = DES.new(key, DES.MODE_ECB)

encrypted = cipher.encrypt(pad(text, 8))

print("Encrypted:", encrypted)

decrypted = unpad(cipher.decrypt(encrypted), 8)

print("Decrypted:", decrypted.decode())
