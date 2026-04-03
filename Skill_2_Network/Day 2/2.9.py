import socket

ip = input("Enter IP address: ")

start_port = 1
end_port = 500

print(f"Scanning UDP ports on {ip}...")

for port in range(start_port, end_port + 1):
    udp_sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_sock.settimeout(0.25)

    try:
        udp_sock.sendto(b"\x00", (ip, port))
        udp_sock.recvfrom(1024)
        print(f"Port {port} is OPEN (UDP)")
    except socket.timeout:
        print(f"Port {port} is OPEN or FILTERED (UDP)")
    except Exception:
        pass
    finally:
        udp_sock.close()
