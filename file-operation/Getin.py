# 登录功能

# 定义数据变量，存放已经注册的用户信息

# 定义数据变量，存放已经注册的用户信息

userlist = []  # 存放所有用户名
pwdlist = []  # 存放所有的密码
blacklist1 = []  # 存放所有的黑名单用户

# 读取所有的注册信息 使用 a+ 打开文件，再调整指针位置。防止初始无文件报错
with open('./user.txt', 'a+', encoding='utf-8') as ap:
    ap.seek(0)  # 调整指针至文件头部
    allpwd = ap.readlines()  # 按行读取所有数据
    for i in allpwd:
        r = i.strip()  # 处理换行
        arr = r.split(':')  # admin:123 ==> ['admin', '123']
        userlist.append(arr[0])  # 用户名追加到列表
        pwdlist.append(arr[1])  # 密码追加到列表

# 获取黑名单数据
with open('./blacklist1.txt', 'a+', encoding='utf-8') as bl:
    bl.seek(0)
    bln = bl.readlines()
    for i in bln:
        blacklist1.append(i.strip())



# 封装函数，实现登录
    def login():
        # 定义终结变量，终结外循环
        islogin = True
        # 定义变量，检测输入错误次数
        errornum = 3
        # 循环执行
        while islogin:
            # 获取登录的用户名
            username = input('欢迎登录，请输入您的用户名：')
            # 检测当前用户名是否存在
            if username in userlist:
                # 检测是否属于锁定状态（是否在黑名单中）
                if username in blacklist1:
                    print('Your account is already locked. Contact the administrator!')
                else:
                    # 定义循环，执行密码输入
                    while True:
                        # 让用户输入密码
                        pwd = input('请输入您的密码：')
                        # 获取用户名在用户列表的索引
                        inx = userlist.index(username)
                        # 检测用户输入的密码是否正确
                        if pwd == pwdlist[inx]:
                            print('登录成功')
                            # 结束循环
                            islogin = False  # 结束外循环
                            break  # 结束内循环
                        else:
                            # 密码错误则修改次数变量
                            errornum -= 1
                            # 判断当前密码错误次数
                            if errornum <= 0:
                                print('you have been locked! Contact your administrator!')
                                # 锁定账户（把锁定用户拉入黑名单）
                                with open('./blacklist1.txt', 'a+', encoding='utf-8') as op:
                                    op.write(username+'\n')
                                # 结束循环
                                islogin = False  # 结束外循环
                                break
                            else:
                                print(f'密码错误，请重新输入密码。您还有{errornum}次机会')
            else:
                # 用户名不存在
                print('用户名错误请重新输入')


# 检测用户是否属于锁定状态

login()