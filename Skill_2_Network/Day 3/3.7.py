import socket
import threading
import time

HOST = "127.0.0.1"
PORT = 9999

def server():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen()

    conn, addr = srv.accept()

    # 1) Receive "SYN"
    msg = conn.recv(1024).decode()
    if msg == "SYN":
        print("Server: received SYN")

        # 2) Send "SYN-ACK"
        conn.send("SYN-ACK".encode())
        print("Server: sent SYN-ACK")

    # 3) Receive "ACK"
    msg = conn.recv(1024).decode()
    if msg == "ACK":
        print("Server: received ACK")
        print("Server: Handshake completed ✅")

    conn.close()
    srv.close()

def client():
    time.sleep(0.2)

    cli = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cli.connect((HOST, PORT))

    # 1) Send "SYN"
    cli.send("SYN".encode())
    print("Client: sent SYN")

    # 2) Receive "SYN-ACK"
    msg = cli.recv(1024).decode()
    if msg == "SYN-ACK":
        print("Client: received SYN-ACK")

        # 3) Send "ACK"
        cli.send("ACK".encode())
        print("Client: sent ACK")
        print("Client: Handshake completed ✅")

    cli.close()

t1 = threading.Thread(target=server)
t2 = threading.Thread(target=client)

t1.start()
t2.start()

t1.join()
t2.join()
