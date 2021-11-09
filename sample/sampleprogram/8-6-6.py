# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

# file_src = 'star.png'
#file_src = 'circle.png'
file_src = 'crescent.png'
#file_src = 'ellipse.png'
#file_src = 'spiral.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 0)

cv2.namedWindow('src')
cv2.namedWindow('dst')

m = cv2.moments(img_src)
area = m['m00']
x_g = m['m10'] / m['m00']
y_g = m['m01'] / m['m00']
ang = 0.5 * math.atan2(2.0 * m['mu11'], m['mu20'] - m['mu02'])
print(x_g, y_g, ang * 180.0 / math.pi)

x1 = int(x_g - 200*np.cos(ang))
y1 = int(y_g - 200*np.sin(ang))
x2 = int(x_g + 200*np.cos(ang))
y2 = int(y_g + 200*np.sin(ang))
cv2.line(img_src, (x1, y1), (x2, y2), 128, 2)

cv2.imshow('src', img_src) # 入力画像を表示
#cv2.imshow('dst', img_dst) # 出力画像を表示
#cv2.imwrite(file_dst, img_dst); # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
