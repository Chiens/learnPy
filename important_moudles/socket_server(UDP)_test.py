#coding:utf-8
'''UDP'''

import socket,time,threading

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind(('127.0.0.1', 9999))
print('UDP server waiting for message...')

def udplink(sock, data, addr):
    print('One new message come from %s:%s' % addr)
    time.sleep(1)
    sock.sendto(('I have gotten your message, %s' % data.decode('utf-8')).encode('utf-8'), addr)
while True:
    data, addr = server.recvfrom(1024)
    t = threading.Thread(target=udplink, args=(server, data, addr))
    t.start()
    print('Message reply %s:%s.' % addr)