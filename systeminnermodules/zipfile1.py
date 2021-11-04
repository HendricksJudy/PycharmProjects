# 压缩模块

import zipfile,os,shutil
'''
zipfile.zipfile(路径包名, 模式, 压缩或打包)
'''
# with zipfile.ZipFile('spam.zip', 'w') as myzip:
#     myzip.write('被压缩文件名')

# 解压文件
# with zipfile.ZipFile('spam.zip', 'r') as myzip:
#     myzip.extractall(path=None, members=None, pwd=None)


# 如何压缩当前文件夹的所有文件
# with zipfile.ZipFile('spam.zip', 'w', zipfile.ZIP_DEFLATED) as myzip:
#     arr = os.listdir('所需目录')  # 获取当前目录中所有项
#     for i in arr:
#         myzip.write(i)

#  使用shutil模块进行归档压缩
# 参数1 创建的压缩文件名称     参数2 指定的压缩格式 zip tar     参数3 要压缩文件或文件夹路径
shutil.make_archive('a', 'tar', './')
