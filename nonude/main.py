#!/usr/bin/env python
# coding=utf-8

import glob

import itertools
import nude

# 用 glob 返回匹配指定模式的文件名
images_jpg = glob.glob("*.jpg")  # 返回匹配指定模式的文件名
images_png = glob.glob("*.png")
images_gif = glob.glob("*.gif")

# itertools.chain 把迭代对象串联起来，形成一个更大的迭代器
images_list = itertools.chain(images_jpg, images_png, images_gif)

for img in images_list:
    n = nude.Nude(img)  # 对图片进行识别
    n.parse()
    print(img, n.result, n.message)  # 输出结果和判断信息
    print(n.inspect())  # 输出更加详细的判断信息

print(nude.is_nude("1.jpg"))
