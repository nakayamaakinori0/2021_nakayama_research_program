# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:16:07 2019

@author: akinori
"""

import cv2
import math
import numpy as np

input_img = cv2.imread("src.png", 1)
width, height, chanel = input_img.shape

size = tuple(np.array([width,height]))

afn_mat = np.float32([[math.cos(-math.pi / 4), -math.sin(-math.pi / 4), 0],
                     [math.sin(-math.pi / 4), math.cos(-math.pi / 4), input_img.shape[0] * 0.5]])

output_img = cv2.warpAffine(input_img, afn_mat, size, flags = cv2.INTER_LINEAR)

cv2.imshow("input_img", input_img)
cv2.imshow("output_img", output_img)

cv2.imwrite("affine_change.png",output_img)


cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
