#coding:utf-8
'''这个是socket模块网络编程的练习文件,这是以TCP方式进行的与服务器通信
注意它们之间的通信数据类型是bytes'''
import socket

#创建一个socket对象
visitor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
visitor.connect(('127.0.0.1', 9999))

#接受服务器传来的消息
print(visitor.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    visitor.send(data)
    print(visitor.recv(1024).decode('utf-8'))
visitor.send(b'exit')
visitor.close()