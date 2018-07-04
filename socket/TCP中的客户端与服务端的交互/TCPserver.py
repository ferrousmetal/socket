'''
TCP服务端
'''

import socket
name=socket.gethostname()
ip=socket.gethostbyname(name)
# 1.创建服务端的socket对象
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.绑定ip地址和端口号
server.bind((ip,8000))
# 3.监听是否有客户端接入 参数是监听的个数
server.listen(5)
print("服务器启动成功")
# 4.同意连接
client,add=server.accept()
print("客户端接入了",add)
# 5.接受数据recive
while True:
    data = client.recv(1024)
    # 解码，将二进制转化为字符串
    print("客户端说：",data.decode())
    data1=input("请输入要给客户端回复的数据：")
    client.send(data1.encode())

