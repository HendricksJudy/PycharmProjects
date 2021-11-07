# 定义一个类
'''
类名的书写规范围
    驼峰命名法：类名首字母大写，其他字母小写，第二个字母大写
    大驼峰：MyCar XiaoMi
    小驼峰：myCar xiaoMi

类 = 特征（描述）在编程中称之为变量 + 功能（能力）在编程中称之为函数

'''

class car():
    # 属性 ==> 特征 ==> 变量
    color = 'red'
    brand = 'XiaoMi'

    # 功能 ==> 能力 ==> 函数
    def run(self):
        print('the car could take the cargo')

    def stop(self):
        print('the car could stop')

    def turn(self):
        print('the car could turn to everywhere')

# 如何去使用这个类
# 通过类实例化一个对象
xiaoMi = car()
print(xiaoMi, type(xiaoMi))

# 调用对象的方法
xiaoMi.run()

# 获取对象属性
print(xiaoMi.color)

