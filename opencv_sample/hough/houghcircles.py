# -*- coding: utf-8 -*-
import cv2
import numpy as np

img_src = cv2.imread('AB195_L.jpg', 1)
img_dst = img_src.copy()

# グレースケール化
img_gray = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)

# ほかし処理
img_gray = cv2.medianBlur(img_gray, 5)

# ハフ変換による円検出
circles = cv2.HoughCircles(img_gray, cv2.HOUGH_GRADIENT, 5, 100)

# 円の描画
for x, y, r in circles[0,:]:
    cv2.circle(img_dst, (x, y), r, (0, 0, 255), 3)

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
