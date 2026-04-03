def ipv4_to_binary(ip):
    parts = ip.split(".")
    binary_ip = []

    for part in parts:
        binary = bin(int(part))[2:]   # تحويل إلى binary وإزالة 0b
        binary = binary.zfill(8)       # ضمان 8 bits
        binary_ip.append(binary)

    return ".".join(binary_ip)


ip = input("Enter IPv4 address: ")
print("Binary format:", ipv4_to_binary(ip))
