# yield 关键字

'''
yield 关键字使用在 生成器函数中
        + yield 和 函数中的 return  相似
        + 共同点：执行到这个关键字后 会把结果返回
        + 不同点：
            + return 会把结果返回，并结束当前函数的调用
            + yield 会返回结果，并记住当前代码执行的位置，下一个调用时从上一次离开的位置继续向下执行
'''

# 定义一个普通函数
# def hello():
#     print('hello 1')
#     return 1  # return 在函数中会把结果返回，并且结束当前的函数，后面的代码不再执行
#     print('world 2')
#     return 2

# 使用 yield 定义一个 生成器函数
def hello():
    print('hello 1')
    yield 1  # return 在函数中会把结果返回，并且结束当前的函数，后面的代码不再执行
    print('world 2')
    yield 2

# 调用生成器函数， 返回一个迭代器
result1 = hello()
# next(result1)  # 逐个调用

# 适应 list 类似的函数 去调用生成器返回的迭代器时，会把迭代器的返回结果，作为容器的元素
# r = list(result1)
# print(r)

# for i in result1:
#     print(i)
'''
hello 1
1
world 2
2

首先 调用来生成器函数，返回来一个迭代器
1. 第一次调用迭代器：
    走到当前的生成器函数中，到 yield 1 ，并返回1， 并且记住来当前的执行状态（位置），暂停执行，等待下一次的调用
    
2. 第二次在第一次执行的暂停处，重复第一次并返回第二个 yield 值

3. 重复上述过程直到 yield 被调用完 再次调用则报错
'''

# 练习题： 使用 生成器 改写 斐波那契数列函数


