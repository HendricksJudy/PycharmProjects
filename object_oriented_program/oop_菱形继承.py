# 菱形继承

# 祖先类
class Animal:
    num = 444


    def work(self) :
        print('His work is try to survive')

    def run(self):
        print('running...')


class Father(Animal):
    num = 333
    # 父亲的职业薪水
    salary = 7000
    work = "professor"

    def work(self):
        super().work()
        print(super().num)
        print("He is a father who is a professor work in the CMU.")

    def salary(self):
        print(super().num)
        print("He's salary is 7000.")

    def academic(self):
        print("He has a lot of creation about machine learning.")


class Mother(Animal):
    num = 222
    # 母亲的职业薪水
    salary = 5000
    work = "nurse"

    def work(self):
        super().work()
        print("He is a mother who is a nurse work in the NIH.")

    def salary(self):
        print(super().num)
        print("She's salary is 5000.")

    def healthcare(self):
        print("She's good at health caring.")


# 定义子类
class Son(Father, Mother):
    num = 111

    # 定义子类的属性
    def eat(self):
        print(super().num)
        print("He is a child who is want eat everything")

    def work(self):
        super().work()
        print("He is a child who is a doctor work in the Harvard.")


# 实例化
son = Son()
son.eat()
son.work()

# mro() 获取MRO列表，就是类的继承关系
print(Son.mro())
"""
[<class '__main__.Son'>, <class '__main__.Father'>, <class '__main__.Mother'>,
<class '__main__.Animal'>, <class 'object'>]
"""
"""
super()
    使用super去调用父类的方法，实际上是在用super调用MRO列表中的上一级的方法，属性同理
super()本身去调用父级方法时，传递的self对象，就是从这个方法中的那个self对象自己
"""
