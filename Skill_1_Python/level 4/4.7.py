def xor_encrypt(text, key):
    result = ""

    for i in range(len(text)):
        result += chr(ord(text[i]) ^ ord(key[i % len(key)]))

    return result


message = input("Enter text: ")
key = input("Enter key: ")

encrypted = xor_encrypt(message, key)
print("Encrypted:", encrypted)

decrypted = xor_encrypt(encrypted, key)
print("Decrypted:", decrypted)
