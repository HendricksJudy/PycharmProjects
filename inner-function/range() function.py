# range() 函数

'''
range（）函数的
功能： 能够生成一个指定的数字序列
参数：
    start: 开始的值 （如果是未提供则位0）
    stop；结束值
  [,  step]：可选，步进值  （如果未提供则为1）
返回值：可迭代对象，数字序列
'''

# res = range(10)  # 所有的数据都是对象
# 转为list 列表数据
# print(list(res))

# 通过for 循环 进行遍历
# for i in res:
#     print(i)

# 转为迭代器，使用next函数调用
# res = iter(res)
# print(next(res))

# 只写一个参数就是从0到10之前
# res = range(10)

# 两个参数时，第一个参数时开始值，第二个是结束值（在结束值之前）
# res = range(5,  10)

# 三个参数 第一个是开始值，第二个是结束值，参数三步进值
# res = range(1, 10,2)
res =range(10, 0, -1)
print(list(res))