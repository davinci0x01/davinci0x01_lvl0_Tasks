import socket
import datetime

HOST = "0.0.0.0"
PORT = 8080

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print(f"Monitoring incoming TCP connections on port {PORT}...")

while True:
    conn, addr = server.accept()

    time_now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-5]

    log_message = f"[{time_now}] Connection from {addr[0]}"
    print(log_message)

    with open("connections.log", "a") as log_file:
        log_file.write(log_message + "\n")

    conn.close()
