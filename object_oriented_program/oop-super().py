# 继承
"""
继承：
    子类继承父类的所有属性和方法，子类可以继承父类的构造方法
    子类继承父类的公有属性和私有属性，子类可以继承父类的公有属性和私有属性
意义：提高代码的重用性，建立新的类与类的关系，方便与其他逻辑的操作
"""


# 定义父类
class Cat():
    def __init__(self, name, age, color, gender):
        self.name = name
        self.age = age
        self.color = color
        self.gender = gender

    def walk(self):
        print("行进")

    def focus(self):
        print('注视')


# 定义子类
class CatBlack(Cat):
    pass

# 通过cat 实例化对象
CatBlack1 = Cat()
