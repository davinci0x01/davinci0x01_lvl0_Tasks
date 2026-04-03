import socket

ip = input("Enter IP address to scan: ")

print("Scanning first 1000 ports...")

for port in range(1, 1001):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    result = sock.connect_ex((ip, port))
    if result == 0:
        print(f"Port {port} is OPEN")

    sock.close()
