import socket
socket=socket.socket()
socket.connect(('localhost',9999))
# message=socket.recv(1024)
# print(message.decode())
# # socket.send("Hello from client".encode())
# inp=input("Enter your message: ")
# socket.send(inp.encode())
while True:
    message=socket.recv(1024)
    print(message.decode())
    inp=input("Enter your message: ")
    socket.send(inp.encode())