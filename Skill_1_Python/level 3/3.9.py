items = ["Nmap", "Wireshark", "Metasploit", "BurpSuite"]
result = ""
max_length = 0

for item in items:
    if len(item) > max_length:
        max_length = len(item)
        result = item
        
print("The longest item is:", result)