# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:14:52 2019

@author: arailab
"""


import cv2
import numpy as np

img = cv2.imread("src.png")
"""
a = np.array([[1,1,1],
              [1,-8,1],
              [1,1,1]])
img_tmp = cv2.filter2D(img,-1,a)
img_dst = cv2.convertScaleAbs(img_tmp)
cv2.imshow("kyoutyou", img_dst)
"""


cv2.waitKey(0)
cv2.destroyAllWindows()