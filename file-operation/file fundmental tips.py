# 打开文件
'''
open()
    参数1：文件路径
        路径 URL 统一资源定位符
        相对路径：针对文件   1,txt ，默认为当前目录和 ./1.txt 是一个位置
                          ./1.txt 代表当前目录中的 1.txt
                          ../1.txt 代表当前目录中的上一级目录
        绝对路径：
    参数2： 打开方式
        基础模式： w: write 写入 1. 文件如果不存在，则创建这个文件 2. 如果文件存在，则打开文件并清空文件内容 3. 文件打开后，文件的指针在文件的最前面
                 r：read 读取 1. 文件不存在则报错 2. 文件如果存在，则打开文件
                 x: xor 异或 1. 文件不存在则创建 2. 文件存在则报错（防止覆盖） 3. 文件的指针在最前面
                 a：append 追加 1. 文件不存在则创建 2. 文件如果存在则打开 3. 文件指针在当前文件最后
        拓展模式：
                b bytes 二进制
                + plus 增强模式 （可读可写）
    参数 encoding 可选参数， 设置文件字符集
        如果是一个二进制文件不需要设置字符集
        一般为 encoding = 'utf-8'
'''
# 打开文件 创建文件对象
Myfristfile = open('./1.txt', 'w', encoding='utf-8')
print(Myfristfile, type(Myfristfile))

# 写入内容
Myfristfile.write('hello world')

# 关闭文件
Myfristfile.close()