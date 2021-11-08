# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 20:42:17 2019

@author: akinori
"""

import cv2
import numpy as np

img_src1_filename = 'heada1.png'
img_src2_filename = 'heada2.png'
img_src1 = cv2.imread(img_src1_filename, 1)
img_src2 = cv2.imread(img_src2_filename, 1)

gray_img_src1 = cv2.cvtColor(img_src1, cv2.COLOR_BGR2GRAY)
gray_img_src2 = cv2.cvtColor(img_src2, cv2.COLOR_BGR2GRAY)

# img_dst = np.abs(gray_img_src1 - gray_img_src2)
# img_dst = gray_img_src1 + gray_img_src2
img_df = cv2.absdiff(gray_img_src1, gray_img_src2)
threshold, img_binari = cv2.threshold(img_df, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化)
op = np.ones((3, 3), np.uint8)
img_md = cv2.dilate(img_binari, op, iterations=2)
img_mask = cv2.erode(img_md, op, iterations=2)
img_bitwised1 = cv2.bitwise_and(gray_img_src1, img_mask)
img_bitwised2 = cv2.bitwise_and(gray_img_src2, img_mask)
img_logical_sum = cv2.absdiff(img_bitwised1, img_bitwised2)
print('合計値', np.sum(img_logical_sum), [...])

cv2.imwrite('img_logical_sum.png', img_logical_sum)
cv2.imshow('img_df', img_df)
cv2.imshow('img_binari', img_binari)
cv2.imshow('img_md', img_md)
cv2.imshow('mask', img_mask)
cv2.imshow('img_logical_sum', img_logical_sum)
cv2.waitKey(0)
cv2.destroyAllWindows()
