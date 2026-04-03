import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 9999))
server.listen(1)

print("Server listening on port 9999...")

conn, addr = server.accept()
print("Connected by:", addr)

conn.send("Hello, Client!".encode())

conn.close()
server.close()
