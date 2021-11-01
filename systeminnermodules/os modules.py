# 系统接口模块 os

import os

# getcwd() 获取当前工作目录，注意获取的不是当前脚本的储存目录
path1 = os.getcwd()
print(path1)

# os.chdir(修改的目录) 修改当前的工作目录（当前运行python解释器的地方）

# os.listdir() 用于获取当前目录下的所有项目，但不包含有.和： 不指定默认为当前工作目录

# os.mkdir(文件夹路径， 权限) 创建文件夹 默认在工作目录 无法递归创建
'''
文件权限仅限Linux
    第2~4个字符代表文件所有人的权限
    第 5~7个字符代表文件所属组的权限
    第 8~11个字符代表其他人的权限
例如：rwx|r-x|r-x
    前三位的rwx代 表文件所有人(u）的权限
    中间三位的r-x 代表文件所属组(g)的权限
    最后三位的r-x 代装其他人(o）的权限
    
    r：Read 读

    w：Write 写

    x：Execute 执行
'''

# os.makedirs(os.path.dirname(os.path.path)) 可以递归创建文件夹

# os.rmdir() 删除 空（从未使用过） 文件夹

# os.removedirs() 递归删除空文件夹

# os.remove('/.DS_Store')  # 删除隐藏文件 即可删除 空文件夹

# os.rename(原有名字， 目的名字) 修改文件或文件夹的名字

# os。system() 执行操作系统中的命令

# os.path 路径模块
'''
os.path.abspath()
将相对路径转化为绝对路径 项目可移植

获取路径中的主体部分
os.path.basename()

获取路径的路径部分 返回路径最后一部分之前的内容
os.path.dirname()


os.path.join(路径1， 路径2) 链接多个路径，组成一个新的路径

os.path.split() 拆分路径，把路径分为路径和主体部分

os.path.splitext() 拆分路径， 可以拆分文件后缀名

获取文件大小 单位：字节
os.path,getsize()

检测是否为一个文件夹或是否存在
os.path.isdir()

# 检测文件是否存在
os.path.isfile()

# 检测路径是否存在 既可检测文件也可检测路径
os.path.exist()

# 检测两个path是否同时指向同一个目标位置 （两个路径必须真实）
os.path.samefile(路径1, 路径2)

# 检测该路径的最后某些时间
os.path.getmtime()  # 修改
os.path.getatime()  # 打开
os.path.getctime()  # 创建




'''



