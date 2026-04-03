def is_private_ip(ip):
    parts = ip.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            return False
    
    first = int(parts[0])
    second = int(parts[1])

    if first == 10:
        return True
    elif first == 172 and 16 <= second <= 31:
        return True
    elif first == 192 and second == 168:
        return True
    else:
        return False


ip = input("Enter IP address: ")

if is_private_ip(ip):
    print("Private IP address")
else:
    print("Public IP address")
