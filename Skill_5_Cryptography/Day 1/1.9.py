import base64

text = input("Enter encoded string: ")

try:
    bytes.fromhex(text)
    print("This looks like HEX encoding")
except ValueError:
    pass

try:
    base64.b64decode(text)
    print("This looks like Base64 encoding")
except Exception:
    pass
