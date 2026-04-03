from Crypto.PublicKey import RSA

key = RSA.generate(2048)

private_key = key.export_key()
print("Private Key:\n" + private_key.decode())

public_key = key.publickey().export_key()
print("Public Key:\n" + public_key.decode())
