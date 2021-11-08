# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 12:35:43 2019

@author: akinori
"""
import cv2
import numpy as np

def erosion_dilation (binarization, erosion_neibor_number, dilation_neibor_number):
         # ２近傍定義
    neiborhood2 = np.array([1, 1, 1],
                                np.uint8)
    
     # ４近傍定義
    neiborhood4 = np.array([[0, 1, 0],
                                [1, 1, 1],
                                [0, 1, 0]],
                                np.uint8)
     # ８近傍定義
    neiborhood8 = np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]],
                                np.uint8)
    
    all_neiborhood = {2:neiborhood2, 4:neiborhood4, 8:neiborhood8} # 定義した近傍設定を呼び出すための母体
    erosion_neiborhood = all_neiborhood[erosion_neibor_number] # 収縮時の近傍選択　２か４か８
    dilation_neiborhood = all_neiborhood[dilation_neibor_number] # 膨張時の近傍選択　２か４か８
    
    eroded = cv2.erode(binarization,erosion_neiborhood,iterations = 0)
    return cv2.dilate(eroded, dilation_neiborhood, iterations = 0)

    
