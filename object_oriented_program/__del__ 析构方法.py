# __del__ 析构方法
'''
 __del__ 析构方法

__del__ 是一个特殊的方法，当一个对象被删除时，会调用该方法。

__del__ 方法不带参数，但是必须要有返回值。

__del__ 方法的返回值，是用来表示对象的状态，如果返回值是 True，
那么对象的状态就是正常的，如果返回值是 False，那么对象的状态就是异常的。

是销毁触发了析构

对象在哪些情况下会被销毁？
1. 当程序执行完毕，内存中所有资源都会被销毁释放
2. 当对象被引用的次数为0时，对象被销毁
3. 使用 del 删除时，对象被销毁

'''

import time

from my_firstoop import xiaoMi


class WriteLog:
    # 成员属性
    fileurl = './'
    filename = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'  # 日志文件名称

    # 初始化 打开文件
    def __init__(self):
        print('初始化方法被触发了, 完成文件打开')
        self.f = open(self.fileurl + self.filename, 'a+', encoding='utf-8')

    # 日志写入
    def write_log(self, log):
        print(f'把日志：{log} 写入文件中')

    # 析构方法
    def __del__(self):
        print('析构方法被触发了')
        # 在对象被销毁时，关闭在初始化方法中打开的文件对象的状态
        self.f.close()


log_today = WriteLog()
log_today.write_log('今天天气真不错，Github Copilot真好用')

# 使用 del 手动删除
del log_today
'''

未删除时顺序
把日志：今天天气真不错，Github Copilot真好用 写入文件中
....
析构方法被触发了

删除时的顺序
把日志：今天天气真不错，Github Copilot真好用 写入文件中
析构方法被触发了
....

'''

print('....')

# 当对象不再被引用时
WriteLog()
'''
初始化方法被触发了, 完成文件打开
析构方法被触发了
'''

class phone(object):
    def __init__(self, name, price):
        self.name = name
        self.price = price
        print(f'初始化方法被触发：创建{self.name}手机')

    def __del__(self):
        print(f'析构方法被触发：{self.name}手机被销毁了')

# XiaoMi = phone('小米', '1000')
# iphone = phone('iphone', '5000')
# Samsung = phone('三星', '3000')
'''
以上三行的执行顺序是：
初始化方法被触发：创建小米手机
初始化方法被触发：创建iphone手机
初始化方法被触发：创建三星手机
析构方法被触发：小米手机被销毁了
析构方法被触发：iphone手机被销毁了
析构方法被触发：三星手机被销毁了
'''

phone('小米', '1000')
phone('iphone', '5000')
phone('三星', '3000')
'''
以上三行的执行顺序是：
初始化方法被触发：创建小米手机
析构方法被触发：小米手机被销毁了
初始化方法被触发：创建iphone手机
析构方法被触发：iphone手机被销毁了
初始化方法被触发：创建三星手机
析构方法被触发：三星手机被销毁了
'''

