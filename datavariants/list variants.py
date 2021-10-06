# 列表定义与基本操作

numlist1 = [1, 2, 3, 4]
numlist2 = ['a', 'b', 'c', 'd']

# 列表的拼接
# result1 = numlist1 + numlist2  # [1, 2, 3, 4, 'a', 'b', 'c', 'd'] 相加组合为一个新的列表
# print(result1)

# 列表元素的重复
# result2 = numlist1*3  # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# result4 = numlist1 * ['aa', 'bb']TypeError: can't multiply sequence by non-int of type 'list'
# print(result2)

# 检测元素是否存在于列表之中
# result3 = 'a' in numlist2  # True
# print(result3)

# 列表的索引操作
'''
 0    1    2    3
'a', 'b', 'c', 'd'
-4   -3   -2   -1
'''
# 通过下获取指定的元素
# print(numlist2[2])  # c

# 通过下标修改元素
# numlist2[1] ='fdijhasfoj'
# print(numlist2[1])

# 不能通过下标添加元素， 因为下标数等于元素数-1

# 向列表元素中追加元素
# numlist1.append('ff')  # [1, 2, 3, 4, 'ff']
# numlist1.append(['gg', 'ff', 'pp'])  # [1, 2, 3, 4, ['gg', 'ff', 'pp']] 可添加列表，但是不可以同时添加多个元素

# 列表元素的删除
# del numlist1[1]  # [1, 3, 4]
# print(numlist1)
# numlist1.pop()  # [1, 2, 3]
# print(numlist1)

# 获取列表中的长度 len()
# lengthen1 = len(numlist1)  # 4
# print(lengthen1)
