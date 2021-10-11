# 深copy 与 浅copy

# 浅拷贝 只能拷贝当前列表， 不能拷贝列表中的多维列表元素

# varlist = [1, 2, 3]

# 简单的拷贝 就可以把列表复制一份
# newlist = varlist.copy()
# 对新拷贝的列表操作，也是独立的
# del newlist[1]
# print(varlist, id(varlist))
# print(newlist, id(newlist))
'''
[1, 2, 3] 4378945088
[1, 2, 3] 4379524992  id 不同

[1, 2, 3] 4372718592
[1, 3] 4372954688
'''
# 多维列表
varlist2 = [1, 2, 3, ['a', 'b', 'c']]

# 使用 copy 函数 拷贝一个多维列表
newlist2 = varlist2.copy()

'''
print(newlist2, id(newlist2))
print(varlist2, id(varlist2))
[[1, 2, 3], ['a', 'b', 'c']] 4314657984
[[1, 2, 3], ['a', 'b', 'c']] 4314657920
'''
# 如果是一个被拷贝的列表， 对它的多维列表元素进行操作时， 会导致原列表的多维列表也发生了变化
del newlist2[3][1]
print(newlist2[3], id(newlist2[3]))
print(varlist2[3], id(varlist2[3]))
'''
通过 id 检测， 发现列表中的多维列表是同一个元素（对象）

print(newlist2[3], id(newlist2[3]))
print(varlist2[3], id(varlist2[3]))
['a', 'c'] 4370097728
['a', 'c'] 4370097728                       # id 一致

[1, 2, 3, ['a', 'c']] 4345878848
[1, 2, 3, ['a', 'c']] 4345855872
'''

# 深copy 将多维列表全部拷贝
# 方法： 使用 copy 模块中 深拷贝方法 deepcopy
import copy
varlist2 = [1, 2, 3, ['a', 'b', 'c']]
newlist = copy.deepcopy(varlist2)
del newlist[3][1]
'''
[1, 2, 3, ['a', 'b', 'c']]
[1, 2, 3, ['a', 'c']]

print(newlist2[3], id(newlist2[3]))
print(varlist2[3], id(varlist2[3]))
['a', 'c'] 4339361344
['a', 'b', 'c'] 4340167552
'''

print(varlist2)
print(newlist2)
