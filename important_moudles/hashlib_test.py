#coding:utf-8
'''这是hashlib的练习:根据用户输入的口令，计算出存储在数据库中的MD5口令'''

import hashlib

db = {}
cw, mw = 'clearwords', 'md5words' #password的两种形式

#获取password相应的md5口令
def calc_md5(pws):
    md5 = hashlib.md5()
    md5.update((pws+'chiens').encode('utf-8'))
    return md5.hexdigest()

#向数据库中写入用户信息
def save_user(username, pws):
    clear = cw, pws
    md = mw, calc_md5(pws)
    password = dict([clear, md])
    db[username] = password
    print('用户信息保存完毕。')

#用户登陆
def login(username, pws):
    if username in db:
        if calc_md5(pws) in db[username][mw]:
            return 1
        return 2
    return 0

#用户查询密码
def query(username):
    print("进入查询。")
    a = input("1.查询明文 2.查询摘要")
    if a == '1':
        print(db[username][cw])
    else:print(db[username][mw])


def main():
    while True:
        print("1,login  2.registered 3.exit")
        behavior = input('\n:')
        if behavior == '1':
            username = input("Enter your username:")
            if username in db:
                password = input("Enter your password:")
                if calc_md5(password) in db[username][mw]:
                    print('Welcome!')
                    print('是否查询密码?')
                    a = input('(y/n):')
                    if a == 'y':
                        query(username)
                    else:continue
                else:print("Password is wrong.")
            else:print("Username is wrong.")
        elif behavior == '2':
            username = input("Enter your username:")
            password = input("Enter your password:")
            save_user(username,password)
        else:
            break

if __name__ == '__main__':
    main()