# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:25:15 2019

@author: akinori
"""

import cv2
import numpy as np

def cordinate_coloring (Img_src, signal_cordinate_x, signal_cordinate_y, color_pallette):
    
    Img_dst = Img_src
    for rows in range (0, signal_cordinate_x.shape[0]):
        for column in range (0, signal_cordinate_x.shape[1]):
            Img_dst[signal_cordinate_y[rows][column], signal_cordinate_x[rows][column]] = color_pallette
    return Img_dst