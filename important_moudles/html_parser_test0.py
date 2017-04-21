#coding:utf-8
'''
用于解析html的模块,html.parser
'''
from html.parser import HTMLParser
from html.entities import name2codepoint
from urllib import request

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        '''和下面的是一对 <some> ... </some> 中的开始'''
        print("<%s>" % tag)
    def handle_endtag(self, tag):
        '''和上面的相对应 <some> ... </some> 中的结尾'''
        print("</%s>" % tag)
    def handle_startendtag(self, tag, attrs):
        '''形如<meta ..../>'''
        print("<%s/>" % tag)
    def handle_data(self, data):
        '''顾名思意，是标签中的内容如：<a>data</a>'''
        print(data)
    def handle_comment(self, data):
        '''<!--data--> 注释中的内容'''
        print("<!--%s-->" % data)
    def handle_entityref(self, name):
        '''处理实体引用,如空格在html中可以用&nsp;表示，也可以用&#1234;表示.英文的就叫“实体引用”，数字的就叫“字符引用”'''
        print("&%s;(我就是实体引用)" % name)
    def handle_charref(self, name):
        '''处理字符引用'''
        print("&#%s;(我就是字符引用)" % name)
webpage_test0 = '''
    <html>
        <head></head>
        <body>
        <!-- test html parser -->
            <p>Some <a href=\"#\">html</a> HTML&nbsp;tutorial...&#1234;<br>END</p>
        </body>
    </html>
    '''

'''
#使用urllib中的request类中的方法urlopen获取
response = request.urlopen(r'https://www.baidu.com',timeout=3)
webpage = response.read()   #读取成文件
webpage = webpage.decode('utf-8')   #将格式bytes-->str
'''
def myurlopen(url):
    response = request.urlopen(url)
    webpage = response.read()
    return webpage.decode('utf-8')

page = myurlopen(r'https://www.python.org/events/python-events/')
parser = MyHTMLParser()
parser.feed(page)