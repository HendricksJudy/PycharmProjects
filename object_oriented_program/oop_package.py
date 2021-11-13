# 封装
"""
封装级别：
        1.public：公开的，对外可见
        2.protected：受保护的，只有本类和子类可以访问
        3.private：私有的，只有本类可以访问
封装原理：私有化 ==> _objectName__attrName 通过这样的名字可以实现对私有化的访问
"""


class Dog:
    # 定义类属性
    name = "dog"
    _age = "年龄"  # 受保护的属性
    color = "颜色"
    __weight = "体重"  # 私有属性

    def __init__(self, name, age, color, weight):
        self.name = name
        self._age = age
        self.color = color
        self.__weight = weight

    def eat(self):
        print("%s is eating" % self.name)

    def drink(self):
        print("%s is drinking" % self.name)

    def break_limit(self):
        """
        如果有类中有public访问了限制方法与属性，那么限制将会无效，依旧可以被引用。
        :return:
        """
        print(self.__weight)
        self.__work()
        self.__private_method()

    def sleep(self):
        print("%s is sleeping" % self.name)

    def _run(self):
        print("%s is running" % self.name)  # 受保护的方法可以在外部操作

    def __work(self):
        print("%s is working" % self.name)  # 私有方法只能在本类中操作

    def __private_method(self):
        print("%s is private method" % self.name)


Dog1 = Dog("wangcai", 2, "white", 10)
print(Dog1.name)

Dog1.break_limit()  # 内部可以操作任意成员