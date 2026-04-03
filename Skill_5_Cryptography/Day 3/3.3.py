from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
private_key = key

message = b"Important system update file"

hashed_message = SHA256.new(message)

signer = pkcs1_15.new(private_key)
signature = signer.sign(hashed_message)

print(f"Message: {message.decode()}")
print(f"Signature (Hex): {signature.hex()}")
