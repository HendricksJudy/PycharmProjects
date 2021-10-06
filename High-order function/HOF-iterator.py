# 迭代器

# range(10)  # 返回一个可迭代对象 0--9 左闭右开
# range(10, 3, -1) 表示10--4

# arr = ['a', 2, 3, 4, 5]
# for i in arr:
#     print(i)


'''
iter()
    功能：把可迭代的对象， 转化为一个迭代器对象
    参数：可迭代的对象  （str, list, tuplr, dict, set, range...）
    返回值：迭代器对象
    注意：迭代器一定是一个可以迭代的对象，但可迭代对象不一定是迭代器
'''
# 定义一个列表是一个可迭代的对象
arr = ['zhaosi', 'liuneng', 'xiaoshengyang', 'chaomian']
# print(arr)
# for i in arr:
#     print(i)
# 可以使用for循环来遍历数据

# 可以把可迭代对象转为迭代器使用
res = iter(arr)
# print(res, type(res))  # <list_iterator object at 0x10b5dde50> <class 'list_iterator'>

# 使用next()函数去调用迭代器对象
r = next(res)
print(r)  # 上述操作可持续至元素个数次，每一次都取一个数据且取出后该数据从组内删除，超过即停止迭代 stopiteration


'''
迭代器取值的特点，取出来一个少一个，直到都取完，最后再获取即会报错
迭代器取值的方案
    1. next（）调用一次获取一次，直到数据被取完
    2. list（）使用list函数直接取出迭代器中的所有数据
    2. for     使用for循环遍历迭代器的数据

'''

# 检测迭代器和可迭代对象的方法

from collections.abc import Iterator, Iterable  # （迭代器） (可迭代对象)

varstr = '123456'
res = iter(varstr)

# type() 函数返回当前数据类型
# isinstance()  检测一个数据是不是一个指定的类型
r1 = isinstance(varstr, Iterable)
r2 = isinstance(varstr, Iterator)
print(r1, r2)
