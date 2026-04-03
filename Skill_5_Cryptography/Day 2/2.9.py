from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

text = input("Enter text: ").encode()
key = input("Enter key (16 chars): ").encode()

iv = get_random_bytes(16)

cipher = AES.new(key, AES.MODE_CBC, iv)

encrypted = cipher.encrypt(pad(text, AES.block_size))

with open("output.bin", "wb") as f:
    f.write(iv + encrypted)

print("Encrypted saved to output.bin")
print("IV:", iv)