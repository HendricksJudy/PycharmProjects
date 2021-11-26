import numpy as np
from PIL import Image
import os

# 顺序读取测试集里面的内容并将其封装成一个函数供神经网络测试使用

root_dir = "./tmp/test"

img_list = []


def gen_list():
    for parent, dirnames, filenames in os.walk(root_dir):  # 三个参数：分别返回1.父目录 2.所有文件夹名字（不含路径） 3.所有文件名字
        for filename in filenames:  # 输出文件信息
            img_list.append(filename.replace(".jpg", ""))
            # print("parent is:" + parent)
            # print("filename is:" + filename)
            # print("the full name of the file is:" + os.path.join(parent, filename))  # 输出文件路径信息
    return img_list


img_list = gen_list()


# 表示读取这个文件夹的第i张文件，按顺序读取
def get_test_captcha_text_and_image(i=None):
    img = img_list[i]
    captcha_image = Image.open(root_dir + "\\" + img + ".jpg")
    captcha_image = np.array(captcha_image)
    return img, captcha_image


# 获取测试集长度
def get_test_sets_length():
    return len(img_list)

# test
# print(img_list)
# print(len(img_list))

