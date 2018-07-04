'''
TCP客户端
特点：必须要建立连接 才可以发送数据
1.导入socket模块
2.创建socket对象  指定通信协议（TCP、UDP）
'''
import socket
name=socket.gethostname()
ip=socket.gethostbyname(name)
# socket.AF_INET：IPV4 socket_stream:TCP协议
# 1.创建socket对象
client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 2.建立连接(ip 端口号)
client.connect((ip,8000))
# 3.发送数据 对字符串进行一个编码(转化成二进制)
while True:
    data=input("请输入要发送的信息：")
    client.send(data.encode())

    data1=client.recv(1024)
    print("服务端说：",data1.decode())
