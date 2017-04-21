#coding:utf-8
'''
模拟iPhone向douban发送请求
此处有向douban加送了一个本来没有的头部
'''
from urllib import request

req = request.Request(r'https://www.douban.com/')

req.add_header('User-Agent',
               'Mozilla/6.0 '
               '(iPhone; CPU iPhone OS 8_0 like Mac OS X) '
               'AppleWebKit/536.26 (KHTML, like Gecko) '
               'Version/8.0 Mobile/10A5376e Safari/8536.25')
with request.urlopen(req) as f:
    print("Status:", f.status, f.reason)
    for key, value in f.getheaders():
        print("%s: %s" % (key, value))
    print('Data:', f.read().decode('utf-8'))