from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes

key = b'1234567890abcdef'

text = b'Hello World!'

# ECB
cipher_ecb = AES.new(key, AES.MODE_ECB)
ecb_encrypted = cipher_ecb.encrypt(pad(text, AES.block_size))

# CBC
iv = get_random_bytes(16)
cipher_cbc = AES.new(key, AES.MODE_CBC, iv)
cbc_encrypted = cipher_cbc.encrypt(pad(text, AES.block_size))

print("ECB:", ecb_encrypted)
print("CBC:", cbc_encrypted)
