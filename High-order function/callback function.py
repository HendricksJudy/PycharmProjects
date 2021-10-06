# 回调函数

# 定义一个函数，函数中的一个参数要求是另一个函数
#带有回调函数参数的函数
# def func(f):
#     # print(f, type(f))
#     f() # 并且在函数中调用了传递进来的形参函数
#
# 回调函数
# def love():
#     print('123')
#
# func(love)

def func(x, y, f):
    '''
    当前这个函数接收两个数值，并把这两个数值给第三个参数进行调用
    x, y int
    f    function
    :return:
    '''
    # print(f([x, y]))
    print(f(x, y))



# func(1, 2, sum)
func(2, 3, pow)


