# 字典相关函数

# len() 获取键值对个数

# dict.keys()   dict.values()   dict.item()

dict1 = {'a': 1, 'b': 2, 'c': 3}

# iter(d) 返回以字典的键为元素的迭代器
# result1 = iter(dict1)

# dict.pop() 从当前字典中弹出键值对    删除  如果弹出对象不存在则报错
# outkv1 = dict1.pop('a')

# dict.popitem()    LIFO: Last in ,First out 后进先出
outkv2 = dict1.popitem()  # 把最后加入到字典的键值对删除并返回一个元组

# dict.get() 使用key获取字典中不存在的元素，会报错。  因此使用一个get 存在则返回 不存在默认返回None

# 字典内的更新 dict.update() 可以更新现有的 也可以新增
# dict1.udpate({'c': 33, 'd': 44})
# dict1.udpate(a=11, b=22)

# dict.setdefault(key [, default])   存在key 则返回值  不存在则插入值为default的key， 并返回default default默认为None
outv1 = dict1.setdedault('a')

# clear() 清空


