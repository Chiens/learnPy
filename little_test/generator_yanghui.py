#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
@解释：杨辉三角
'''

def creatnew(list = [1]):
    '''创建一个可以用任意一个列表作为开始的杨辉三角生成器'''
    list_tmp = [0]+list+[0]
    list_len = len(list_tmp)
    list_index = 0
    list_new = []
    while list_index <= list_len-2:
        value = list_tmp[list_index]+list_tmp[list_index+1]
        list_new.append(value)
        list_index += 1
    return list_new
def yanghui():
    list_yang = [1]
    while True:
        yield list_yang
        list_yang = creatnew(list_yang)


if __name__ == '__main__':
    num = int(input("Enter:"))
    n = 0
    for i in yanghui():
        print(i)
        n += 1
        if n == num:
            break