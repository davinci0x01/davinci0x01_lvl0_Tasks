from Crypto.PublicKey import RSA

key = RSA.generate(2048)

with open("private_key.pem", "wb") as priv_file:
    priv_file.write(key.export_key("PEM"))

with open("public_key.pem", "wb") as pub_file:
    pub_file.write(key.publickey().export_key("PEM"))

print("Keys saved successfully to files")

loaded_private_key = RSA.import_key(open("private_key.pem", "rb").read())
loaded_public_key = RSA.import_key(open("public_key.pem", "rb").read())

print("Keys loaded successfully from files")
print(f"Loaded Private Key length: {loaded_private_key.size_in_bits()} bits")
