#coding:utf-8
'''这是分布式计算的工作程序'''

import time, queue
from multiprocessing.managers import BaseManager

#创建QueueManager
class QueueManager(BaseManager):
    pass

#从网络上获取Queue
QueueManager.register('get_task_queue')
QueueManager.register('get_result_queue')

#连接到服务器，即task_master.py
server_address = '127.0.0.1'
print('Connect to server %s...' % server_address)
m = QueueManager(address=(server_address, 5000), authkey=b'abc')
m.connect()

#获取Queue的对象
task = m.get_task_queue()
result = m.get_result_queue()

#把从task中获取的任务执行，并将结果写入result中
for i in range(10):
    try:
        n = task.get(timeout=1)
        print('Run task %d * %d...' % (n,n))
        r = '%d * %d = %d' % (n, n, n*n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')

#任务结束
print('worker exit.')