#coding:utf-8
'''UDP-visitor-test'''

import socket

visitor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

addr = ('127.0.0.1', 9999)

for data in [b'Bob', b'Miss', b'Alex']:
    visitor.sendto(data, addr)
    print(visitor.recv(1024).decode('utf-8'))