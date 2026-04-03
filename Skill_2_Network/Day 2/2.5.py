import random

open_ports = random.sample(range(1024, 65536), 5)

print("Random open ports:")
for port in open_ports:
    print(port)
