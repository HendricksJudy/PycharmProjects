# 多态 继承版

"""
定义一个接口规范类，其他类继承该类，实现该接口
由于每个对象实现父类的方法或过程都是不同的，最后的结果是不一样的形态
"""

# 定义 USB 接口
class USB():
    """
    这个类是接口规范类。需要子类继承并实现start方法
    start 方法不做任何具体功能但实现。
    """

    # 定义一个规范的 USB 接口方法，但不实现任何功能
    def start(self):
        pass


# 定义鼠标，键盘类，继承 USB 接口
class Mouse(USB):

    def start(self):
        print("鼠标开始工作")


class Keyboard(USB):

    def start(self):
        print("键盘开始工作")


# 实例化对象
mouse_1 = Mouse()
keyboard_1 = Keyboard()

# 启动鼠标，键盘
mouse_1.start()
keyboard_1.start()



