import secrets

key_128 = secrets.token_bytes(16)
key_256 = secrets.token_bytes(32)

print("AES 128-bit key:", key_128)
print("AES 256-bit key:", key_256)
