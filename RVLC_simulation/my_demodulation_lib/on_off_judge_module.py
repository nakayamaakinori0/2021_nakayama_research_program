# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:03:12 2019

@author: akinori
"""

import numpy as np

def on_off_judge (Img_src,signal_cordinate_x, signal_cordinate_y, jujge_threshold_arr):
    
    true_singo = np.zeros((signal_cordinate_x.shape[0], signal_cordinate_x.shape[1]), dtype = 'str')
    #oya_singo = []
    #ko_singo = []
    for rows in range (0, signal_cordinate_x.shape[0]):
        #oya_singo.append(ko_singo)
        for column in range (0, signal_cordinate_x.shape[1] ):
            if Img_src[signal_cordinate_y[rows, column],signal_cordinate_x[rows, column]] > jujge_threshold_arr[rows, column]:
                true_singo[rows,column] = '1'
                #ko_singo.append('1')
            else:
                true_singo[rows,column] = '_'
                #ko_singo.append(' ')
    return true_singo
#oya_singo