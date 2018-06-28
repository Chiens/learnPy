# !/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
'''
@ Author: Chiens
@ Time  : （传统纪年4716年，西元2018年）。戊戌年，戊午月，戊子日
@ File  : set_test0.py
@ Context: 用于进行集合各项操作的实验练习
'''
import time

class Myset(object):
    '''This object is created to show main operation of set.'''
    def __init__(self):
        self.__doc__=['my_creat','my_add','my_delet','my_clear','my_find','my_len','my_change']
        self.seq = '这个实例用于展示集合的主要操作。'
        print(self.seq)
    def my_creat(self):
        print('Please choice a creat operation.')
        self.my_set = set()
        while True:
            self.my_choice = input('Enter to choice input new value or exit(1/0):')
            if self.my_choice == '1':
                try:
                    self.my_value = input('Enter the value:')
                    self.my_set.add(self.my_value)
                except TypeError:
                    return 'Something is wrong...'
            else:
                break
        return self.my_set
    def my_add(self):
        '''this is a operation of add&'''
        self.my_value = input('Please enter the value which you want to add into this set:')
        self.my_set.update(self.my_value)
        return self.my_set
    def my_delet(self):
        print('Please check this set:',self.my_set)
        self.my_delvalue = input('Enter the value what you want to delet:')
        self.my_set.discard(self.my_delvalue)   #remove 也可以，但是remove如果元素不存在会导致报错
        return self.my_set
    def my_clear(self):
        print('The set will be clear...')
        time.sleep(3)
        self.my_set.clear()
        return self.my_set
    def my_find(self):
        self.my_findvalue = input('Enter the value you want to find:')
        if self.my_findvalue in self.my_set:
                print('存在')
        else:print('不存在')
    def my_len(self):
        self.my_setlen = len(self.my_set)
        return self.my_setlen
    def my_change(self):
        print(self.my_set)
        self.my_coldvalue = input('Which one do you want to exchange:')
        self.my_cnewvalue = input('What do you want to excahnge to:')
        self.my_set.remove(self.my_coldvalue)
        self.my_set.add(self.my_cnewvalue)
        return self.my_set

if __name__ == "__main__":
    MySet = Myset()
    print(MySet.__doc__)
    myseq = 'There are many operations of set to choice:\n' \
            '1.creat a new set\n' \
            '2.add a value in set\n' \
            '3.delet a value from set\n' \
            '4.find a value from set\n' \
            '5.change a value in set\n' \
            '6.exit'
    print(myseq)
    while True:
        try:
            mychoice = int(input('Enter your choice:'))
            if mychoice == 1:
                MySet.my_creat()
                print(MySet.my_set)
            elif mychoice == 2:
                MySet.my_add()
                print(MySet.my_set)
            elif mychoice == 3:
                MySet.my_delet()
                print(MySet.my_set)
            elif mychoice == 4:
                MySet.my_find()
                print(MySet.my_set)
            elif mychoice == 5:
                MySet.my_change()
                print(MySet.my_set)
            else:break
        except ValueError:
            print('Please enter a nubmer from 1 to 5.')
            continue