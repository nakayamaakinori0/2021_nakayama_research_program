# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

file_src = 'src.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 1)

cv2.namedWindow('src')
cv2.namedWindow('dst')

# ルックアップテーブル生成
Y =  np.ones((256, 1), dtype = 'uint8') * 0
for i in range(256):
	Y[i][0] = 255 * pow(float(i) / 255, 1.0 / 2.0)
# ルックアップテーブル変換
img_dst = cv2.LUT(img_src,Y)

cv2.imshow('src', img_src) # 入力画像を表示
cv2.imshow('dst', img_dst) # 出力画像を表示
cv2.imwrite(file_dst, img_dst); # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
