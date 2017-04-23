#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
@解释：使用SMTP发送带附件的邮件
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
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

#邮件对象用MIMEMultipart,可以添加附件
msg = MIMEMultipart()
#添加邮件头
msg['From'] = _format_addr("Python爱好者<%s>" % from_addr)
msg['To'] = _format_addr("管理员<%s>" % to_addr)
msg['Subject'] = Header("来自SMTP的问候...",'utf-8').encode()

#邮件正文
msg.attach(MIMEText('Send with file...(I used bytes)', 'plain', 'utf-8'))


#添加附件就是加上一个MIMEBase,从本地读取一个图片
with open('/home/chiens/图片/Images/tdr.jpg', 'rb') as f:
    #
    mime = MIMEBase('image', 'jpg', filename = 'tdr.jpg')
    #加上头信息
    mime.add_header('Content-Disposition', 'attachment', filename = 'tdr.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-ID', '0')
    #读入附件内容
    mime.set_payload(f.read())
    #编码,用Base64
    encoders.encode_base64(mime)
    #加到MIMEMultipart中
    msg.attach(mime)

#发送邮件
server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_bytes())   #注意此处有图片的时候我是用的bytes
server.quit()
