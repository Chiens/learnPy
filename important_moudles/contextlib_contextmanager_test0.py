#coding:utf-8
'''上下文管理的实现，
即__enter__ __exit__ 方法的实现
以及with语句使用的关键'''


#一个正确实现上下文管理的类
class Query(object):
    def __init__(self, name):
        self.name = name
    def __enter__(self):
        '''这是正确实现上下文管理的关键方法之一'''
        print("Begin")
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        '''这是正确实现上下文管理的关键方法之一'''
        if exc_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print("Query info about %s..." % self.name)

#运行
def main(name):
    with Query(name) as q:
        q.query()

if __name__ == '__main__':
    name = input("Enter your name:")
    main(name)