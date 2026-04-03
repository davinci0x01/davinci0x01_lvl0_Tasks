from Crypto.Util.Padding import pad, unpad

text = input("Enter text: ").encode()

padded = pad(text, 16)

print("Padded:", padded)

unpadded = unpad(padded, 16)

print("Unpadded:", unpadded.decode())
