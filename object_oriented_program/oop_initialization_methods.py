# 初始化方法
'''
__init__() 说明：当类实例化对象后，自动触发的一个方法，用于初始化对象的属性
不需要手动调用，会在某种情况下自动执行
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return '{} is {} years old.'.format(self.name, self.age)


Judy = Person('Judy', 18)
print(Judy)
