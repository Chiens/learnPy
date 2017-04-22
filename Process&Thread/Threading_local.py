#coding:utf-8
"在全局dic中存放每个线程自己的变量，既方便线程使用，又方便函数调用"
import threading

#创建全局ThreadLocal对象
local_student = threading.local()

def process_student():
    std = local_student.student
    print('Hello, %s (in %s).' % (std, threading.current_thread().name))

def process_thread(name):
    #绑定全局ThreadLocal的student对象
    local_student.student = name
    process_student()

if __name__ == '__main__':
    t1 = threading.Thread(target=process_thread, args=('Alice',), name='Thread-A')
    t2 = threading.Thread(target=process_thread, args=('Bob',), name='Thread-B')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
