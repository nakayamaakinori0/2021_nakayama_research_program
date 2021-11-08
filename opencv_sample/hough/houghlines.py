# -*- coding: utf-8 -*-
import cv2
import numpy as np

img_src = cv2.imread('AB090_L.jpg', 1)
img_dst = img_src.copy()

# グレースケール化
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

# エッジ検出
img_edge = cv2.Canny(img_gray, 200, 700)

# ハフ変換による直線検出
lines = cv2.HoughLines(img_edge, 1, np.pi/180, 100)
rows, cols = img_dst.shape[:2]
   
# 線の描画
#for i, line in enumerate(lines):
for rho, theta in lines[:,0]:
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    cv2.line(img_dst,
		(int(x0 - cols*(b)), int(y0 + cols*(a))), 
		(int(x0 + cols*(b)), int(y0 - cols*(a))), 
		(0, 0, 255), 2)

cv2.imshow('src', img_src)
cv2.imshow('edge', img_edge)
cv2.imshow('dst', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
