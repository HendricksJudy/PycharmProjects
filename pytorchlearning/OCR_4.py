# _captchaTest为项目名 gen_captcha为该项目名下的python文件
from _captchaTest.gen_captcha import number
from _captchaTest.gen_captcha import alphabet
from _captchaTest.gen_captcha import ALPHABET
from _captchaTest.gen_captcha import gen_captcha_text_and_image_new
import numpy as np
import tensorflow as tf

text, image = gen_captcha_text_and_image_new()
print("验证码图像channel:", image.shape)  # (60, 160, 3)
# 图像大小
IMAGE_HEIGHT = 60
IMAGE_WIDTH = 160
MAX_CAPTCHA = len(text)
print("验证码文本最长字符数", MAX_CAPTCHA)  # 验证码最长4字符; 我全部固定为4,可以不固定. 如果验证码长度小于4，用'_'补齐


# 把彩色图像转为灰度图像（色彩对识别验证码没有什么用）
def convert2gray(img):
    if len(img.shape) > 2:
        gray = np.mean(img, -1)
        # 上面的转法较快，正规转法如下
        # r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
        # gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
        return gray
    else:
        return img


"""
cnn在图像大小是2的倍数时性能最高, 如果你用的图像大小不是2的倍数，可以在图像边缘补无用像素。
np.pad(image,((2,3),(2,2)), 'constant', constant_values=(255,))  # 在图像上补2行，下补3行，左补2行，右补2行
"""
# 文本转向量
char_set = number + alphabet + ALPHABET + ['_']  # 如果验证码长度小于4, '_'用来补齐
CHAR_SET_LEN = len(char_set)


def text2vec(text):
    text_len = len(text)
    if text_len > MAX_CAPTCHA:
        raise ValueError('验证码最长4个字符')

    vector = np.zeros(MAX_CAPTCHA * CHAR_SET_LEN)

    def char2pos(c):
        if c == '_':
            k = 62
            return k
        k = ord(c) - 48
        if k > 9:
            k = ord(c) - 55  # A:65 65-55=10
            if k > 35:
                k = ord(c) - 61  # a:97 97-36=61
                if k > 61:
                    raise ValueError('No Map')
        return k

    # enumerate() 函数用于将一个可遍历的数据对象(如列表、元组或字符串)组合为一个索引序列，
    # 同时列出数据和数据下标，一般用在 for 循环当中。
    # i 下标 c 数据
    for i, c in enumerate(text):
        idx = i * CHAR_SET_LEN + char2pos(c)
        vector[idx] = 1
    return vector


# 向量转回文本
def vec2text(vec):
    # nonzero函数是numpy中用于得到数组array中非零元素的位置（数组索引）的函数。
    char_pos = vec.nonzero()[0]
    # [  0  73 162 189]
    text = []
    for i, c in enumerate(char_pos):
        char_at_pos = i  # c/63
        char_idx = c % CHAR_SET_LEN  # c%63
        if char_idx < 10:
            char_code = char_idx + ord('0')  # 48
        elif char_idx < 36:
            char_code = char_idx - 10 + ord('A')  # 65
        elif char_idx < 62:
            char_code = char_idx - 36 + ord('a')  # 97
        elif char_idx == 62:
            char_code = ord('_')
        else:
            raise ValueError('error')
        text.append(chr(char_code))
    return "".join(text)

    """
    #向量（大小MAX_CAPTCHA*CHAR_SET_LEN）用0,1编码 每63个编码一个字符，这样顺利有，字符也有
    vec = text2vec("F5Sd")
    text = vec2text(vec)
    print(text)  # F5Sd
    vec = text2vec("SFd5")
    text = vec2text(vec)
    print(text)  # SFd5
    """

