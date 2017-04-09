#coding:utf-8
"This is coding on python3"
import subprocess

print("$ nslookup www.python.org")
r = subprocess.call(['nslookup','www.python.org'])
print('Exit code：', r)