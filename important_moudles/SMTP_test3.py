#!usr/bin/env python
#encoding:utf-8
'''
@version:python3.4
@author:Chiens
@解释：把图片嵌入到正文中发送，使用加密传输
1.用添加附件的方式把图片添加进去
2.用html写邮件内容并在合适的位置放入图片
3.创建SMTP对象后，立刻调用starttls()方法
(注意：邮件对象仍然是MIMEMultipart对象，图片仍然要先attach进去，接下来才是调用图片)
'''
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.utils import parseaddr,formataddr
from email.header import Header
from email.mime.text import MIMEText
import smtplib
import re

class MyMessage(object):
    def __init__(self):
        self.from_addr = input("From:")
        self.password = input("Password:")
        self.to_addr = input("To:")
        self.smtp_server = input("SMTP server:")
        self.msg = MIMEMultipart()
        self.msg['From'] = self._format_addr("Python爱好者<%s>" % self.from_addr)
        self.msg['To'] = self._format_addr("管理员<%s>" % self.to_addr)
        self.msg['Subject'] = Header("来自SMTP的问候...", 'utf-8').encode()

    def get_picture(self):
        '''最好是写一个正则方法来匹配出图片名字和格式'''
        self.pic_addr = input('Picture address:')
        self.pic_name, self.pic_att = self._get_pic_name(self.pic_addr)
        with open(self.pic_addr, 'rb') as f:
            self.mime = MIMEBase('image', self.pic_att, filename = self.pic_name)
            # 加上头信息
            self.mime.add_header('Content-Disposition', 'attachment', filename='tdr.jpg')
            self.mime.add_header('Content-ID', '<0>')
            self.mime.add_header('X-Attachment-ID', '0')
            # 读入附件内容
            self.mime.set_payload(f.read())
            # 编码,用Base64
            encoders.encode_base64(self.mime)
            # 加到MIMEMultipart中
            self.msg.attach(self.mime)
            self.msg.attach(MIMEText('<html><body>'
                                '<h1>Hello!</h1>'
                                '<p><img src="cid:0"></p>'
                                '<body/></html>', 'html', 'utf-8'))
    def send_msg(self):
        self.server = smtplib.SMTP(self.smtp_server, 25)
        self.server.starttls() #使用加密传输
        self.server.set_debuglevel(1)
        self.server.login(self.from_addr, self.password)
        self.server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        self.server.quit()

    '''邮件头部内容解析方法'''
    @classmethod
    def _format_addr(cls, string):
        name, addr = parseaddr(string)
        return formataddr((Header(name, 'utf-8').encode(), addr))

    '''正则匹配方法,返回图片的名字和格式'''
    @classmethod
    def _get_pic_name(cls, string):
        pattern = r'.([a-zA-Z]+)(\.{1})([a-zA-Z]{3})' #匹配 字母(1个或多个).字母(三个)
        m = re.search(pattern, string)
        return m.group(1), m.group(3)

if __name__ == '__main__':
    message = MyMessage()
    message.get_picture()
    message.send_msg()