# 元组的切片操作

# 注意，定义元组时，如果只有一个元素，也需要使用 逗号
# tuple2 = 1,  # (1,) <class 'tuple'>
# tuple1 = 1, 2, 3  # (1, 2, 3) <class 'tuple'>

tuple1 = (1, 2, 3, 4, 5)

# 获取元组的长度 len()

# 元组的切片操作 和列表一样 varinat = [开始值:结束值:步进值]
# reslut1 = tuple1[:] 或 tuple1[::] 均是获取全部
# 如果需要倒序输出需要给出 所有三个参数

# 统计一个元素在元组中出现的次数
tuple2 = (1, 2, 3, 4, 5, 5, 4, 3, 2, 1)
# frequency1 = tuple2.count(5)
# print(frequency1)

# 获取一个元素在元组的索引值 tuplename.index(self, x, start, end)  x为查找开始值的下标（不包含）
# marknum1 = tuple2.index()
# print(marknum1)

# 元组的合并, 自我扩增
# addition1 = (1, 2, 3) + ('a', 'b', 'c')
# tuplerepeat1 = (1, 2, 3)*3

# 检测一个元素是否在元组中
# detection1 = 2 in tuple2
# print(detection1)