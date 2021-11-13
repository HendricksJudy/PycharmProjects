# 日志类封装
"""
日志类
     class      MyLog
     功能：
         1.记录日志
         2.记录异常
         3.记录报错
     储存位置：默认在当前目录
     日志文件名：默认为当前日期
     日志格式：年月日时分秒 错误信息：（）

     属性：存储信息供成员方法调用
        储存地址：fileURL
        日志文件名：filename
        日志对象：logobj


     方法：完成一个功能的过程
        __init__ ==> 初始化方法，并打开文件
        writeLog() ==> 接收日志信息，并写入到日志文件中
        __del__ ==> 析构方法，在对象被销毁时，关闭打开的文件
"""
import time


class MyLog():
    # 属性
    fileURL = './'
    filename = time.strftime('%Y-%m-%d', time.localtime(time.time())) + '.log'
    logobj = None

    # 方法
    def __init__(self):
        # 初始化方法，并打开文件
        self.logobj = open(self.fileURL + self.filename, 'a+', encoding='utf-8')

    def writelog(self, msg):
        # 准备写入信息
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        logmsg = now + ' ' + msg + '\n'
        # 显示准备写入的信息
        print(logmsg)
        # 写入信息
        self.logobj.write(logmsg)

    def __del__(self):
        # 关闭打开的文件
        self.logobj.close()


todayrecord = MyLog()
todayrecord.writelog('今天也是用Copilot的一天！')
