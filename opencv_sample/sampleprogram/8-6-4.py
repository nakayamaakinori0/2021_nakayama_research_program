# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

#file_src = 'star.png'
file_src = 'circle.png'
#file_src = 'crescent.png'
#file_src = 'ellipse.png'
#file_src = 'spiral.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 0)

cv2.namedWindow('src')
cv2.namedWindow('dst')

#contours,  hierarchy = cv2.findContours(img_src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contours = cv2.findContours(img_src, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[1]
area = cv2.contourArea(contours[0])
perimeter = cv2.arcLength(np.array(contours[0]), True)
roundness = 4 * np.pi * area / perimeter / perimeter
print(area, perimeter, roundness)
# area: 画素数, perimeter: 周囲長, roundness: 円形度

cv2.imshow('src', img_src) # 入力画像を表示
#cv2.imshow('dst', img_dst) # 出力画像を表示
#cv2.imwrite(file_dst, img_dst); # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
