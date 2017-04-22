#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
@file:$(NAME).py
@time:$(DATE) $(TIME)
这个邮件没有主题等信息
'''

from email.mime.text import MIMEText


#构建一个纯文本文件
message = MIMEText('Hello, send by Python...', 'plain', 'utf-8')

#通过SMTP发送出去
from_addr = input('From:') #发件人邮箱
password = input('Password:') #密码
to_addr = input('To:') #收件人邮箱

#输入SMTP服务器地址,sina.com的是smtp.sina.com,端口25
smtp_server = input('SMTP server:')

import smtplib
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], message.as_string())
server.quit()