# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:19:11 2021

@author: arailab
"""

import cv2

WIDTH = 512
HEIGHT = 512

img = cv2.imread("rena.png", 1)
for x in range(HEIGHT):
    for y in range(WIDTH):
        b, g, r = img[x,y]
        img[x,y] = 0, g, 0
cv2.imshow("kadai", img)
cv2.imwrite("kadai.png", img)

cv2.waitKey(0)
cv2.destroyAllWindows()