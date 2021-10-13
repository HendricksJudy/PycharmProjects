# 1. {'user' : 'admin' , 'age' : 20, 'phonenumber' : '13356924857'} 将字典中的键值对转换成 a = b 的数据格式化并在之间加入&

# dictionary1 = {'user': 'admin', 'age': 20, 'phonenumber': '13356924857'}
# answer1 = [i+'='+str(dictionary1[i]) for i in dictionary1]
# # for key, value in dictionary1.items():
# print(answer1)
# print('&'.join(answer1))
'''
['user=admin', 'age=20', 'phonenumber=13356924857']
user=admin&age=20&phonenumber=13356924857
'''

# 2. 把列表中所有字符全部转为小写
# # ['AAAAA', 'bbBb', 'CCCcc']
# prototypes = ['AAAAA', 'bbBb', 'CCCcc']
# concequences = [i.lower() for i in prototypes]
# print(concequences)

# 3. x 是 1-6 之间的偶数，y是 1-6 之间的奇数， 把 x, y组成一个元组，放到列表中
# 普通方法
# combo = []
# for x in range(7):
#     for y in range(7):
#         if x % 2 == 0 and y % 2 == 1:
#             combo.append((x, y))
#
# print(combo)  # [(0, 1), (0, 3), (0, 5), (2, 1), (2, 3), (2, 5), (4, 1), (4, 3), (4, 5), (6, 1), (6, 3), (6, 5)]

# 列表推导式
# combo = [(x, y) for x in range(7) for y in range(7) if x % 2== 0 and y % 2 == 1]
# print(combo)

# 使用列表推导式 完成 99乘法表
# multiplegroups = [f'{x}x{y}={x*y}' for x in range(1, 10) for y in range(1, x+1)]
# print(multiplegroups)

# 5. 求M, N中矩阵和元素的乘积
'''
M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

N = [
        [2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]
]

实现乘积的结果
（1） ==> [2, 4, 6, 12, 15, 18, 28, 32, 36]
 (2 ==> [[2, 4, 6], [12, 15, 18], [28, 32, 36]]
'''

M = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
]

N = [
        [2, 2, 2],
        [3, 3, 3],
        [4, 4, 4]
]

matrix3 = [M[x][y]*N[x][y] for x in range(3) for y in range(3)]
print(matrix3)
