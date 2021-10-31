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

