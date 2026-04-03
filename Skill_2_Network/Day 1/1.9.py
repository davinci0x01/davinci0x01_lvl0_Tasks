def get_ip_class(ip):
    first_octet = int(ip.split(".")[0])

    if 1 <= first_octet <= 126:
        return "Class A"
    elif 128 <= first_octet <= 191:
        return "Class B"
    elif 192 <= first_octet <= 223:
        return "Class C"
    elif 224 <= first_octet <= 239:
        return "Class D"
    elif 240 <= first_octet <= 255:
        return "Class E"
    else:
        return "Invalid or Reserved"


ip = input("Enter IPv4 address: ")
print("IP Class:", get_ip_class(ip))
