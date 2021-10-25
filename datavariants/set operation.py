# 集合运算
'''
集合的主要运算
    交集 &    set.intersection()有返回值，设置新集合返回结果  set.intersection_update()没有返回值，改变原有集合
    并集 |    union() 返回并集结果    update() 没有返回值，改变原有集合
    差集 -    set.difference() 返回差集结果    set.diffence_update() 没有返回值，改变原有集合
    对乘差集 ^    set.symmetric_difference()    set.symmetric_difference_update()
    检测 超集 set.issuperset()  子集  set.issubset()
    检测是否相交 set.isdisjoint()
'''

var1 = {'郭富城', '刘德华', '张学友', '黎明', '都敏俊'}
var2 = {'尼古拉斯赵四', '刘能', '小沈阳', '宋小宝', '都敏俊'}

# 求两个集合相交的部分
result1 = var1 & var2

# 求并集
result2 = var1 | var2

# 求差集
result3 = var1 - var2

# 求对称差集
result4 = var1 ^ var2