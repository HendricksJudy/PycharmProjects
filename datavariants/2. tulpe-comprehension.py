# 元组推导式
'''
    列表推导式结果返回了一个列表，元组推导式返回的是一个生成器
    语法：
        列表推导式 ==> [变量运算 for i in 容器] ==> 输出 一个列表
        元组推导式 ==> [变量运算 for i in 容器] ==> 输出 一个生成器

生成器是什么？
    生成器是一个特殊的迭代器，生成器可以自定义也可以使用元组推导式去定义
    生成器是按照某种算法去推算下一个数据或结果，只需要往内存中写入一个生成器，节约内存资源，提升性能
语法：
    （1） 里面是推导式，外面是一个（） 的结果就是一个生成器
    （2） 自定义生成器， 内含yield关键字的函数是生成器
         含有yield关键字的函数，返回的结果是一个迭代器，生成器是一个返回迭代器的函数

如何操作生成器？
    生成器是迭代器的一种，因此可以使用迭代器的操作方法来操作生成器


'''
numlist1 = [1, 2, 3,4, 5, 6]
# resultlist1 = [i**2 for i in numlist1]
# print(resultlist1)

# tuple 返回的generator
resultlist2 = (i**2 for i in numlist1)
print(resultlist2)  # <generator object <genexpr> at 0x104a7fa70>

# 使用next函数去调用
# print(next(resultlist2))

# 使用list 或 tuple 函数 进行操作
# print(list(resultlist2))
# print(tuple(resultlist2))

# 使用 for 进行遍历
for i in resultlist2:
    print(i)