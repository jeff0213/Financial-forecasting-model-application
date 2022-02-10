# -*- coding: utf-8 -*-
# @Time    : 2022/2/10 11:39
# @Author  : jeff0213
# @File    : drawing.py
# @Software: PyCharm
import numpy as np
from matplotlib import pyplot as plt
import json


def draw(b, c, d):
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    x = np.arange(len(x))
    tick_label = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    width = 0.35
    plt.figure(figsize=[20, 15])
    plt.bar(x, b, width, alpha=0.9, label='Business-area profits without the patent technology')
    plt.plot(x + width / 2, c, marker='*', label='Foreseeable profits for the patent technology')
    plt.bar(x + width, d, width, alpha=0.9, label='Business-area profits with the patent technology')
    plt.xticks(x + width / 2, tick_label)  # 将坐标设置在指定位置
    # plt.xticklabels(x)#将横坐标替换成
    plt.legend()
    plt.savefig("result.png")
    plt.show()


# 根据图片文件路径获取hyp
def load_json(FilePath):
    with open(FilePath, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict


if __name__ == '__main__':
    load_dict = load_json('result.json')
    b = load_dict["Business-area profits without the patent technology"]
    c = load_dict["Foreseeable profits for the patent technology"]
    d = load_dict["Business-area profits with the patent technology "]
    draw(b, c, d)
