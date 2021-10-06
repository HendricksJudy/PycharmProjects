# 英文字符与字符检测相关函数

sentence = 'i love you'

'''
大小写转换相关
'''
# str.capitalize() 返回原字符串的副本，其第一个字符大写，其余小写
# res = sentence.capitalize()
# print(res)

# str.title()  返回原字符的副本， 把字符串中的每个单词的首字母大写
# res = sentence.title()  # I Love You

# str.upper()  # 字符串中的英文字符全转为 大写
# res = sentence.upper()

 # str.lower()  # 字符串中的英文字符全转为 小写
# res = sentence.lower()

# 返回原字符串的副本， 其中大小写字符转换为小写，反之亦然
# res = sentence.swapcase()

# 字符检测方法
# 当前字符串中的英文字符是否全部由大写字符组成
# judgment = sentence.isupper()  # function's structure variant2 = variant1(examined).is'examining condition'()

# str.isalnum()
# judgment = sentence.isalnum()  # 检测字符串是否由字符组成（中文，字母，数字）组成

# str.isalpha
# judgment = sentence.isalpha()  # 检测是否由中英文字符组成（不包含数字）

# str.isdigit()
# judgment = sentence.isdigit()  # 检测当前字符串是否为纯数字

# str.isspace()  # 检测是否有空格

# 检测一个字符串是否由指定字符开头的, 也可以指定开始和结束的位置
# judgment = sentence.startwith('examined content', 'position number')

# 检测一个字符串是否由指定的字符结尾的，也可以指定开始和结束位置
# judgment = sentence.endwith('examined content', 'start number', 'end number')



# print(judgment)

