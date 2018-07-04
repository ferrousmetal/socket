import socket

data=input("请输入：")
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
client.sendto(data.encode(),("10.35.161.6",8000))
