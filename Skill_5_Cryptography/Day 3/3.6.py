from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii

private_key = RSA.import_key(open('private_key.pem', 'rb').read())
public_key = RSA.import_key(open('public_key.pem', 'rb').read())

print("--- RSA OAEP Encryption Tool ---")
user_text = input("Enter text to encrypt: ").encode()

cipher_encrypt = PKCS1_OAEP.new(public_key)
encrypted_text = cipher_encrypt.encrypt(user_text)

print(f"\nEncrypted (Hex):\n{binascii.hexlify(encrypted_text).decode()}")

cipher_decrypt = PKCS1_OAEP.new(private_key)
decrypted_text = cipher_decrypt.decrypt(encrypted_text)

print(f"\nDecrypted:\n{decrypted_text.decode()}")
