def is_ipv4(ip):
    parts = ip.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    
    return True


def is_ipv6(ip):
    parts = ip.split(":")
    
    if len(parts) < 3 or len(parts) > 8:
        return False
    
    hex_digits = "0123456789abcdefABCDEF"
    
    for part in parts:
        if part == "":
            continue  # for ::
        if len(part) > 4:
            return False
        for char in part:
            if char not in hex_digits:
                return False
    
    return True


ip = input("Enter IP address: ")

if "." in ip and is_ipv4(ip):
    print("Valid IPv4 address")
elif ":" in ip and is_ipv6(ip):
    print("Valid IPv6 address")
else:
    print("Invalid IP address")
