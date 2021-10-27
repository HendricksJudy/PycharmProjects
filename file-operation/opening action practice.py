# 文件操作的步骤和写入方式

# 打开文件
# Myfristfile = open('./1.txt', 'a', encoding="utf-8")
# # 写入文件
# Myfristfile.write('\n你好')
# # 关闭文件
# Myfristfile.close()

# 读取操作
# Myfristfile = open('./1.txt', 'r', encoding="utf-8")
# result1 = Myfristfile.read()
# Myfristfile.close()
# print(result1)

#
'''
with open(文件路径， 打开模式） as 变量：
    变量.操作()
打开关闭操作一体化
r+ 可读可写
w+ 打开先清空 可读可写
a+ 可读 追加写入
x+ 异或 用于不存在文件创建并写入
'''
with open('./1.txt', 'r+', encoding='utf-8') as Myfristfile:
    Myfristfile.write('BB')

    # 设置指针的位置
    Myfristfile.seek(0)  # 设置当前指针的位置 seek(0，最开始的位置
    res = Myfristfile.read()
    print(res)