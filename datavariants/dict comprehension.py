# 字典推导式

# 把字典中键值对进行交换  {'a': 1, 'b': 2, 'c': 3}

dict1 = {'a': 1, 'b': 2, 'c': 3}

# 普通方法实现 字典中的键值交换
# newdict1 = {}
# for k,v in dict1.items():
#     newdict1[v] = k


# newdict1 = {v: k for k, v in dict1.items()}  # {1: 'a', 2: 'b', 3: 'c'} <class 'dict'>
# newdict1 = {v for k, v in dict1.items()}  # {1, 2, 3} <class 'set'> 返回的结果是一个集合， 集合推导式
# print(newdict1, type(newdict1))

