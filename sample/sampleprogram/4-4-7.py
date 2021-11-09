# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

#file_src = 'src.png'
file_src = 'colorbar.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 1)

cv2.namedWindow('src')
cv2.namedWindow('dst')

img_dst = cv2.cvtColor(img_src, cv2.COLOR_BGR2HSV)

img_h, img_s, img_v = cv2.split(img_dst)
img_msk_h = cv2.inRange(img_h, 0, 10)
img_msk_s = cv2.inRange(img_s, 100, 255)
img_msk_v = cv2.inRange(img_v, 0, 255)
img_msk = cv2.bitwise_and(img_msk_h, img_msk_s, img_msk_v)
cv2.imshow('msk', img_msk)

cv2.imshow('src', img_src) # 入力画像を表示
cv2.imshow('dst', img_dst) # 出力画像を表示
cv2.imwrite(file_dst, img_dst); # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
