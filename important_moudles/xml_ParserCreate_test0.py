#coding:utf-8
'''原实验练习'''
from xml.parsers.expat import ParserCreate

#通常SAX解析一个XML只要我们实现三个事件：start_element、char_data、end_element
class DefaultSaxHandler(object):
    def start_element(self, name, attrs):
        '''节点头部读取事件'''
        print("sax: start_element: %s, attrs: %s" % (name, str(attrs)))
    def end_element(self, name):
        '''节点尾部读取事件'''
        print("sax: end_element: %s" % name)
    def char_data(self, text):
        '''节点内容读取事件'''
        print("sax: char_data: %s" % text)

xml = r'''<?xml version = "1.0"?>
<ol>
    <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
    <li><a href = "/python">Python</a></li>
    <li><a href = "/ruby">Ruby</a></li>
</ol>
'''

handler = DefaultSaxHandler()
parser = ParserCreate() #Return a new XML parser object.

parser.StartElementHandler = handler.start_element
parser.EndElementHandler = handler.end_element
parser.CharacterDataHandler = handler.char_data

parser.Parse(xml)