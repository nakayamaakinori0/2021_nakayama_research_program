# -*- coding: utf-8 -*-
import cv2
import numpy as np

# チェスボード画像
files = ['1.bmp', '2.bmp', '3.bmp', '4.bmp', '5.bmp'] 

# カメラパラメータを読み込み
camera_matrix = np.loadtxt("camera_matrix.csv", delimiter =',')
dist_coefs = np.loadtxt("dist_coefs.csv", delimiter =',')
print(camera_matrix)
print(dist_coefs)

# 歪み補正
for i in files:
    img_src = cv2.imread(i, 1)
    img_dst = cv2.undistort(img_src, camera_matrix, dist_coefs)
    cv2.imshow('dst', img_dst)
    cv2.waitKey(0)

cv2.destroyAllWindows()
