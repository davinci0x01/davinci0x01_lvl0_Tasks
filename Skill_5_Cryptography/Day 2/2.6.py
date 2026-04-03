from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

key = b'1234567890abcdef'
iv = b'abcdef1234567890'

with open("encrypted.bin", "rb") as f:
    encrypted_data = f.read()

cipher = AES.new(key, AES.MODE_CBC, iv)

decrypted = unpad(cipher.decrypt(encrypted_data), AES.block_size)

with open("decrypted.txt", "wb") as f:
    f.write(decrypted)

print("File decrypted successfully")
print("Decrypted content:", decrypted.decode())
