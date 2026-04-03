from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP, AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

public_key = RSA.import_key(open("public_key.pem", "rb").read())
private_key = RSA.import_key(open("private_key.pem", "rb").read())

file_data = open("secret_document.txt", "rb").read()

aes_key = get_random_bytes(16)
cipher_aes = AES.new(aes_key, AES.MODE_CBC)
encrypted_data = cipher_aes.encrypt(pad(file_data, AES.block_size))

cipher_rsa = PKCS1_OAEP.new(public_key)
encrypted_aes_key = cipher_rsa.encrypt(aes_key)

with open("encrypted_file.bin", "wb") as f:
    f.write(encrypted_aes_key)
    f.write(cipher_aes.iv)
    f.write(encrypted_data)

print("File encrypted and saved to 'encrypted_file.bin'")
with open("encrypted_file.bin", "rb") as f:
    print("Encrypted file content (hex):", f.read())



with open("encrypted_file.bin", "rb") as f:
    enc_aes_key = f.read(256) 
    iv = f.read(16)           
    enc_data = f.read()       

decrypt_rsa = PKCS1_OAEP.new(private_key)
dec_aes_key = decrypt_rsa.decrypt(enc_aes_key)

decrypt_aes = AES.new(dec_aes_key, AES.MODE_CBC, iv)
decrypted_data = unpad(decrypt_aes.decrypt(enc_data), AES.block_size)

with open("decrypted_document.txt", "wb") as f:
    f.write(decrypted_data)

print("\nFile decrypted and saved to 'decrypted_document.txt'")
with open("decrypted_document.txt", "rb") as f:
    print("Decrypted file content (hex):", f.read().decode())
