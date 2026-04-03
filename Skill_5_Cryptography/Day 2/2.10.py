from Crypto.Cipher import AES
from Crypto.Util import Counter

key = b'1234567890abcdef'

text = input("Enter text: ").encode()

ctr = Counter.new(128)

cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

encrypted = cipher.encrypt(text)

print("Encrypted:", encrypted)

# فك التشفير
ctr2 = Counter.new(128)

cipher2 = AES.new(key, AES.MODE_CTR, counter=ctr2)

decrypted = cipher2.decrypt(encrypted)

print("Decrypted:", decrypted.decode())