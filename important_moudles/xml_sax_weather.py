#coding:utf-8
'''
利用SAX编写程序解析Yahoo的XML格式的天气预报，获取当天和第二天的天气：
http://weather.yahooapis.com/forecastrss?u=c&w=2151330
参数w是城市代码，要查询某个城市代码，可以在weather.yahoo.com搜索城市，浏览器地址栏的URL就包含城市代码
'''
from xml.parsers.expat import ParserCreate

class WeatherSaxHandle(object):
    def __init__(self):
        self.weather = dict()
        self.data = dict()
    def start_element(self, name, attrs):
        if name == 'yweather:location':
            '''保存地址'''
            self.weather['city'] = attrs['city']
            self.weather['country'] = attrs['country']
        #以下是时间上的每天大概天气
        elif name == 'yweather:forecast':
            if attrs['day'] == 'Wed':
                self.data['today'] = attrs
            elif attrs['day'] == 'Thu':
                self.data['tomorrow'] = attrs
        self.weather['data'] = self.data
    def end_element(self, name):
        pass
    def char_data(self, data):
        pass

def main(xml_data):
    weather_handler = WeatherSaxHandle()
    parser = ParserCreate()

    parser.StartElementHandler = weather_handler.start_element
    parser.CharacterDataHandler = weather_handler.char_data
    parser.EndElementHandler = weather_handler.end_element
    '''此处我犯了两个错误：
                        1.weather_handler.start_element() 加了这个“()”
                        2.parser.StartElement 这个属性没有写全。
    '''
    parser.Parse(xml_data)
    return weather_handler.weather

data = r'''<?xml version="1.0" encoding="UTF-8" standalone="yes" ?>
<rss version="2.0" xmlns:yweather="http://xml.weather.yahoo.com/ns/rss/1.0" xmlns:geo="http://www.w3.org/2003/01/geo/wgs84_pos#">
    <channel>
        <title>Yahoo! Weather - Beijing, CN</title>
        <lastBuildDate>Wed, 27 May 2015 11:00 am CST</lastBuildDate>
        <yweather:location city="Beijing" region="" country="China"/>
        <yweather:units temperature="C" distance="km" pressure="mb" speed="km/h"/>
        <yweather:wind chill="28" direction="180" speed="14.48" />
        <yweather:atmosphere humidity="53" visibility="2.61" pressure="1006.1" rising="0" />
        <yweather:astronomy sunrise="4:51 am" sunset="7:32 pm"/>
        <item>
            <geo:lat>39.91</geo:lat>
            <geo:long>116.39</geo:long>
            <pubDate>Wed, 27 May 2015 11:00 am CST</pubDate>
            <yweather:condition text="Haze" code="21" temp="28" date="Wed, 27 May 2015 11:00 am CST" />
            <yweather:forecast day="Wed" date="27 May 2015" low="20" high="33" text="Partly Cloudy" code="30" />
            <yweather:forecast day="Thu" date="28 May 2015" low="21" high="34" text="Sunny" code="32" />
            <yweather:forecast day="Fri" date="29 May 2015" low="18" high="25" text="AM Showers" code="39" />
            <yweather:forecast day="Sat" date="30 May 2015" low="18" high="32" text="Sunny" code="32" />
            <yweather:forecast day="Sun" date="31 May 2015" low="20" high="37" text="Sunny" code="32" />
        </item>
    </channel>
</rss>
'''


if __name__ == '__main__':
    weather = main(data)

    print('Location:', str(weather['city']), str(weather['country']))
    print("Weather", str(weather['data']))
