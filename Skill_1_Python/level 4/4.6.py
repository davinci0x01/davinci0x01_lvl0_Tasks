import random

mac = []

for i in range(6):
    part = random.randint(0, 255)
    mac.append(f"{part:02x}")

mac_address = ":".join(mac)
print("Random MAC address:", mac_address)
