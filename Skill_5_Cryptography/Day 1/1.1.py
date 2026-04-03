import base64

text = input("Enter text to encode: ")

encoded = base64.b64encode(text.encode())
print("Encoded (Base64):", encoded.decode())

decoded = base64.b64decode(encoded)
print("Decoded:", decoded.decode())
