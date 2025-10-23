import socket
socket=socket.socket()
socket.bind(('localhost',9999))
# 127.0.0.1 = localhost
socket.listen(5)
client_socket,addr=socket.accept()
# client_socket2,addr2=socket.accept()
# client_socket3,addr3=socket.accept()
# client_socket4,addr4=socket.accept()
#www.google.com ---> ip 218.56.23.134:80
print(f"Connection from {addr} has been established!")
# client_socket.send("Hi there!".encode())
# inp=input("Enter your message to send to client: ")
# client_socket.send(inp.encode())
# message=client_socket.recv(1024)
# print(message.decode())

while True:
    inp=input("Enter your message to send to client: ")
    client_socket.send(inp.encode())
    message=client_socket.recv(1024)
    print(message.decode())
