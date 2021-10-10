# 列表相关
memberlist1 = ['刘德华', '张学友', '张国荣', '张学友',  '郭富城', '黎明', '小沈阳', '刘能', '宋小宝', '赵四']

# len()     检测当前列表长度，列表中元素的个数
# length1 = len(memberlist1)

# count()   检测当前列表中指定元素元素出现的次数
# frequency1 = memberlist1.count('张学友')
# print(frequency1)

# append() 向列表的尾部追加新的元素，返回值为None
# revalue = memberlist1.append('周杰伦')  # None
# print(revalue)

# insert(self, index, object) 向列表中指定的索引位置添加新的元素
# memberlist1.insert(1, 'aa')
# print(memberlist1)

# pop() 可以将指定索引位置上的元素做 出栈 操作 返回出栈元素
# outvariant = memberlist1.pop()  # 默认会把列表中的最后一个元素 出栈
# outvariant2 = memberlist1.pop(5)
# print(outvariant2)

# remove()  可以指定列表中第一个被查找到元素 进行 删除 无返回值 未找到则报错
numlist1 = [1, 2, 3, 4, 11, 22, 33, 44, 1, 2, 3, 4]
# outvaint3 = numlist1.remove(1)
# print(numlist1)

# index() 可以查找指定元素在列表中第一次出现的索引位置
res = numlist1. index(1, 5, 10)  # 可以在指定索引范围内查找元素的索引位置
print(res)

# extend()  接收一个容器类型数据， 把容器中的元素追加到原列表中
# numlist1.extend('123')
# print(res)
# print(numlist1)

# s.clear() 清空列表内容
# res = numlist1.clear()
# print(res)
# print(numlist1)

# resverse() 列表翻转
# res = numlist1.reverse()
# print(res)
# print(numlist1)

# sort()  对列表进行排序
# res = numlist1.sort()  # 默认对元素进行从小到大的排序
# res = numlist1.sort(reverse=True)  # 对元素进行从大到小的排序
# res = numlist1.sort(key=abs)  # 可以传递一个函数，按照函数处理结果进行从小到大排序

# copy()  拷贝，复制当前的列表
# 在单维列表中对副本进行操作，对原品无影响
# res = numlist1.copy()
# print(res)
# print(numlist1)

# 定义多维列表
numlist2 = ['a', 'b', 'c', [11, 22, 33]]
res = numlist2.copy()

# 对 copy 的子列表进行操作
del res[3][1]  # 对多维列表进行操作，副本与原品均会发生改变
print(res)
print(numlist2)
'''
['a', 'b', 'c', [11, 33]]
['a', 'b', 'c', [11, 33]]
'''
