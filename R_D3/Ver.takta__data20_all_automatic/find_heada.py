# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:39:17 2019

@author: akinori
"""
import cv2
import numpy as np


def get_heada_vlue(image_t1, image_t2, img_mask):
    img_gray_t1 = cv2.cvtColor(image_t1, cv2.COLOR_BGR2GRAY)
    img_gray_t2 = cv2.cvtColor(image_t2, cv2.COLOR_BGR2GRAY)
    img_bitwised_t1 = cv2.bitwise_and(img_gray_t1, img_mask)
    img_bitwised_t2 = cv2.bitwise_and(img_gray_t2, img_mask)
    img_logical_sum = cv2.absdiff(img_bitwised_t1, img_bitwised_t2)
    sum_value = np.sum(img_logical_sum)
    return sum_value
