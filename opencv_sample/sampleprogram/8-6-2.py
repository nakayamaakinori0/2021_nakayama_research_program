# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

#file_src = 'star.png'
#file_src = 'circle.png'
#file_src = 'crescent.png'
#file_src = 'ellipse.png'
file_src = 'spiral.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 0)

cv2.namedWindow('src')
cv2.namedWindow('dst')

rows, cols = img_src.shape[:2]
print(rows, cols)

x_min = cols
x_max = 0
y_min = rows
y_max = 0

for y in range(rows):
	for x in range(cols):
		if img_src[y, x] == 255:
			if x < x_min:
				x_min = x
			elif x > x_max:
				x_max = x
			if y < y_min:
				y_min = y
			elif y > y_max:
				y_max = y

aspectratio = float(y_max - y_min) / float(x_max - x_min)
print(aspectratio)

cv2.rectangle(img_src, (x_min, y_min), (x_max, y_max), 128, 2)

cv2.imshow('src', img_src) # 入力画像を表示
#cv2.imshow('dst', img_dst) # 出力画像を表示
#cv2.imwrite(file_dst, img_dst); # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
