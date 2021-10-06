# 字符串操作函数
sentence = 'user_admin_id_123'
userinfo = 'uid=123&type=ab&kw=hh'
# str.split()  按照指定的字符进行分隔，把一个字符串分隔成一个列表
# operation1 = sentence.split('_')  # ['user', 'admin', 'id', '123']
# print(operation1.pop())  # .pop获取最后一个


# operation2 = userinfo.split('&')
# print(operation2)  # ['uid=123', 'type=ab', 'kw=hh']
# for i in operation2:
#     res = i.split('=')
#     print(res.pop())

# arr = ['user', 'admin', 'id', '123']
# str.join(iterable) 按照指定字符，把容器类型中的数据链接为一个字符串
# res = '@'.join(arr)  # user@admin@id@123


# 可以指定分隔的次数
# str.rsplit(sep=None, maxsplit=-1)
# res2 = sentence.rsplit('_', 2)  # ['user_admin', 'id', '123'] 倒序
# print(res2)

# pretitle1 = '   这是一个是文章的标题    '
# str.strip()  # 可以去除字符串左右两侧的指定字符
# title1 = pretitle1.strip(' ')
# print(title1, len(title1))  # 这是一个是文章的标题 10
# print(pre-title1, len(pretitle1))  #    这是一个是文章的标题     17

# str.lstrip()  去除字符串左侧的指定字符    str.rstrip()    去除字符串左侧的指定字符

# str.replace(old, new[, count])
# sentence = 'iloveyoutosimidailoveyou'
# # res = sentence.replace('love', 'like')
# res = sentence.replace('love', 'like', 1)  # 只替换一次
# print(res)

#
word1 = 'love'

# res = word1.center(10)
# res = word1.center(10,'*')  # ***love***

res = sentence.ljust(10, '*')


print(res)

