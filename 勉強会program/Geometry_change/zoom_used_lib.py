# -*- coding: utf-8 -*-
"""
Created on Wed May 22 02:35:12 2019

@author: akinori
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 22 01:33:01 2019

@author: akinori
"""

import cv2
import glob
import os
import numpy as np
import csv
from operator import itemgetter

input_img = cv2.imread("src.png", 1)
width, height, chanel = input_img.shape

zoomed_img = cv2.resize(input_img, (int(width*0.5), int(height*1.0)), interpolation = cv2.INTER_LINEAR)

cv2.imshow("input_img", input_img)
cv2.imshow("zoomed_img", zoomed_img)

cv2.imwrite("test_zoomed_img_cubic.png",zoomed_img)


cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
