#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
@解释：通过pop3获取最新的一封邮件
'''
import poplib
from email.parser import Parser

class GetMail(object):
    def __init__(self):
        self.email = input("Email:")
        self.password = input("Password:")  #如果是163邮箱，这里要填授权码
        self.pop_server = input("POP3 server:")
        self.server = poplib.POP3(self.pop_server)
        try:
            self.debug = int(input("Do you want to open(1)/close(0) debug(input 1/0):"))
            if self.debug == 0 or self.debug == 1:
                pass
            else:raise TypeError
        except TypeError:
            print("Please input '1' or '0' to open/close debug.")
        print(self.server.getwelcome().decode('utf-8'))
    def connect_pop3(self):
        self.server.set_debuglevel(self.debug)
        self.server.user(self.email)
        self.server.pass_(self.password)
        self.mail_num, self.mail_size = self.server.stat()  #邮件数量和大小
        self.resp, self.mails, self.octets = self.server.list() #返回所有邮件的编号
        print("Mails:", self.mails)
        return self
    def get_mail(self):
        cho = input("%s emails.\n"
                    "A.The first email.\n"
                    "B.The last.\n"
                    "C.Another(2~n):" % len(self.mails))
        if cho == 'A':
            self.index = 1
        elif cho == 'B':
            self.index = len(self.mails)
        elif cho == 'C':
            num = int(input("Which one do you want to load:"))
            if num in range(2,len(self.mails)):
                self.index = num
            else: print('Number outside range.')
        else:print("Wrong...")
        #lines存储了邮件原始文本的每一行
        self.get_resp, self.get_lines, self.get_octets = self.server.retr(self.index)
        self.msg_content = b'\r\n'.join(self.get_lines).decode('utf-8')
        print(self.msg_content)
        self.msg = Parser.parsestr(self.msg_content)

    def quit(self):
        self.server.quit()

if __name__ == '__main__':
    my_mail = GetMail()
    my_mail.connect_pop3()
    my_mail.get_mail()
    my_mail.quit()