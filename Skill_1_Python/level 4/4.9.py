import socket

hostname = input("Enter hostname: ")

try:
    ip_address = socket.gethostbyname(hostname)
    print(f"The IP address of {hostname} is {ip_address}")
except socket.gaierror:
    print("Hostname could not be resolved")
