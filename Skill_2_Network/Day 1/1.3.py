filename = "ips.txt"

def is_ipv4(word):
    parts = word.split(".")
    
    if len(parts) != 4:
        return False
    
    for part in parts:
        if not part.isdigit():
            return False
        if not 0 <= int(part) <= 255:
            return False
    
    return True



with open(filename, "r") as file:
    for line in file:
        words = line.split()
        for word in words:
            if is_ipv4(word):
                print(word)
