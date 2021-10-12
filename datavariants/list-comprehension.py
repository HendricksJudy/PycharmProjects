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
    if x%2 == 0:
        numlist1.append(x)

print(numlist1)

# numlist1 = [x for x in range(10) if i % 2 == 0] 在3.7版本之前可用 新版需使用正规 for 语句进行推导式书写

# 带有条件判断的多循环的推导式
# [1, 2, 3] , [3, 1 ,4] ==> 把两个列表中的元素 两两组合， 要求组合的元素不能重复
a = [1, 2, 3]
b = [3, 1 ,4]
combo = []
for x in a:
    for y in b:
        if x != y:
            combo.append((x, y))  # [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]

print(combo)

# 对于嵌套循环的列表推导式
'''
# Consider the following example of a 3x4 matrix implemented as a list of 3 lists of length 4
matrix = [     
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
'''

matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
 ]
# 常规
# matrix2 = []
# for i in range(4):
#     res = []
#     for row in matrix1:
#          res.append(row[i])
#     matrix2.append(res)
#
# print(matrix2)

matrix2 = [[row[i] for row in matrix1] for i in range(4)]
print(matrix2)





