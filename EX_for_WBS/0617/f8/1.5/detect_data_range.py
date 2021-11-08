# -*- coding: utf-8 -*-
"""
Created on Fri Jun 25 14:53:20 2021

@author: arailab
"""

import cv2
import numpy as np
from mylib import mymodules as mm
im_data_range_color = cv2.imread("header2/2.png", 1)
im_data_range = cv2.imread("header2/2.png", 0)
im_mask = cv2.imread("header1_mask/binary_mask.png",0)
im_data_range_trimmed = cv2.bitwise_and(im_data_range, im_mask)
blur = cv2.GaussianBlur(im_data_range_trimmed,(5,5),0)
ret, im_binary_data_range_trimmed = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imwrite("header2_trimmed/header2_trimmed.png", im_data_range_trimmed)



color_pallette = (0, 255, 0)
arr_coordinates_data_range = mm.getCodnCylinder(im_binary_data_range_trimmed)
im_colorerd = mm.coordinate_coloring_2D(im_data_range_color, arr_coordinates_data_range, color_pallette)#img_src, coordinate_list, color_pallette

cv2.imshow("im_colorerd",im_colorerd)
cv2.waitKey(0)
cv2.destroyAllWindows()
