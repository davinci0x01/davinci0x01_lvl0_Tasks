def is_privileged_port(port):
    return 0 <= port <= 1023


port = int(input("Enter port number: "))

if is_privileged_port(port):
    print("Privileged port")
else:
    print("Non-privileged port")
