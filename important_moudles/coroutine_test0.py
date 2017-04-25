#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
@解释：协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后，切换回生产者继续生产。
'''

#消费者
def consumer():
    r = ''
    while True:
        n = yield r #第一次没有运行到n被赋值，如果没有send传入，n被赋的值永远是None。
                    # yield会把r返回出整个函数,然后就冻结(激活时就从此运行)，先给n赋值None，继续到yield。
        if not n:
            return
        print("[CONSUMER] Consuming %s..." % n)
        r = '200 OK'

#生产者
def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n += 1
        print("[PRODUCE] Producing %s..." % n)
        r = c.send(n)
        print("[PRODUCE] Consumer return: %s" % r)
    c.close()

if __name__ == '__main__':
    c = consumer()
    produce(c)