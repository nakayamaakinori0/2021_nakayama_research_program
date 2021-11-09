# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:32:43 2021

@author: arailab
"""

import cv2
import numpy as np
im = cv2.imread("rena.png")
img_nega = 255 - im
k = 1.0
op = np.array([[-k,-k,-k],
               [-k,1+8*k, -k],
               [-k,-k,-k]])

img_tmp = cv2.filter2D(im, -1, op)
img_tmp_nega = cv2.filter2D(im, -1, op)
img_dst = cv2.convertScaleAbs(img_tmp)
img_dst_nega = cv2.convertScaleAbs(img_tmp_nega)

cv2.imshow("input", im)
cv2.imshow("out", img_dst)
cv2.imshow("img_nega", img_nega)
cv2.imshow("out_nega", img_dst_nega)



cv2.waitKey(0)
cv2.destroyAllWindows()
