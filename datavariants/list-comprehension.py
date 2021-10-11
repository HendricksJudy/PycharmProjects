# 列表推导式

# 一，基本的列表推导式使用方式
# 变量 = [ for 变量 in 容器]

# 使用普通方法
# squares = []
# for x in range(10):
#     squares.append(x**2)

# print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 使用 map 函数和 list 完成
# squares = list(map(lambda x: x**2, range(10)))

# 使用列表推导式
squares = [i**2 for i in range(10)]  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares)

# 2.'1234' ==> [2, 4, 6, 8]
doublenum2 = [x*2 for x in range(1, 5)]  # [2, 4, 6, 8]
print(doublenum2)

# 带有判断条件的列表推导式
# 变量 = [变量或变量的处理结果 for i in 容器类型数据 条件表达式]
# 0-9 求所有的偶数
numlist1 = []
for x in range(10):
    numlist1.append(x)

evennum = [x for x in numlist1, if x %2== 0]

