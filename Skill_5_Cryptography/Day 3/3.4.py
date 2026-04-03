from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

key = RSA.generate(2048)
private_key = key
public_key = key.publickey()
#Fake_key = RSA.generate(2048)

original_message = b"Important system update file"
hashed_msg = SHA256.new(original_message)
signature = pkcs1_15.new(private_key).sign(hashed_msg) # change to fake_key to see the invalid signature case

received_message = b"Important system update file"
received_hash = SHA256.new(received_message)

try:
    pkcs1_15.new(public_key).verify(received_hash, signature)
    print("Signature is valid.")
except ValueError:
    print("Invalid signature! The message was tampered with or fake.")
