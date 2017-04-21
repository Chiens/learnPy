#coding:utf-8
'''
urllib中的各模块和方法练习与理解
request.rulopen()的练习
'''

import urllib.request

if __name__ == '__main__':
    with urllib.request.urlopen(r'https://api.douban.com/v2/book/2129650') as f:
        data = f.read()
        print("Status:", f.status, f.reason)
        for key, value in f.getheaders():
            print("%s: %s" % (key, value))
        print('Data:', data.decode('utf-8'))
