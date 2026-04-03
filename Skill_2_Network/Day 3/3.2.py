# Server code

import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(("127.0.0.1", 5000))

print("UDP server is listening on port 5000...")

data, addr = server.recvfrom(1024)
print("Received message:", data.decode())

server.close()

# Client code

import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = input("Enter a message to send to the UDP server: ")
client.sendto(message.encode(), ("127.0.0.1", 5000))

client.close()
