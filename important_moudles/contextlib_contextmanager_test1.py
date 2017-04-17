#coding:utf-8
'''contextlib模块中的contextmanager装饰器。
@contextmanager这个decorator接受一个generator，
用yield语句给with ... as var把变量输出出去，然后，with语句就可以正常地工作了。'''

from contextlib import contextmanager

class Query(object):
    def __init__(self, name):
        self.name = name
    def query(self):
        print("Query info about: %s" % self.name)

@contextmanager
def creat_query(name):
    print("Begin")
    q =  Query(name)
    yield q
    print('End')

if __name__ == '__main__':
    with creat_query('Bob') as q:
        q.query()