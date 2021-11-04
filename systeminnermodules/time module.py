# 时间模块

import time

# 获取当前系统的时间戳

'''
概念
    时间戳：1970年1月1日0时0分0秒到现在的秒数，目前可以计算到2038年
    时间字符串：格式化后的时间，比如Thu Nov  4 18:07:23 2021
    时间元组：time.struct_time(tm_year=2021, tm_mon=11, tm_mday=4, tm_hour=18, tm_min=10, tm_sec=20, tm_wday=3, tm_yday=308, tm_isdst=0)

'''
timestamp = time.time()
print(timestamp)

# 获取当前系统时间
localtime = time.ctime()
print(localtime)

# 获取当前系统时间  时间元组
localtime_tuple = time.localtime()
print(localtime_tuple)

# 将时间戳转换为时间
localtime_str = time.asctime(localtime_tuple)
print(localtime_str)

# 获取年，月，日，时，分，秒
res = localtime_tuple
print(f'{res.tm_year}年{res.tm_mon}月{res.tm_mday}日{res.tm_hour}时{res.tm_min}分{res.tm_sec}秒 星期{res.tm_wday}')

# 格式化时间
fomration_time = time.strftime('%Y-%m-%d %H:%M:%S', localtime_tuple)
print(fomration_time)

# 时间休眠 给定的秒数内可以暂停当前线程的执行
time.sleep(2)

# 用于统计程序运行时间
# time.perf_counter()

stat_time = time.perf_counter()
for i in range(1000000):
    if 'abc' > 'acd' :
        pass
end_time = time.perf_counter()
print(end_time - stat_time)