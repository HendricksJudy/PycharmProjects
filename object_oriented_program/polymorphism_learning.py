# 多态
# 对于同一个方法，由于调用对象不同（或者传入对象不同），最终实现了不同的结果

# 定义电脑类
class Computer:
    # 在电脑中定义一个 USB 接口
    def usb(self, obj):
        obj.start()

    # 在电脑中定义一个 HDMI 接口
    def hdmi(self, obj):
        obj.start()


# 定义鼠标类
class Mouse():
    def start(self):
        print('鼠标开始工作')


# 定义键盘类
class Keyboard():
    def start(self):
        print('键盘开始工作')


# 定义显示器类
class Monitor():
    def start(self):
        print('显示器开始工作')


# 定义一个电脑对象，输入对象和输出对象
computer_1 = Computer()
mouse_1 = Mouse()
keyboard_1 = Keyboard()
monitor_1 = Monitor()

# 把鼠标与键盘通过USB连接电脑
computer_1.usb(mouse_1)
computer_1.usb(keyboard_1)


# 把显示器通过HDMI连接电脑
computer_1.hdmi(monitor_1)