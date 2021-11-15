# 合并登录注册

# 定义数据变量，存放已经注册的用户信息

userlist = []  # 存放所有用户名
pwdlist = []  # 存放所有的密码
blacklist1 = []  # 存放所有的黑名单用户

# 读取所有数据
def readallusers():
# 读取所有的注册信息 使用 a+ 打开文件，再调整指针位置。防止初始无文件报错
    with open('./user.txt', 'a+', encoding='utf-8') as ap:
        ap.seek(0)  # 调整指针至文件头部
        allpwd = ap.readlines()  # 按行读取所有数据
        for i in allpwd:
            r = i.strip()  # 处理换行
            arr = r.split(':')  # admin:123 ==> ['admin', '123']
            userlist.append(arr[0])  # 用户名追加到列表
            pwdlist.append(arr[1])  # 密码追加到列表

# 封装函数 完成注册功能
def register():
    # 定义一个变量用户控制外循环
    sdo = True
    # 循环执行用户名输入操作
    while sdo:
        # 用户输入用户名
        username = input('欢迎您的到来，请输入用户名：')

        # 检测用户名是否存在
        if username in userlist:
            print('用户名重复，请换一个再试！')
        else:
            # 用户名是否重复
            while True:
                # 输入密码
                pwd = input('请输入密码：')
                # 检测密码长度不得低于五位
                if len(pwd) >= 5:
                    # 重复输入密码
                    repwd = input('请再次输入密码确认：')
                    # 检测密码和确认密码是否一致
                    if pwd == repwd and len(username) >= 3:
                        # 密码和用户名都正确，就可写入文件
                        # 打开文件
                        with open('./user.txt', 'a+', encoding='utf-8') as fp:
                            fp.write(f'{username}:{pwd}\n')
                        print(f'注册成功：用户名：{username}')
                        # 结束循环
                        #结束外循环
                        sdo = False
                        # 结束内循环
                        break
                    else:
                        print('两次密码不一致，请重新输入')
                else:
                    print('密码强度不够！请输入长度大于3的密码')


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


# 判断当前的脚本是否作为一个主进程在执行
if __name__ == '__main__':
    # 以上代码只会在python解释器中直接运行才会执行
    # 如果当前的脚本被作为一个模块被其他文件导入使用时，那么这个地方的代码就不会执行
    # 因此这地方的代码适合写当前脚本中的一些测试，这样不会影响其他脚本

    # 调用初始化方法，加载数据
    readallusers()
    # 终结引导程序变量
    successfully1 = True

    while successfully1:
        welcomeMessage = '''
        *********************************
        ** 登录(0)    注册(1)   退出(esc)**
        *********************************
        '''
        print(welcomeMessage)

        # 让用户选择对应操作
        choicenum = input('请输入对应括号内的字符，体验功能：')
        if choicenum == '0':
            login()
            successfully1 = False
        elif choicenum == '1':
            register()
            successfully1 = False
        elif choicenum =='esc':
            successfully1 = False
        else:
            print('请输入0或1以进行下一步操作，或输入 esc 退出程序！')