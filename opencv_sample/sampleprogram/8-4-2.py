# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

#file_src = 'src.png'
file_src = 'src_bin.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 1)

cv2.namedWindow('src')
cv2.namedWindow('dst')

element4 = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], np.uint8) # 4 近傍
element8 = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]], np.uint8) # 8 近傍
img_dst = cv2.dilate(img_src, element8, iterations = 5)
#img_dst = cv2.erode(img_src, element4, iterations = 5)

cv2.imshow('src', img_src) # 入力画像を表示
cv2.imshow('dst', img_dst) # 出力画像を表示
cv2.imwrite(file_dst, img_dst); # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
