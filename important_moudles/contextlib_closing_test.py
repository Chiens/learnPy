#coding:utf-8
'''contextlib模块中colsing类的练习'''
from contextlib import closing
from urllib.request import urlopen

#urlopen获取的对象没有实现上下文管理
url_obj = urlopen('https://www.python.org')

#使用closing类可以让它实现上下文管理
with closing(url_obj) as page:
    for line in page:
        print(line.decode('utf-8'))