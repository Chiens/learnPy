# !/usr/local/bin/python3.6
# -*- coding: utf-8 -*-
'''
@ Author: Chiens
@ Time  : 2018-6-21
@ File  : dict_test0.py
@ Context:复习字典的特性、内建方法、多态方法。。
'''

class Common(object):
    def __init__(self):
        self.seq='这是一个包含了字典各种方法操作的对象。'
        self.mykey = range(10)
        self.mydict = dict()
        self.mydict = self.mydict.fromkeys(self.mykey, 'FuckYou')
        print(self.seq)
        self.mydictseq = 'This is dict(now):'
    def myadd(self):
        '''this method is a operation of show dict-add'''
        self.dikey = input('Enter the new key:')
        self.dival = input('Enter the new value:')
        self.mydict[self.dikey] = self.dival
        print(self.mydict)
    def mydel(self):
        '''this method is a operation of delet value or key from dict'''
        while True:
            self.mychoice = input('Please choice a operation:'
                                  '\n1. Delet a keys-value without return.'
                                  '\n2. Delet a keys-value with return.'
                                  '\n3. Delet all dict.'
                                  '\n4. Exit.')
            self.mychoice = int(self.mychoice)
            if self.mychoice is 1:
                print(self.mydictseq, self.mydict)
                self.delkey = int(input('Choice the key to delet:'))
                del self.mydict[self.delkey]
            elif self.mychoice is 2:
                print(self.mydictseq, self.mydict)
                self.delkey = int(input('Choice the key to delet:'))
                print(self.mydict.pop(self.delkey))
            elif self.mychoice is 3:
                print(self.mydictseq,self.mydict)
                self.mydict.clear()
                #del self.mydict
            else:break
        print(self.mydictseq, self.mydict)
    def myfind(self):
        '''this method is a operation of find value or key in dict'''
        self.myfindkey = int(input('Pleas enter a number of key:'))
        if self.myfindkey in self.mydict:
            print('The value is:', self.mydict[self.myfindkey])
        else:print('There is no value.')
    def mychange(self):
        '''this method is a operation of change value in dict'''
        self.mychangekey = int(input('Enter key:'))
        self.mychanegvalue = input('Enter value:')
        print('The oldvalue is', self.mydict[self.mychangekey])
        self.mydict[self.mychangekey] = self.mychanegvalue
        print('The newvalue is', self.mydict[self.mychangekey])


if __name__ == '__main__':
    ThisDict = Common()
    while True:
        print('Choice your operation:\n'
          '1.add\n'
          '2.delet\n'
          '3.find\n'
          '4.exchange\n'
          '5.Exit\n')
        mychoice = int(input(':'))
        if mychoice is 1:
            ThisDict.myadd()
        elif mychoice is 2:
            ThisDict.mydel()
        elif mychoice is 3:
            ThisDict.myfind()
        elif mychoice is 4:
            ThisDict.mychange()
        else:break