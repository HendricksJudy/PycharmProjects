# 回调函数
 

> 函数中的参数可以是任意类型，那参数可否是一个函数呢？

>如果在一个函数内要求传递的参数是一个函数作为参数，并且在函数中使用了传递进来的函数，那么这个函数我们可以称为一个回调函数

# 匿名函数 lambda 表达式
> 匿名函数的意思就是说可以不使用def定义，并且这个函数也没有名字
> 在python中可以使用lambda表达式来定义匿名函数
> 注意：lambda表达式仅是一个表达式，不是一个代码块，所以lambda又称一行代码的函数
> lambda表达式存在形参，并且不能访问除了自己的形参之外的任何数据包括全局变量

# 迭代器
> 迭代器是 python 中最具特色的功能之一，是访问集合元素（容器类型）的一种方式
> 迭代器是一个可以记住访问遍历的位置的对象
> 从集合的第一个元素开始访问，直到集合中所有元素被访问完毕
> 迭代器只能从前往后逐个向前遍历，无法后退
>能被 next（）函数调用，并不断返回下一个值的对象称为迭代器（iterator 迭代器对象）
> 迭代器一定是一个可迭代对象，但是可迭代对象不一定是一个迭代器


#### iter()
    功能：把可迭代的对象， 转化为一个迭代器对象
    参数：可迭代的对象  （str, list, tuplr, dict, set, range...）
    返回值：迭代器对象
    注意：迭代器一定是一个可以迭代的对象，但可迭代对象不一定是迭代器

#### next()
> next()函数可以去调用迭代器， 并返回迭代器中的下一个数据

#### 迭代器取值的方案
    1. next（）调用一次获取一次，直到数据被取完
    2. list（）使用list函数直接取出迭代器中的所有数据
    2. for     使用for循环遍历迭代器的数据
#### 迭代器取值的特点，取出来一个少一个，直到都取完，最后再获取即会报错

#### 检测迭代器和可迭代对象的方法
```python

from collections.abc import Iterator, Iterable  # （迭代器） (可迭代对象)

varstr = '123456'
res = iter(varstr)

# type() 函数返回当前数据类型
# isinstance()  检测一个数据是不是一个指定的类型
r1 = isinstance(varstr, Iterable)
r2 = isinstance(varstr, Iterator)
print(r1, r2)
```
