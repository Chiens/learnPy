#coding:utf-8
"用以练习datetime模块的小程序"
import datetime

#获取当前时间
now = datetime.datetime.now()
print('1.当前时间是：%s' % now)

#获取指定时间
date = datetime.datetime(2017,4,9,16,13)
print('2.指定的时间是：%s' % date)

#datetime转换为timestamp,即相对于1970-1-1 00：00 UTC+00:00的当前秒数
date_timestamp = date.timestamp()
print('3.相对于1970-1-1 00：00 UTC+00:00 过去了%s秒' % date_timestamp)

#timestamp转换为datetime
local_dt = datetime.datetime.fromtimestamp(date_timestamp)
dt = datetime.datetime.utcfromtimestamp(date_timestamp)
print('4.1970-1-1 00:00 UTC+00:00过去1491725580.0秒后的本地时间：%s, UTC时间：%s' % (local_dt,dt))

#str转换为datetime
rul = '%Y-%m-%d %H:%M:%S'
time_str = '2017-4-9 16:30:23'
cday = datetime.datetime.strptime(time_str, rul)
print('5.将字符串（%s）转换为datetime格式：%s' % (time_str, cday))

#datetime转换为str
now = datetime.datetime.now()
rul = '%a, %Y %b %d %H:%M'
print('6.将现在时间的datetime对象转换为str：%s --> %s' % (now, now.strftime(rul)))

#datetime加减,需要用到timedelta这个类
print('7.现在时间(%s) + 8 个小时：%s' % (now, now + datetime.timedelta(hours=8)))
print(' '*2+'现在时间(%s) - 8 分钟：%s' % (now, now - datetime.timedelta(minutes=8)))
print(' '*2+'现在时间(%s) + 8 天：%s' % (now, now + datetime.timedelta(days=8)))
print(' '*2+'现在时间(%s) + 8天，8小时，8分钟：%s' % (now, now + datetime.timedelta(days=8, hours=8, minutes=8)))

#本地时间转换为UTC时间
tz_utc_8 = datetime.timezone(datetime.timedelta(hours=8)) #创建时区UTC+8:00。即北京时间
utc_dt = now.replace(tzinfo=tz_utc_8) #设置当前时间为UTC+8:00
print('8.将当前时间[%s]强制设置为UTC+8:00为：[%s](如果没有变化，那么证明本地时间就是北京时间)' % (now, utc_dt))

#使用datetime.datetime.utcnow()获取当前的UTC时间
utc_dat = datetime.datetime.utcnow().replace(tzinfo=datetime.timezone.utc)
print('9.当前的UTC时间是：%s' % utc_dat)
#将UTC时间转换为北京时间
bj_dat = utc_dat.astimezone(datetime.timezone(datetime.timedelta(hours=8)))
print(' '*2 + '将当前UTC时间(%s)转换为北京时间(UTC+8:00)为：[%s]' % (utc_dat,bj_dat))
#将UTC时间转换为东京时间
tokyo_dat = utc_dat.astimezone(datetime.timezone(datetime.timedelta(hours=9)))
print(' '*2 + '将当前UTC时间(%s)转换为东京时间(UTC+9:00)为：[%s]' % (utc_dat,tokyo_dat))
#将北京时间转换为东京时间
tokyo_dat1 = bj_dat.astimezone(datetime.timezone(datetime.timedelta(hours = 9)))
print(' '*2 + '将当前北京时间(%s)转换为东京时间(UTC+9:00)为：[%s]' % (bj_dat,tokyo_dat1))
