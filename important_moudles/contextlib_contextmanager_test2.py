#coding:utf-8
'''
用@contextmanager实现,在某段代码执行前后自动执行特定代码
'''
from contextlib import contextmanager

@contextmanager
def tag(tab):
    try:
        print("<%s>" % tab)
        yield
    except:
        print("Something wrong...")
    finally:
        print("</%s>" % tab)

if __name__ == '__main__':
    with tag('h'):
        print("Hello,")
        print("world!")