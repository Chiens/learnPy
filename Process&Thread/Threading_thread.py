#coding:utf-8
"此篇旨在了解threading.Tread()类"
import threading, time

#新线程执行的代码
def loop():
    print('Thread %s is running...' % threading.current_thread().name)
    for n in range(5):
        print('Thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('Thread %s ended.' % threading.current_thread().name)

if '__name__' == '__main__':
    print('Thread %s is running...' % threading.current_thread().name)
    t = threading.Thread(target=loop, name='哈哈')
    t.start()
    t.join()
    print('Thread %s ended.' % threading.current_thread().name)