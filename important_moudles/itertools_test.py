#coding:utf-8
'''itertools模块的练习'''

import itertools

#count()类
'''natuals = itertools.count(1)
def resual_natual(natual = natuals):
    for data in natual:
            yield data

value = resual_natual()
for i in range(10):
    print(next(value))
'''
natuals = itertools.count(1)
ns = itertools.takewhile(lambda x: x<=10, natuals)#使用takewhile函数截取一段
print("This is test of count():")
print(list(ns))

#cycle()
cs = itertools.cycle('ABC')
print("This is test of cycle():")
for i in range(6): #迭代6次
    print(next(cs))

#repeat()
rs = itertools.repeat("D", 3)
print("This is test of repeat():")
for r in rs:
    print(r)

#chain()
ci = itertools.chain('ABC','abc','XYZ')
print("This is test of chain():")
for n in ci:
    print(n)

#groupby()
print("This is test of groupby():")
kg = itertools.groupby('AAABBCCDAA')
for key,group in kg:
    print(key,list(group))

#忽略大小写
print('忽略大小写:')
kg_u = itertools.groupby('AaaBbbbCccDddaAA', lambda x: x.upper())
for key, group in kg_u:
    print(key,list(group))