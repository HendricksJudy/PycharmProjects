# 内置高阶函数
# sored（）
'''
原理：把可迭代的数据内含元素，逐个取出，放入key函数中进行处理，依照return的结果进行排序，返回一个新的列表
功能： 排序
参数：
    iterable 可迭代数据 （容器类型数据，range，迭代器）
    reverse 可选，是否反转， 默认为false，不反转， true反转
    key     可选， 函数， 可以是自定义， 也可以是内置函数
返回值：    排序后的结果
'''

arr = [3, 7, 1, -9, 20, 10]
# 默认可以依照从小到大的方式进行排序
# res = sorted(arr)  # [-9, 1, 3, 7, 10, 20]

# 可以依照从大到小的方式进行排序
# res = sorted(arr, reverse=True)  # [20, 10, 7, 3, 1, -9]

# abs 求绝对值
# res = sorted(arr, key=abs)  # [1, 3, 7, -9, 10, 20]
'''
key是排序前对元素的处理规则，再对处理结果进行默认排序
'''
# print(res)

# 使用自定义函数
# def func(num):
#     return num % 2
#
# arr = [3, 2, 4, 6, 5, 7, 9]
# res = sorted(arr, key=func)
# print(res)

# 优化版 对于简单规则使用匿名函数lambda直接写入key中
# arr = [3, 2, 4, 6, 5, 7, 9]
# res = sorted(arr, key=lambda x:x%2)
# print(res)  # [2, 4, 6, 3, 5, 7, 9]


# map()
'''
功能：对传入的可迭代数据中的每一个元素进行处理，返回一个新的迭代器
参数；
    func 函数  自定义函数 ｜ 内置函数
    iterables：可迭代的数据
返回值： 新的迭代器
map(func, *iterables)
'''

# 把一个字符串数字的列表 转为 整型的数字
# varlist = ['1', '2', '3', '4']
# newlist = []
# for i in varlist:
#     newlist.append(int(i))  # append（）用于将括号内的数据追加至指定对象
# print(newlist)

# 使用map函数进行处理
# varlist = ['1', '2', '3', '4']
# res = map(int, varlist)
# print(list(res))

# [1,2,3,4] ==> [1,4,9,16]

# varlist = [1, 2, 3, 4]
# newlist = []
# for i in varlist:
#     res = i ** 2
#     newlist.append(res)
#
# print(newlist)

# 使用map函数
# varlist = [1, 2, 3, 4]
# def func(x):
#     return x ** 2
# res = map[func, varlist]

# reduce() 函数
'''
reduce(func, *iterable)
功能：
    每一次从iterable拿出两个元素，放出到func函数中进行处理，得出一个计算结果，
    然后把这个计算结果和iterable中的第三个元素，放入到func函数中继续运算，得出
    的结果和与之后的第四个元素，加入到func函数中进行处理，以此类推，直到最后一个元素都来参与运算
参数：
    func： 内置函数或自定义函数
    iterable： 可迭代的数据
返回值：最终的运算处理结果
注意： 使用reduce 函数时， 需要导入   from functools import reduce
'''
### （1） [5, 2, 1, 1] ==> 5211

# 一般
# varlist = [5, 2, 1, 1]
# res = ''
# for i in varlist:
#     res += str(i)
# res = int(res)
# print(res)

# reduce法
varlist = [5, 2, 1, 1]


def wpy(k, h):
    return k * 10 + h


from functools import reduce

res = reduce(wpy, varlist)
print(res, type(res))  # 5211 <class 'int'>

# filter()
'''
filter(func, iterable)
功能；
    过滤数据，当前 iterable 中的每个元素拿到func 函数中进行处理
    如果函数返回True 则保留这个数据，返回false则丢弃这个数据
参数：
    func    自定义函数
    iterable：   可迭代数据
返回值： 保留下来的数据组成的 迭代器
'''

# 要求保留所有的偶数，丢弃所有的奇数
varlist = [1, 2, 3, 4, 5, 6, 7, 7, 8, 9]

# yiban
newlist = []
for i in varlist:
    if i % 2 == 0:
        newlist.append(i)
print(newlist)


# filter 定义一个函数， 建立过滤规则
def myfunc(n):
    if n % 2 == 0:
        return True
    else:
        return False

# 调用过滤器并写入过滤规则与存放容器
filter(myfunc, varlist)
