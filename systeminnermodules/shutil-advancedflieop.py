# 高级模块 shutil

import shutil

# copy 复制文件
# shutil.copy(原有路径, 目的路径)

# copy2 和 copy 方式一样， 可以把拷贝文件到指定目录，保留原文件的信息（操作时间和权限等）

# copyfile 拷贝文件的内容 （打开文件，读取内容， 写入到新文件）

# copytree
# shutil.copytree(原有路径, 创建路径)  可以把整个目录结构和文件全部拷贝到指定目录中，但目标路径必须不存在

# rmtree()  删除整个文件夹

# move 移动文件或文件夹到指定目录，也可以用于修改文件夹或文件的名称