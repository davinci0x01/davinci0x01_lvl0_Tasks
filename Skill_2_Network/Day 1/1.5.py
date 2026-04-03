ip = input("Enter IP address: ").split(".")
mask = input("Enter Subnet Mask: ").split(".")


network = []
for i in range(4):
    network.append(str(int(ip[i]) & int(mask[i])))


broadcast = []
for i in range(4):
    broadcast.append(str(int(network[i]) | (255 - int(mask[i]))))

print("Network Address   :", ".".join(network))
print("Broadcast Address :", ".".join(broadcast))
