# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:19:40 2019

@author: arailab
"""

import cv2
import numpy as np

src = cv2.imread("sinkago.png")
mask = cv2.imread("Squirtle.png",0)

height, widht, color = src.shape
dst = np.zeros((height,widht,3), dtype="uint8")

for y in range(0,height):
    for x in range(0,widht):
        if (mask[y][x] > 200):
            dst[y][x] = src[y][x]
        else:
            dst[y][x] = 0
               
cv2.imshow("1",dst)
cv2.imwrite("1.png",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
