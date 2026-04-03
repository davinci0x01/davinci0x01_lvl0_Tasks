import socket

def check_telnet(ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    try:
        result = sock.connect_ex((ip, 23))
        if result == 0:
            print(f"Telnet (port 23) is OPEN on {ip}")
        else:
            print(f"Telnet (port 23) is CLOSED on {ip}")
    except Exception as e:
        print("Error:", e)
    finally:
        sock.close()


target_ip = input("Enter target IP: ")
check_telnet(target_ip)
