# self

class Person:
    def __init__(self, name, age, talents, hobbies):
        self.name = name
        self.age = age
        self.talents = talents
        self.hobbies = hobbies

    def my_name(self):
        print("Hello my name is " + self.name)

    def my_talents(self):
        print("I have a lot of talents such as" + self.talents)

    def my_age(self):
        print("I am " + str(self.age) + " years old")

    def my_hobbies(self):
        print("I like to do " + self.hobbies)

    '''
    Warning:Method must have a first parameter, usually called 'self'
    if you don't pass 'self' as a parameter, you can't access the instance variables
    '''
    def test_func():
        print("This is a test function which doesn't have self")


# 实例化对象
person1 = Person("John", 22, "Coding", "Reading")
person2 = Person("Mary", 21, "Dancing", "Swimming")

# 调用对象的方法
person1.my_name()

'''
An object which doesn't have 'self' could be used in a method, but it is not recommended
It can be accessed through the class name
'''
Person.test_func()  # using class name to call a method 调用静态方法


