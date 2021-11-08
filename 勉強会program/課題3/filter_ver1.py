# -*- coding: utf-8 -*-
"""
Created on Wed May  8 12:27:21 2019

@author: Arailab
"""

import cv2
import numpy as np
import glob

#微分(横)
kernel0 = np.array([[ 0, 0, 0],
                    [-1, 1, 0],
                    [ 0, 0, 0]])

#prewitt横
kernel1 = np.array([[-1, 0, 1],
                    [-1, 0, 1],
                    [-1, 0, 1]])


#sobel横微分
kernel2 = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])


#sobel縦微分
kernel3 = np.array([[-1, -2, -1],
                    [ 0,  0,  0],
                    [ 1,  2,  1]])

#2次微分
kernel4 = np.array([[ 0,  1,  0],
                    [ 1, -4,  1],
                    [ 0,  1,  0]])

#鮮鋭化
kernel5 = np.array([[-1, -1, -1],
                    [-1,  9, -1],
                    [-1, -1, -1]])

kernel_t = np.array([[ -1,  -2, -1],
                     [-2,  0, 2],
                     [ -1, 2, 1]])

def filter2d(image, k):
    
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
    
    dst = cv2.filter2D(gray, -1, k)
    
    return dst

images = glob.glob("input/*.jpg")

for fname in images:
    img = cv2.imread(fname)
    dst0 = filter2d(img, kernel2)
    cv2.imshow("dst0", dst0)
    cv2.imwrite("dst0.jpg", dst0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
for fname in images:
    img = cv2.imread(fname)
    dst0 = filter2d(img, kernel3)
    cv2.imshow("dst0", dst0)
    cv2.imwrite("dst1.jpg", dst0)
    cv2.waitKey(0)
    cv2.destroyAllWindows()