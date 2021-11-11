# __del__ 析构方法
'''
 __del__ 析构方法

__del__ 是一个特殊的方法，当一个对象被删除时，会调用该方法。

__del__ 方法不带参数，但是必须要有返回值。

__del__ 方法的返回值，是用来表示对象的状态，如果返回值是 True，
那么对象的状态就是正常的，如果返回值是 False，那么对象的状态就是异常的。

'''

import time


class writelog():
    # 成员属性
    fileurl = './'
    filename = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'  # 日志文件名称

    # 初始化 打开文件
    def __init__(self):
        self.f = open(self.fileurl + self.filename, 'a+', encoding='utf-8')

    # 日志写入
    def write_log(self, log):
        print(f'把日志：{log} 写入文件中')

    # 析构方法
    def __del__(self):
        print('析构方法被触发了')
        # 在对象被销毁时，关闭在初始化方法中打开的文件对象的状态
        self.f.close()

l = writelog()
l.write_log('今天天气真不错，Github Copilot真好用')