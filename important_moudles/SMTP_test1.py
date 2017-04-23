#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
带头部文件的邮件
'''
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib

#格式化邮件地址
def _format_addr(s):
    name, addr = parseaddr(s)
    #返回formataddr对象，其参数是一个元组，里面的name要经过Header编码
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input("From:")
password = input("Password:")
to_addr = input("To:")
smtp_server = input("SMTP server:")

#构造HIMEText对象，如果是发送html则：MIMEText('<html><body><h1>Hello</h1></body></html>', 'html', 'utf-8')
msg = MIMEText("Hello, send by Python...", 'plain', 'utf-8')
#添加邮件头
msg['From'] = _format_addr("Python爱好者<%s>" % from_addr)
msg['To'] = _format_addr("管理员<%s>" % to_addr)
msg['Subject'] = Header("来自SMTP的问候...",'utf-8').encode()


server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1) #显示和SMTP服务器交互的信息
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()