# 序列化 json 一种数据交换格式
'''
JSON 是js中一个对象的表示方法
与Python中字典的定义规则和语法都很类似
是一种通用的数据交换，传输，定义的数据格式
容器类型才能转换为JSON
dump = json.(写入对象，文件对象）
load = json.(文件对象）
'''

import json

vardict1 = {'name': 'damin', 'age': '20', 'sex': 'male'}

# 序列化
res1 = json.dumps(vardict1)

print(res1, type(res1))

# load 反序列化
res2 = json.loads(res1)
print(res2, type(res2))
