#coding:utf-8
"This file running on python3.4"
from multiprocessing import Pool
import os, time, random


#子进程
def long_time_task(name):
    print("Run task %s (%s)..." % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("Task %s runs %0.2f seconds." % (name, (end - start)))

if __name__ == "__main__":
    print("Parant process %s." % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print("Waiting for all subprocess done...")
    p.close()
    p.join()
    print("All subprocess done.")