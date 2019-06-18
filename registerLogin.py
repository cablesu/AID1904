from mysqlhelper import MysqlHelper
from hashlib import sha1
from getpass import getpass
from string

mysql=MysqlHelper('db5')
# 注册函数
def register():
    # 接收用户名
    username=input("请输入注册的用户名")

    sel='select username from user where username=%s'
    r=mysql.get_all(sel,L=username)
    if not r:
        # 用户名可用，接收用户输入密码
        pwd1=getpass('请输入密码')
        pwd2=getpass('请再次输入密码')
        # 判断密码是否一致
        if pwd1==pwd2:
            # 把用户信息存到user表中，并且提示注册成功
            s=sha1()
            s.update(pwd1.encode())
            password = s.hexdigest()
            # 插入到数据库
            ins= 'insert into user values(%s,%s)'
            mysql.execute_sql(ins,L=[username,password])
            print('注册成功')
        else:
            print('密码不一致')
    else:
        print('用户名已存在')
        register()
    # 查询此用户是否已存在
# 登录函数


register()