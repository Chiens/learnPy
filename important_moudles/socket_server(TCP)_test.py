#coding:utf-8
'''这是本机服务器，TCP方式进行'''
import socket,time,threading

local_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#绑定本机端口
local_server.bind(('127.0.0.1', 9999))

#监听,等待连接最大数为5个
local_server.listen(5)
print('Waiting for connection...')
#local_server.send(('Here are you.').encode('utf-8')) 是行不通的，send只能在通信连接建立后才行

#连接处理线程
def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8')) #这里的传送内容一定要用encod()以byte形式发送
    sock.close()
    print('Connection from %s:%s' % addr)

#用一个永久次循环来接受连接
while True:
    sock, addr = local_server.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()