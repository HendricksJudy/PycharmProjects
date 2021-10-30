# 数学模块 Math

import math


# 内置函数 round() 四舍五入
num1 = round(2.25)
# math.ceil() 向上取整
num2 = math.ceil(2.25)
print(num1, num2)  # 2 3


# math.floor() 向下取整
r1 = math.floor(2.55)
print(r1)  # 2

# math.pow() 计算数值的n次方 结果是浮点
r2 = math.pow(2,3)
print(r2)  # 8.0

# math.sqrt() 开平方运算，结算是浮点
r3 = math.sqrt(16)
print(r3)  # 4.0

# mahh.fabs() 计算绝对值, 结算是浮点
r4 = math.fabs(-100)
print(r4)  # 100.0

# math.modf() 把一个数值拆分成整数和小数组成的元组
r5 = math.modf(3.1415)
print(r5)

# math.cppysign(x, y) 把第二个参数的正负拷贝给第一个参数,结果为浮点
r6 = math.copysign(3.15, -99)

# math.fsum() 将一个容器类型中的元进行一个求和运算，结果为浮点 数据必须为numbers

# 阶乘 math.factorial(x) 返回x的阶乘 如果不是自然数则会报错

yzl = math.pi
e = math.e
# ∞ = math.inf



