# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

file_src = 'src.png'
file_dst = 'dst.png'

# img_src = cv2.imread(file_src, 1) # 入力画像（カラー）の読み込み
img_src = cv2.imread(file_src, 0) # 入力画像（グレースケール）の読み込み

cv2.namedWindow('src')
cv2.namedWindow('dst')

# ここに核となる処理を記述する
num_lab, img_lab = cv2.connectedComponents(img_src)
print(num_lab)
img_dst = cv2.compare(img_lab, 10, cv2.CMP_EQ)

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.imwrite('img_label.png', img_dst);
cv2.waitKey(0)
cv2.destroyAllWindows()
