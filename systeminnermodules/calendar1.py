# 日历

import calendar
import time

# 返回指定年份和月份的数据，月份的第一天是星期几和月份中的天数
# calendar.month(year, month)
print(calendar.month(2021, 11))

# 万年历
localtime_tuple = time.localtime()  # 获取当前系统时间
year = localtime_tuple.tm_year  # 获取当前系统时间的年份
print(calendar.calendar(year,w=2,l=1,c=6))
