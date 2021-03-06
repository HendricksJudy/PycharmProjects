# 转义字符



# numbers = '123' \
#           '456'
# print(numbers)  # 123456

# \ 转义符， 在字符出现的特定字符有着特定的含义
# \n 换行符
# sentence = '岁月是把杀猪刀, \n但是它对长得丑的人一点办法都没有'  # 一个\n 换一行

# \r 代表光标的位置 （从\r 出现的位置开始作为起始点）
# sentence = '岁月是把杀猪刀, \r但是它对长得丑的人一点办法都没有'  # 但是它对长得丑的人一点办法都没有


# \t 水平制表符
# sentence = '岁月是把杀猪刀, \t但是它对长得丑的人一点办法都没有'
# 岁月是把杀猪刀, 	但是它对长得丑的人一点办法都没有

# \b 退格符
# sentence = '岁月是把杀猪刀, \b但是它对长得丑的人一点办法都没有'  # 岁月是把杀猪刀,但是它对长得丑的人一点办法都没有 一个\b 回退一格

# 双\\  转义的转义是普通字符
# characters = 'abcdef\\nasdfghj'  # 用于在n之前输出一个\
# print(characters)

# 不想让字符串有转义字符进行普通输出，在字符串前加 r
# characters = r'abcdef\nnasdfghj'  # abcdef\nnasdfghj
# print(characters)


'''
字符串相关操作
 字符串 + 操作
 字符串 * 操作
 字符串 [] 切片操作
'''
# 字符串 + 操作
# poetry1 = '君不见黄河之水从天上来， 奔流到海不复回, '
# poetry2 = '君不见，高堂明镜悲白发，朝如青丝暮成雪'
# poetry3 = poetry1 + poetry2
# authorandtitle = '将进酒 ' + '李白'
# print(poetry3)  # 君不见黄河之水从天上来， 奔流到海不复回, 君不见，高堂明镜悲白发，朝如青丝暮成雪
# print(authorandtitle)  # 将进酒 李白

#  字符串 * 操作
# lyrics = '鸡你太美' * 5
# print(lyrics)  # 鸡你太美鸡你太美鸡你太美鸡你太美鸡你太美

# 字符串 [] 切片操作
# 字符串的索引操作，字符串中只能使用[]下标 访问，不能修改
'''

'''
# poetry1 = '君不见,黄河之水从天上来， 奔流到海不复回, '
# print(poetry1[5])
# print(poetry1[-5])  # 写一个值就是获取指定下标的元素
# print(poetry1[2:5])  # 从2下标开始取值，直到下标五之前，左闭右开
# print(poetry1[4:8:2])  # 黄河之水 ==> 黄之
# print(poetry1[::])  # 从头到尾
# print(poetry1[::2])  # 从头到尾, 每隔一个取一个
'''
字符串的切片操作
str[开始值： 结束值：步进值]
开始值：默认为0，结束值默认是最后一个下标， 步进值默认为1
'''


# 字符串的格式化方法
'''
format() 格式化字符串 f
'''
# 1 普通方式
a = '李白'
# poetry1 = '{}乘舟将欲行，忽闻岸上踏歌声'.format(a)
# poetry1 = '{}乘舟将欲行，忽闻岸上{}'.format(a, '踏歌声')

# 2 通过索引穿                               0    1     3
# poetry1 = '{2}乘舟将欲行，忽闻岸上{1}'.format('a', 'b', 'c')

# 3 关键字传参
# poetry1 = '{a}乘舟将欲行，忽闻岸上{b}'.format(a='李白', b='踏歌声')

# 4容器类型数据传参
author1 = '豪放派：{0[0]}，婉约派：{0[1]}，蛋黄派：{0[2]}'.format(['李白', '李清照', '达利园'])

data = {'a': '李白', 'b': '踏歌声'}
poetry1 = '{a}乘舟将欲行，忽闻岸上{b}'.format(**data)
# print(poetry1)

# 新增格式化方法  f 方法
poetry1 = f'{data["a"]}乘舟将欲行，忽闻岸上{data["b"]}'

# 先定小数的位数
# variant1 = '圆周率是多少：{:.2f}'.format(3.1415926)
# print(variant1)

