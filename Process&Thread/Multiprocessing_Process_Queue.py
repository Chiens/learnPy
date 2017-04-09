#coding:utf-8
"子进程之间用Queue进行通信"
from multiprocessing import Process, Queue
import os, time, random

#向队列写入
def write(q):
    print("Process to write: %s" % os.getpid())
    for value in ['A','B','C']:
        print('Put %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())

#从队列读取
def read(q):
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from queue." % value)

if __name__ == '__main__':
    #father process create queue
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    #start subprocess to write value
    pw.start()
    #start subprocess to read value
    pr.start()
    #wait subprocess pw over
    pw.join()
    #subprocess pr 是一个死循环，强制终止
    pr.terminate()