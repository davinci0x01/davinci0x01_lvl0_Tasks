ips = []

for i in range(256):
    ips.append(f"192.168.1.{i}")

print(f"First 5 IPs: {ips[:5]} \nLast 5 IPs: {ips[-5:]}")
