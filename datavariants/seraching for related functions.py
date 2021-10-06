# 字符串查找与操作相关函数

sentence = 'iloveyoutosimidaandilikeyou'

# 检测一个字符串是否存在与一个字符串中
# judgment = 'love' in sentence

# 获取字符串的长度 len()
# judgment = len(sentence)

# str.find(sub[, start[, end])  # 获取指定字符在字符串第一个字符且第一次出现的索引位置，未找到则返回 -1  从左向右 从前往后
# position1 = sentence.find('i')
# print(position1)
# str.rfind()  # 从右向左找

# str.index() 和 find方法一样， 只不过如果没有找到则报错  # ValueError: substring not found
# position1 = sentence.index('yous')
# position2 = sentence.rindex('yous')  # 从右向左找


# str.count(sub[, start[, end]])  # 统计一个字符在字符串中出现的次数
frequency = sentence.count('i')
print(frequency)

