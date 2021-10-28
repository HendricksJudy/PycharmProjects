# 写入相关

# cstr1 = 'iloveyou'
# container1 = ['hello', 'world']
# with open('./test/4.txt', 'w', encoding='utf-8') as fp:
#      fp.write(cstr1)  # 只能写入字符串类型数据
#      fp.writelines(container1)  # 可以写入容器类型数据，注意容器中的元素也必须是字符串类


# 读取相关函数
'''
res = fp.read()  # 默认从当前指针开始读取到最后 如果内含数字则读取相应元素个数
     res2 = fp.readline()  # 一次只读取一行 且 一行只会读取一次 可填写元素数
     res3 = fp.readlines()  # 一次读取多行数据，每一行作为一个元素，返回一个列表 可填写元素数，不足一行依照一行计入
'''
# with open('./test/4.txt', 'r', encoding='utf-8') as fp:
#      res = fp.read()  # 默认从当前指针开始读取到最后 如果内含数字则读取相应元素个数


# 设置文件指针
# with open('./test/4.txt', 'a+', encoding='utf-8') as fp:
#      fp.seek(0)  # (0, 2)是设置在文件的末尾  0是设置在文件开头
#      res1 = fp.read()

# 截断文件内容 truncate()
# with open('./test/4.txt', 'r+', encoding='utf-8') as fp:
#      res6 = fp.truncate(5)  # 默认从文件的首个字符进行截断，截断的长度为size个字节数 size如果为0，则从当前位置截断到最后


# 使用数据写入的方式，完成一个注册和登录
