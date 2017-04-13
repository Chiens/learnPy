#coding:utf-8
'''写一个能去掉‘=’的base64函数'''
import base64, re

class My_safe_base64(object):
    def __init__(self):
        pass

    #编码
    def encode(self,str):
        if type(str) is not type(b'string'):
            self.str = str.encode(encoding = 'utf-8')
        self.code = base64.b64encode(self.str)
        self.str_code = self.code.decode()
        self.result_code_str = self.str_code.strip('=').encode(encoding = 'utf-8')
        return self.result_code_str

    #解码
    def decode(self,code_str):
        if type(code_str) is type(b'a'):
            self.ble = len(code_str) % 4
            self.add_num = 4 - self.ble
            self.result_code = code_str if self.ble == 0 else code_str + b'='*self.add_num
            return self.result_code
        else:
            return '格式不对'


if __name__ == '__main__':
    while True:
        pro = My_safe_base64()
        cho = input('Which choice would you like to do:'
                    '\n%s1.encode;'
                    '\n%s2.decode;'
                    '\n%s3.Quite'
                    '\nplease enter the number:' % ('  ', '  ', '  '))
        if cho == '1':
            str = input('Enter the string what you want to encod:')
            result = pro.encode(str)
            print('This is the result:\n%s%s\n\n' % ('  ', result))
        elif cho == '2':
            str = input('Enter the code what you want to decode'
                        '(不要加b和\"\'\"，这个数据还会继续处理如：YWJjZA):')
            str = str.encode(encoding='utf-8')
            result_code = pro.decode(str)
            result = base64.b64decode(result_code)
            print('This is the result:'
                  '\n%s%s --解码--> %s\n\n' % ('  ', result_code, result))
        else:
            break