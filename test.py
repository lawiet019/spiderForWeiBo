#coding:utf-8
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread("./doc/img/greyscale/01.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
ret1, th3 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)

for i in range(1,th3.shape[0]):
    for j in range(1,th3.shape[1]):
        if th3[i,j] == 0:
            continue
        #向左判断
        TopCount = 0
        front = False
        for top in range(0,i+1):
            if th3[top,j] == 0:
                front = True
            if th3[top,j] ==255 and front:
                TopCount = TopCount +1
                front = False
        BottomCount = 0
        front = False
        for bottom in range(i,th3.shape[0]):
            if th3[bottom,j] == 0:
                front = True
            if th3[bottom,j] ==255 and front:
                BottomCount = BottomCount +1
                front = False
        LeftCount = 0
        front = False
        for left in range(0,j+1):
            if th3[i,left] == 0:
                front = True
            if th3[i,left] ==255 and front:
                LeftCount = LeftCount +1
                front = False
        RightCount = 0
        front = False
        for right in range(0,j+1):
            if th3[i,left] == 0:
                front = True
            if th3[i,left] ==255 and front:
                LeftCount = LeftCount +1
                front = False
