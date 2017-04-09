#coding:utf-8
"This file is about process too, but useing multiprocessing-moudle which can be running every system."
from multiprocessing import Process
import os

#子进程代码
def run_proc(name):
    print('Run child process %s (%s)...' % (name, os.getpid()))

if __name__ == '__main__':
    print('Parant process %s.' % os.getpid())
    p = Process(target=run_proc, args=('test',))
    print('Child process will start.')
    p.start()
    p.join()
    print('Child process end.')