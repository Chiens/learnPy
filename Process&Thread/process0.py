#coding:utf-8
"useing fork function to create process in Unix/linux systerm."
"The child aways return 0, the father return a ID of child;and then the father will fork more than 1 child."
import os

print("Process (%s) start..." % os.getpid())

pid = os.fork()
#pid是fork()的返回值，它有3种结果： 1.在父进程中它返回子进程的PID， 2.在子进程中它返回0, 3.出现错误返回一个负值
#下面的代码会被复制一份放入子进程中运行，而父进程中依旧运行，它们都将返回结果
if pid == 0:
    print('I am child process (%s), and my parant is %s.' % (os.getpid(), os.getppid()))
else:
    print('I(%s) just created a child process (%s).' % (os.getpid(),pid))
