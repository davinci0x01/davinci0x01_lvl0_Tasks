import hashlib

password = input("Enter 4-digit PIN (1234): ")
target_hash = hashlib.md5(password.encode()).hexdigest()

for pin in range(10000):

    pin_str = f"{pin:04d}"

    hash_value = hashlib.md5(pin_str.encode()).hexdigest()

    if hash_value == target_hash:
        print("PIN Found:", pin_str)
        break
    else:
        print("PIN not found")
