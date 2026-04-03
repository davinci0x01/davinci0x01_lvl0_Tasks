ip = input("Enter an IP address: ")

parts = ip.split(".")
is_valid = True

if len(parts) != 4:
    is_valid = False
else:
    for part in parts:
        if not part.isdigit() or not 0 <= int(part) <= 255:
            is_valid = False
            break

if is_valid:
    print("Valid IP address")
else:
    print("Invalid IP address")
