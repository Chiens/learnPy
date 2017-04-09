#coding:utf-8
'''这是分布式计算的管理程序'''

import random, time, queue
from multiprocessing.managers import BaseManager

#创建收发队列
task_queue = queue.Queue()
result_queue = queue.Queue()

#继承BaseManager
class QueueManager(BaseManager):
    pass

#把两个queue注册到网络上，callable参数关联Queue对象
QueueManager.register('get_task_queue', callable=lambda :task_queue)
QueueManager.register('get_result_queue', callable=lambda :result_queue)

#绑定端口，设置验证码'abc'
manager = QueueManager(address=('', 5000), authkey=b'abc')

#启动Queue
manager.start()

#获得通过网络访问的Queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()

#放入任务
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)

#从result接收结果
print('Try get result...')
for i in range(10):
    r = result.get(timeout = 10)
    print('Result: %s.' % r)

#关闭
manager.shutdown()
print('master exit.')