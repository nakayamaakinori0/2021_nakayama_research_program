# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:42:17 2019

@author: akinori
"""

import cv2
import numpy as np

src1_filename = 'heada1.png'
src2_filename = 'heada2.png'
src1 = cv2.imread(src1_filename, 1)
src2 = cv2.imread(src2_filename, 1)

gray_src1 = cv2.cvtColor(src1, cv2.COLOR_BGR2GRAY)
gray_src2 = cv2.cvtColor(src2, cv2.COLOR_BGR2GRAY)

# dst = np.abs(gray_src1 - gray_src2)
# dst = gray_src1 + gray_src2
df = cv2.absdiff(gray_src1, gray_src2)
threshokd, binari = cv2.threshold(df, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化)
op = np.ones((3, 3), np.uint8)
md = cv2.dilate(binari, op, iterations = 2)
mask = cv2.erode(md, op, iterations = 2)
dst = cv2.bitwise_and(gray_src1, mask)

cv2.imwrite('dst.png',dst)

cv2.imshow('df',df)
cv2.imshow('binari',binari)
cv2.imshow('md',md)
cv2.imshow('mask',mask)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()