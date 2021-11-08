# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 15:26:07 2021

@author: arailab
"""

import cv2
import glob
import numpy as np
import csv
import copy
from mylib import mymodules as mm
import os
# 入力ディレクトリ
# 入力ディレクトリ
input_dir = "capture_img"
header1_dir = "header1"
header2_dir = "header2"
header3_dir = "header3"
header4_dir = "header4"
footer_dir = "footer"
header3_trimmed_dir = "header3_trimmed"
header4_trimmed_dir = "header4_trimmed"
data_dir = "data"
# 出力ディレクトリ
eroded_dilated_dir = "eroded_dilated"
coloring_dir = "coloring"
# 入力画像のパス
input_path = glob.glob(input_dir + '/*')
header3_path = glob.glob(header3_dir + '/*')
header4_path = glob.glob(header4_dir + '/*')
header3_trimmed_path = glob.glob(header3_trimmed_dir + '/*')
header4_trimmed_path = glob.glob(header4_trimmed_dir + '/*')
data_path = glob.glob(data_dir + '/*')
colorling_path = glob.glob(coloring_dir + '/*')

im_header1_1 = cv2.imread("header1/0.png", 0)
im_header1_2 = cv2.imread("header1/1.png", 0)

im_mask = cv2.absdiff(im_header1_1, im_header1_2)
kernel = np.ones((5,5),np.uint8)
im_dilated_mask = cv2.dilate(im_mask, kernel, iterations = 1)
im_eroded_mask_after_dilated = cv2.erode(im_dilated_mask, kernel, iterations = 1)
cv2.imshow("im_mask",im_mask)
cv2.imshow("im_dilated_mask",im_dilated_mask)
cv2.imshow("im_eroded_mask_after_dilated",im_eroded_mask_after_dilated)
cv2.imwrite("header1_mask/mask.png", im_eroded_mask_after_dilated)
ret, im_binary_mask = cv2.threshold(im_eroded_mask_after_dilated, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
im_binary_dilated_mask = cv2.dilate(im_binary_mask, kernel, iterations = 1)
im_binary_eroded_mask_after_dilated = cv2.erode(im_binary_dilated_mask, kernel, iterations = 1)
cv2.imwrite("header1_mask/binary_mask.png",im_binary_eroded_mask_after_dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()