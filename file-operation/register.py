# 注册功能

# 定义数据变量，存放已经注册的用户信息

userlist = []  # 存放所有用户名
pwdlist = []  # 存放所有的密码

# 读取所有的注册信息 使用 a+ 打开文件，再调整指针位置。防止初始无文件报错
with open('./user.txt', 'a+', encoding='utf-8') as ap:
    ap.seek(0)  # 调整指针至文件头部
    allpwd = ap.readlines()  # 按行读取所有数据
    for i in allpwd:
        r = i.strip()  # 处理换行
        arr = r.split(':') # admin:123 ==> ['admin', '123']
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



register()