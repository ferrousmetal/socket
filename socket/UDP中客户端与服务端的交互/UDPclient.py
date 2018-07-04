import socket

server=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(("10.35.161.6",8000))
data=server.recv(1024)
print(data.decode())
