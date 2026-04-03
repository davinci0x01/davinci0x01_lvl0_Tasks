import socket
import time

def measure_rtt(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(3)

    start_time = time.time()
    try:
        sock.connect((ip, port))
        end_time = time.time()
        rtt = (end_time - start_time) * 1000 # To convert to milliseconds
        print(f"RTT to {ip}:{port} = {rtt:.2f} ms")
    except Exception:
        print("Connection failed")
    finally:
        sock.close()


measure_rtt("8.8.8.8", 53)
