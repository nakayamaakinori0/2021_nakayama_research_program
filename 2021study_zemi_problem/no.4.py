# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 15:44:11 2021

@author: arailab
"""

import cv2
import numpy as np


im = cv2.imread("input_no.4.png", 0)
#普通の二値化
ret, im_bin1 = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY)
#適応閾値処理
im_bin_adap_mean = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
im_bin_adap_gauss = cv2.adaptiveThreshold(im, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
                                             #(im, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
#大津式
ret, im_bin_otsu = cv2.threshold(im,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
blur = cv2.GaussianBlur(im,(5,5),0)
ret, im_bin_otsu_gauss = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("input",im)
cv2.imshow("im_bin1",im_bin1)
cv2.imshow("im_bin_adap_mean",im_bin_adap_mean)
cv2.imshow("im_bin_adap_gauss",im_bin_adap_gauss)
cv2.imshow("im_bin_otsu",im_bin_otsu)
cv2.imshow("blur",blur)
cv2.imshow("im_bin_otsu_gauss",im_bin_otsu_gauss)

nlabels, labels, stats, centroids = cv2.connectedComponentsWithStats(im_bin1)
contours, hierarchy = cv2.findContours(im_bin1, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
area = cv2.contourArea(contours[1])
perimeter = cv2.arcLength(np.array(contours[1]), True)
roundness = 4* np.pi * area / perimeter / perimeter
print(perimeter)

cv2.waitKey(0)
cv2.destroyAllWindows()