from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

private_key = RSA.import_key(open("private_key.pem", "rb").read())
public_key = RSA.import_key(open("public_key.pem", "rb").read())

message = b"Top Secret Document"

aes_key = get_random_bytes(16)

cipher_aes = AES.new(aes_key, AES.MODE_CBC)
iv = cipher_aes.iv
encrypted_message = cipher_aes.encrypt(pad(message, AES.block_size))

cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

print("--- Sender ---")
print(f"Encrypted AES Key (Hex): {binascii.hexlify(encrypted_aes_key).decode()}")
print(f"Encrypted Data (Hex): {binascii.hexlify(encrypted_message).decode()}")

print("\n--- Receiver ---")
decrypt_rsa = PKCS1_OAEP.new(private_key)
decrypted_aes_key = decrypt_rsa.decrypt(encrypted_aes_key)

decrypt_aes = AES.new(decrypted_aes_key, AES.MODE_CBC, iv)
decrypted_message = unpad(decrypt_aes.decrypt(encrypted_message), AES.block_size)

print(f"Decrypted Message: {decrypted_message.decode()}")
