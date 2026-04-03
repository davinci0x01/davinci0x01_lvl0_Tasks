def is_valid_port(port):
    return port.isdigit() and 0 <= int(port) <= 65535


port = input("Enter port number: ")

if is_valid_port(port):
    print("Valid port number")
else:
    print("Invalid port number")
