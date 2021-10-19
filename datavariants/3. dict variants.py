var1 = {'a': 1, 'b': 2, 'c': 3}
var2 = {1: 'a', 2: 'b', 3:'c'}


# 获取元素
result = var1['a']  # 通过写入

# 修改元素
result2 = var1['a'] = 111

# 删除元素
del var1['a']

# 添加元素
var1['aa'] = 'AA'

# 如果字典中的key重复了，会被覆盖

# 成员检测 只能检测key 无法检测value
result3 = 'aa' in var1  # True 即为存在 Flase 即为不存在

# 获取当前字典的长度，只能检测当前有多少键值对
length1 = len(var1)

# 获取当前字典的所有 key
allkeys = var1.keys()  # dict_keys(['b', 'c', 'aa'])

# 获取所有的value
allvalues = var1.values()  # dict_values([2, 3, 'AA'])

# 获取所有键值对
allkvs = var1.items()  # dict_items([('b', 2), ('c', 3), ('aa', 'AA')])

# 对字典进行遍历
# for i in var1:
#     print(i)  # 获取key
#     print(var1[i])  # 通过dict(key)，获取value
for k, v in var1.items():
    print(k)  # key
    print(v)  # value