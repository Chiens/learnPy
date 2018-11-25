#coding:utf-8
'''
各进程的变量是独立的，而线程的是共享的，如果不处理这个问题会导致出错.
由于线程的调度是由操作系统决定的，当t1、t2交替执行时，只要循环次数足够多，balance的结果就不一定是0了
给change_it 加上一个锁
'''
from threading import Thread, Lock
import time

#实例化一个锁对象
lock = Lock()
balance = 0

def change_it(n):
    #先存后取，结果应该为0
    global balance
    balance += n
    balance -= n

def run_thread(n):
    for i in range(100000):
        #对change_it加锁,其它线程就不能执行change_it()
        lock.acquire()
        try:
            change_it(n)
        #一定要记得在操作结束后释放锁
        finally:
            lock.release()

if '__name__' == '__main__':
    t1 = Thread(target=run_thread, args=(5,))
    t2 = Thread(target=run_thread, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(balance)