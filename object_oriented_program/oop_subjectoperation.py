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
car.color = 'blue'
print(car.color)