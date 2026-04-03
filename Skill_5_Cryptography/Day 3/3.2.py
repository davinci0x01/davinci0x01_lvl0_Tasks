from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

key = RSA.generate(2048)
public_key = key.publickey()
private_key = key

message = b"Hello World!"

encryptor = PKCS1_OAEP.new(public_key)
encrypted_message = encryptor.encrypt(message)
print(f"Encrypted: {encrypted_message}")

decryptor = PKCS1_OAEP.new(private_key)
decrypted_message = decryptor.decrypt(encrypted_message)
print(f"Decrypted: {decrypted_message.decode()}")
