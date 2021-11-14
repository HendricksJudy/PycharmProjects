# 继承
"""
继承：
    子类继承父类的所有属性和方法，子类可以继承父类的构造方法
    子类继承父类的公有属性和私有属性，子类可以继承父类的公有属性和私有属性
意义：提高代码的重用性，建立新的类与类的关系，方便与其他逻辑的操作

子类继承父类，重新定义了父类的方法，被称之为对父类方法的重写
子类中直接调用父类定义的方法：super().方法名()

子类继承父类后。定义了父类中没有的方法，被称之为对父类方法的重载 （拓展）
"""


# 单继承
# 定义父类
class Cat(object):
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

    # 继承父类后，重新定义父类中的方法
    def walkb(self):
        super(CatBlack, self).walk()

    def focusb(self):
        super(CatBlack, self).focus()


# 通过cat 实例化对象
CatBlack1 = CatBlack("paper", 3, "black", "male")
CatBlack1.walk()
CatBlack1.focusb()


# 多继承
class Father():
    # 父亲的职业薪水
    salary = 7000
    work = "professor"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("He is a father who is a professor work in the CMU.")

    def salary(self):
        print("He's salary is 7000.")

    def academic(self):
        print("He has a lot of creation about machine learning.")


class Mother():
    # 母亲的职业薪水
    salary = 5000
    work = "nurse"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("He is a mother who is a nurse work in the NIH.")

    def salary(self):
        print("She's salary is 5000.")

    def healthcare(self):
        print("She's good at health caring.")


# 定义子类
class Son(Father, Mother):
    # 定义子类的属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("He is a child who is want eat everything")

    def work(self):
        super(Son, self).work()


# 实例化对象
Son1 = Son("Tom", 18)
Son1.eat()
Son1.work()
print(Son1.name)
Son1.academic()
