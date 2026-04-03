from Crypto.Util.number import inverse

n = 3233
e = 17

ciphertext = 855

print(f"Target Public Key -> n: {n}, e: {e}")

p = 0
q = 0
for i in range(2, n):
    if n % i == 0:
        p = i
        q = n // i
        break

print(f"Found factors -> p: {p}, q: {q}")

phi = (p - 1) * (q - 1)

d = inverse(e, phi)
print(f"Cracked Private Key (d): {d}")

decrypted_message = pow(ciphertext, d, n)
print(f"Decrypted Message (Integer): {decrypted_message}")
