# 匿名函数 lambda 表达式

'''
语法：

lambda [参数列表] ： 返回值

'''
# 封装一个函数做加法运算
def jia (x, y):
    return x+y

# print(jia(2, 3))

# lambda表达式来封装
res = lambda x, y: x+y
print(res(4, 4))

# lambda 是一个表达式，功能单一，不能用于写太复杂的逻辑
# lambda 是否可以使用分支结构

def func(gender):
    if gender == 'nan':
        return 'man'
    else:
        return ' nv'

# res = func('nan')
# print(res)

# 带有分支结构的lambda 表达式
# lambda 参数列表： 真区间 if 表达式判断 else 假区间
res = lambda gender: 'nan' if gender == 'man' else 'nv'
# 第一个绿色字符表示满足 if 条件的结果  第二个绿色字符表示 if 条件 第三个绿色字符表示else的输出结果
print(res('man'))