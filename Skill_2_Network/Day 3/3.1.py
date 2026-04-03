# Server Code

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("127.0.0.1", 5000))
server.listen()

print("Server is listening on port 5000...")

conn, addr = server.accept()
print("Connected by:", addr)

message = conn.recv(1024).decode()
print("Received message:", message)

conn.close()
server.close()

# Client Code

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5000))

message = input("Enter a message to send to the server: ")
client.send(message.encode())

client.close()

