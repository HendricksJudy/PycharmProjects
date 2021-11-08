# 对象成员的操作
'''
对象成员：一个对象对象实例化后，在类中定义的属性和方法，可以使用实例化得对象进行操作
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


# 实例化对象
c1 = car()
c2 = car()
print(c1)
print(c2)
'''
一个类可以实例化多个对象，但是每个对象的属性和方法是不同的
<__main__.car object at 0x1029dd0f0>
<__main__.car object at 0x1029dd480>
c1和c2变量都是对象，通过c1和c2变量都可以访问到car类中的属性和方法
'''

# 对象成员的操作
'''
1. 在类的外部，使用对象操作成员
'''
c1.color = 'black'  # 修改对象的属性 修改A对象对其他对象无影响 实际上等于是给此对象创建了一个c1对象自己的color属性
cd1 = c1.color  # 通过对象访问属性
print(cd1)
c1.name = 'A6'  # 给对象添加属性，不对类生效


# 删除属性 只能删除这个对象自己的属性，包括给对象添加的和修改的
# del c1.brand # 删除对象的属性 AttributeError: brand 类属性无法删除
del c1.name
print(c1.name)  # AttributeError: 'car' object has no attribute 'name' 对象属性可以删除
'''
删除一个对象的属性，只是删除了对象的属性，对类的属性没有影响，同时对类赋予对象的属性无法删除
'''
action1 = c1.run()  # 通过对象访问类中方法
print(action1)

# 在类的外部，操作对象的方法
# 访问对象的方法：实际上如果这个对象没有这个方法，会自动调用类中的方法
