# -*- coding: utf-8 -*-
"""
Created on Wed May 22 12:44:31 2019

@author: akinori
"""



import cv2
import math
import numpy as np

input_img = cv2.imread("src.png", 1)
width, height, chanel = input_img.shape
center = tuple(np.array([0, 0]))
#center = tuple(np.array([input_img.shape[1]*0.5, input_img.shape[0]*0.5]))
angle = -30.0
scale = 1.0
size = tuple(np.array([input_img.shape[1], input_img.shape[0]]))
pts1 = np.float32([[160, 0], [480, 479], [480, 240], [160, 240]])
pts2 = np.float32([[260, 479], [480, 479], [400, 240], [240, 240]])

psp_mat = cv2.getPerspectiveTransform(pts1, pts2)

output_img = cv2.warpPerspective(input_img, psp_mat, size)
cv2.imshow("input_img", input_img)
cv2.imshow("output_img", output_img)

cv2.imwrite("shaei_change.png",output_img)


cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
