# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:03:12 2019

@author: akinori
"""

import numpy as np

def on_off_judge (Img_src,signal_cordinate_x, signal_cordinate_y, jujge_threshold_arr):
    
    singo = np.zeros((signal_cordinate_x.shape[0], signal_cordinate_x.shape[1]), dtype = 'int32')
    
    for rows in range (0, signal_cordinate_x.shape[0]):
        for column in range (0, signal_cordinate_x.shape[1] ):
            if Img_src[signal_cordinate_y[rows, column],signal_cordinate_x[rows, column]] > jujge_threshold_arr[rows, column]:
                singo[rows,column] = 1
            else:
                singo[rows,column] = 0
    return singo