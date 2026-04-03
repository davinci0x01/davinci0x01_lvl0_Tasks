from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import time

def test_rsa_speed(key_size):
    print(f"\n--- Testing {key_size}-bit RSA ---")
    
    # Test Key Generation Speed
    start_time = time.time()
    key = RSA.generate(key_size)
    key_gen_time = time.time() - start_time
    print(f"Key Generation: {key_gen_time:.4f} seconds")
    
    public_key = key.publickey()
    private_key = key
    cipher_encrypt = PKCS1_OAEP.new(public_key)
    cipher_decrypt = PKCS1_OAEP.new(private_key)
    message = b"Performance test message"
    
    # Test Encryption Speed
    start_time = time.time()
    encrypted = cipher_encrypt.encrypt(message)
    enc_time = time.time() - start_time
    print(f"Encryption: {enc_time:.6f} seconds")
    
    # Test Decryption Speed
    start_time = time.time()
    decrypted = cipher_decrypt.decrypt(encrypted)
    dec_time = time.time() - start_time
    print(f"Decryption: {dec_time:.6f} seconds")

test_rsa_speed(1024)
test_rsa_speed(2048)
test_rsa_speed(3072)