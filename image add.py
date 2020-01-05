# E:\learning_opencv\PycharmProjects
# -*- coding: utf-8 -*-
# @Time    : 2020/1/5 14:15
# @Author  : Paris
# @File    : 10 image + add.py
import cv2
import numpy as np
src_01 = cv2.imread('E:/learning_opencv/beauty/ssso.jpg',0)

nu_1 = src_01+src_01
nu_2 = cv2.add(src_01,src_01)

cv2.imshow('0',src_01)
cv2.imshow('1',nu_1)
cv2.imshow('2',nu_2)

print('原始',src_01[100,100])
print('直接+的',nu_1[100,100])
print('add的',nu_2[100,100])
print('235+235=',235+235)
print('235+235-255=',235+235-255)
cv2.waitKey()
cv2.destroyAllWindows()
