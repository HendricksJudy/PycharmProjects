# 类成员的操作
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


# 获取类成员属性
print(car.color)
car.color = 'blue'  # 修改类成员属性
print(car.color)

car.name = 'RR'  # 添加类成员属性

del car.name  # 删除类成员属性
'''
对类成员属性的修改，会导致对类成员的所有实例的属性也被修改
对类成员属性的添加，会导致对类成员的所有实例的属性也被添加
'''

# 类操作成员属性 所有操作将会影响所有引用此类的对象
'''
访问：类.成员属性名
修改：类.成员属性名 = 新值
删除：del 类.成员属性名 只能删除类成员属性
添加：类.成员属性名 = 新值
'''

# 类操作成员方法
'''
访问：类.成员方法名(实例)
修改：类.成员方法名(实例) = 新值 
添加：类.成员方法名(实例) = 新值 
删除：del 类.成员方法名(实例) 
'''

# 对象操作将类替换为对象即可，但此时的操作只会影响该对象