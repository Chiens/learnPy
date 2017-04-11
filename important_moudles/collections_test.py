#coding:utf-8

'''这是python内建模块collections的练习文件，主要用于集合
    此处会练习的内容有：
    1.namedtuple(typename, field_names, verbose=False, rename=False)
    2.deque,实际上deque是来自_collections.py的一个类，从源码来看它就是双端队列
    3.defaultdict,它同样来自_collections.py的一个类，defaultdict(dict)
    4.OrderedDict(dict),它在位置在collecitons/__init__.py
    5.Counter(dict)类
'''

from collections import *
from copy import deepcopy
#namedtuple('名称', [属性list])
print('1.关于namedtuple()函数的示例：')
point = namedtuple('Point',['x', 'y'])
p = point(1,2)
print(' '*2 +'p.x=%s, p.y=%s.' % (p.x, p.y))
#例如一个圆
circle = namedtuple('Circle', ['x', 'y', 'r'])
c = circle(0,0,1)
print(' '*2 +'这是一个圆的座标：c.x=%s, c.y=%s, c.r=%s' % (c.x, c.y, c.r))

#双端队列deque(序列)
q = deque(['a', 'b', 'c'])
temp_q = deepcopy(q)
temp_q.append('x')
q0 = deepcopy(temp_q)
temp_q.appendleft('y')
q1 = deepcopy(temp_q)
temp_q.pop()
q2 = deepcopy(temp_q)
temp_q.popleft()
q3 = deepcopy(temp_q)
print('2.deque具备相比序列更加高效的插入和删除打操作。')
print(' '*2 + '使用deque(序列)生成一个双端队列:', q)
print(' '*2 + 'q.append(\'x\')-->', q0)
print(' '*2 + 'q.appendleft(\'y\')-->', q1)
print(' '*2 + "q.pop()-->", q2)
print(' '*2 + "q.popleft()-->", q3)

#defaultdict(f)，它的作用就是在dict的key不存在时，会返回一个默认值.
#等同于dict.get('key', 'N/A'),或者是使用dict.fromkeys([key0,key1,key2],'N/A')所创建的dict
dd = defaultdict(lambda :'N/A')
dd['key0'] = 'abc'
dd['key1'] = '123'
print("3.设置了dd['key0', 'key1']:"
      "\n%sdd['key0']--> %s"
      "\n%sdd['key1']--> %s"
      "\n%s而未设置的dd['key4']--> %s" % ('  ', dd['key0'], '  ',dd['key1'], '  ',dd['key4']))
print('%s它的作用就在于创建一个就算是不存在的key也具备默认值的dict' % '  ')

#OrderedDict类,它就是一个dict，不过它的key是按照写入顺序排序的，它具有‘先入先出’的特点
Odict = OrderedDict
d = dict([('a', 1), ('b', 2), ('c', 3)])
od = Odict([('a', 1), ('b', 2), ('c', 3)])
print("4.普通dict:", d, "写入：d = dict(['a', 1], ['b', 2], ['c', 3])\n",
      " " +"OderDict:", od, "写入：od = Odict(['a', 1], ['b', 2], ['c',3])")

#Counter计数器,没有什么内容,它也是dict的一个子尖
c = Counter()
for char in 'programing':
      c[char] += 1
print("4.Counter对象统计单词'programing'中各字母的数量:", c)