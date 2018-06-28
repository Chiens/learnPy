# !/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
'''
@ Author: Chiens
@ Time  : 2018-6-26
@ File  : list_test0.py
@ Context:This program is used to show list function.
'''

import time
from collections import deque

class Mylist(object):
    def __init__(self):
        self.__doc__ = ['list_app',
                        'list_ext',
                        'list_ins',
                        'list_rem',
                        'list_pop',
                        'list_cle',
                        'list_ind',
                        'list_cou',
                        'list_sor',
                        'list_rev',
                        'list_cop',
                        'list_sta',
                        'list_que',
                        'list_dec',
                        'list_mat',
                        'list_del']
        self.my_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    def list_creat(self):
        self.new_list = list()
        #print(type(self.new_list))
        while True:
            self.stop = int(input('继续(1/0)?:'))
            if self.stop == 1:
                self.new_value = input('Enter the value to add in new list:')
                self.new_list.append(self.new_value)    #这里不能用self.new_list = self.new_list.append() 这样会导致slef.new_list变为NoType
                #print(type(self.new_list))
            elif self.stop == 0:
                break
            else:print('不要乱输入。。')
        return  self.new_list
    def list_app(self):
        self.app_value = input('Enter what you want to add into this list:')
        self.my_list.append(self.app_value)
        return self.my_list
    def list_ext(self):
        print('At first you need to creat a new list to extend on old list.')
        self.new_list = self.list_creat()
        self.my_list.extend(self.new_list)
        return self.my_list
    def list_ins(self):
        print('This is a operation to insert value in the list.'
              '\n list.insert(0, value),this will insert a value on the front of list')
        print('这是现在列表的样子:', self.my_list)
        self.ins_value = input('请输入想要插入的值(还是中文好看):')
        while True:
            try:
                self.ins_num = int(input('输入要插入的位置(但是我为什么要和自己说这些):'))
                self.my_list.insert(self.ins_num, self.ins_value)
                break
            except ValueError:
                print('位置输入请用数字..')
        print('这是插入操作后的样子:', self.my_list)
        return
    def list_rem(self):
        print('This operation list.remove(x) will delete the first like x in list.')
        print(self.my_list)
        self.rem_value = input('输入要删除的值:')
        self.my_list.remove(self.rem_value)
        print(self.my_list)
        return
    def list_pop(self):
        print('This operation will pop the last value from list.')
        print(self.my_list)
        try:
            self.pop_value = int(input('输入要弹出值的位置(不输入则弹出最后一个)：'))
            print('弹出的值是：', self.my_list.pop(self.pop_value))
        except ValueError:
            print('弹出的值是：', self.my_list.pop())
        print('现在列表：', self.my_list)
        return
    def list_cle(self):
        print('这个是列表清除操作，操作之后当前列表会被清空。')
        print(self.my_list)
        self.my_list.clear()
        time.sleep(3)
        print(self.my_list)
        return
    def list_ind(self):
        print('这是一个查询操作list.index(x)，返回x所在位置。')
        self.ind_num = input('输入要查询的值所在位置吧：')
        try:
            self.ind_num = int(self.ind_num)
            print('这个值为：',self.my_list.index(self.ind_num))
        except ValueError:
            print('这个值为：', self.my_list.index(self.ind_num))
        return
    def list_cou(self):
        print('这个操作list.count(x)用于返回x在列表中的个数。')
        self.coun_value = input('输入要查询的值：')
        try:
            self.coun_value = int(self.coun_value)
            print('此元素的个数为：', self.my_list.count(self.coun_value))
        except ValueError:
            print('此元素的个数为：', self.my_list.count(self.coun_value))
        return
    def list_sor(self):
        print('这个操作 list.sort() 是一个对列表进行排序的操作，它会对列表本身进行个性。'
              '\n而另一个 list.sorted()则不改变列表本身，返回一个新的被排序后的列表')
        print('排序前的列表：', self.my_list)
        print('开始变身,哈哩噜啾啾嗨呀呀....')
        time.sleep(3)
        self.my_list.sort()
        print('排序后的列表：', self.my_list)
        return
    def list_rev(self):
        print('这个操作 list.reverse() 是将列表以当前状态进行反序，它是对列表本身进行改变')
        print('当前列表：', self.my_list)
        print('开始变身，出来吧！光能使者!!!')
        time.sleep(3)
        self.my_list.reverse()
        print('排序后的列表：', self.my_list)
        return
    def list_cop(self):
        print('这是一个对列表进行淺复制的操作，list.copy()。')
        self.cop_list = self.my_list.copy()
        print('复制后的列表：', self.cop_list)
        return
    def list_sta(self):
        '''useing list just like a stack with append and pop functions.'''
        print('这个操作是用列表来实现栈的方法。主要会使用到尾插的 append() 和 尾弹的 pop()')
        print('这是栈的当前状态：', self.my_list)
        while True:
            self.sta_choice = int(input('入栈操作扣1, 出栈操作扣2，不操作扣3:'))
            if self.sta_choice == 1:
                self.sta_in = input('输入要入栈的数据：')
                try:
                    self.my_list.append(int(self.sta_in))
                    print(self.my_list)
                except ValueError:
                    self.my_list.append(self.sta_in)
                    print(self.my_list)
            elif self.sta_choice == 2:
                print('开始出栈操作...')
                time.sleep(3)
                try:
                    print('出栈的数据为：', self.my_list.pop())
                except IndexError:
                    print('空了...')
            elif self.sta_choice == 3:
                print('再见..')
                break
            else:print('还是别乱输入啊。。')
        return
    def list_que(self):
        '''useing list just like a queue with deque.'''
        self.my_que = deque(self.my_list)
        print('现在的列表变为队列：', self.my_que)
        while True:
            try:
                self.que_choice = int(input('选择想要进行的操作吧：'
                                            '\n1.队列前端插入数据'
                                            '\n2.队列后端插入数据'
                                            '\n3.队列前端弹出数据'
                                            '\n4.队列后端弹出数据'
                                            '\n5.退出'))
                if self.que_choice == 1:
                    self.que_addvalue = input('输入想要插入的数据：')
                    self.my_que.appendleft(self.que_addvalue)
                    print('插入后的队列：', self.my_que)
                elif self.que_choice == 2:
                    self.que_addvalue = input('输入想要插入的数据：')
                    self.my_que.append(self.my_que)
                    print('插入后的队列：', self.my_que)
                elif self.que_choice == 3:
                    print('弹出的数据：', self.my_que.popleft())
                    print('操作后的队列：', self.my_que)
                elif self.que_choice == 4:
                    print('弹出的数据：', self.my_que.pop())
                    print('操作后的队列：', self.my_que)
                elif self.que_choice == 5:
                    break
                else:raise ValueError
            except ValueError:
                print('不要输入奇怪的东西..')
        return
    def list_dec(self):
        '''列表推导式.'''
        print('这个东西其实是列表的一个特性，可以使用诸如： [for x in seq if x <n] 返回一个生成的列表。'
              '\n这就是列表推导式。')
        return
    def list_mat(self):
        '''matrix display with list.'''
        print('以列表来表示矩阵。')
        self.mat_matrix = [[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9],
                           [10, 11, 12]]
        self.mat_change = [[row[i] for row in self.mat_matrix] for i in range(len(self.mat_matrix)-1)]
        print('有一个矩阵：', self.mat_matrix)
        print('我们用一些方法将它进行转换，如：[[row[i] for row in matrix] for i in range(4)]转换为了', self.mat_change)
        return
    def list_del(self):
        '''这个是序列del操作在列表上的使用'''
        print('del list，可以依照索引来删除元素，也可以清空整个列表。')
        while True:
            try:
                print('这是当前列表：', self.my_list)
                self.del_choice = int(input('选择一个操作:\n'
                                            '1.删除元素'
                                            '2.清空列表'
                                            '3.exit'))
                if self.del_choice == 1:
                    self.del_list_choice = int(input('输入索引：'))
                    del self.my_list[self.del_list_choice]
                elif self.del_choice == 2:
                    del self.my_list
                elif self.del_choice == 3:
                    print('done')
                    break
                else: raise ValueError
            except ValueError:
                print('不要乱输入...')
        return self.my_list
if __name__ == '__main__':
    MyList = Mylist()
    while True:
        print('1.列表后入, 2. 列表连接,\n'
          '3.列表查询, 4.列表移除值,\n'
          '5.列表弹出值, 6.清除列表,\n'
          '7.列表插入, 8.列表元素统计,\n'
          '9.列表排序, 10.列表反序,\n'
          '11.列表复制(淺), 12.栈,\n'
          '13.队列, 14.列表推导式,\n'
          '15.矩阵, 16.删除操作')
        try:
            mychoice = int(input('选择一个要看的操作吧:'))
            if mychoice == 1:
                new_list = MyList.list_app()
                print('操作后的数列：', new_list)
            elif mychoice == 2:
                new_list = MyList.list_ext()
                print('操作后的数列：', new_list)
            elif mychoice == 0:
                new_list = MyList.list_creat()
                print('操作后的数列：', new_list)
            elif mychoice == 3:
                MyList.list_ind()
            elif mychoice == 4:
                MyList.list_rem()
            elif mychoice == 5:
                MyList.list_pop()
            elif mychoice == 6:
                MyList.list_cle()
            elif mychoice == 7:
                MyList.list_ins()
            elif mychoice == 8:
                MyList.list_cou()
            elif mychoice == 9:
                MyList.list_sor()
            elif mychoice == 10:
                MyList.list_rev()
            elif mychoice == 11:
                MyList.list_cop()
            elif mychoice == 12:
                MyList.list_sta()
            elif mychoice == 13:
                MyList.list_que()
            elif mychoice == 14:
                MyList.list_dec()
            elif mychoice == 15:
                MyList.list_mat()
            elif mychoice == 16:
                newlis = MyList.list_del()
                print('操作后的列表是：', newlis)
            else:raise ValueError
        except ValueError:
            print('选项错误，重来！')