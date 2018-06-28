#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
@解释：生成器实现fib
'''

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n += 1
    return 'done'

if __name__ == '__main__':
    my_max = int(input("Enter the max number:"))
    fib = fib(my_max)
    #以这种方式获取generator函数的返回值
    while True:
        try:
            x = next(fib)
            print("value: %s" % x,end=',')
        except StopIteration as e:
            print("Generator return: %s" % e.value)
            break