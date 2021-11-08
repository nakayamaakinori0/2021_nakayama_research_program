# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:39:19 2019

@author: akinori
"""

import cv2
import numpy as np


def make_mask(image_t1, image_t2):
    img_gray_t1 = cv2.cvtColor(image_t1, cv2.COLOR_BGR2GRAY)
    img_gray_t2 = cv2.cvtColor(image_t2, cv2.COLOR_BGR2GRAY)
    img_df = cv2.absdiff(img_gray_t1, img_gray_t2)
    threshold, img_binari = cv2.threshold(img_df, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化)
    op = np.ones((3, 3), np.uint8)
    img_dilated = cv2.dilate(img_binari, op, iterations=1)
    img_mask = cv2.erode(img_dilated, op, iterations=1)
    return img_mask
