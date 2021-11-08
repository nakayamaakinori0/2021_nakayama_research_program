# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:30:39 2019

@author: akinori
"""

import cv2
import numpy as np

input_img = cv2.imread("src.png", 0)
height, width,= input_img.shape
operator_x = []
operator_y = []
pvalue_array = np.array([[0 for i in range (3)]for i in range (3)])

for y in range(0, height):
    op_count = 0
    for x in range (0, width):
        for count in range (1, 10):
            if count == 1:
                operator_x.append(x - 1)
                operator_y.append(y - 1)
            elif count == 2:
                operator_x.append(x)
                operator_y.append(y - 1)
            elif count == 3:
                operator_x.append(x + 1)
                operator_y.append(y - 1)
            elif count == 4:
                operator_x.append(x - 1)
                operator_y.append(y)
            elif count == 5:
                operator_x.append(x)
                operator_y.append(y)
            elif count == 6:
                operator_x.append(x + 1)
                operator_y.append(y)
            elif count == 7:
                operator_x.append(x - 1)
                operator_y.append(y + 1)
            elif count == 8:
                operator_x.append(x)
                operator_y.append(y + 1)
            elif count == 9:
                operator_x.append(x + 1)
                operator_y.append(y + 1)
                for array_y in range (0, 3):
                    for array_x in range (0, 3):
                        if operator_y[op_count] >= 0 and operator_y[op_count] <= height - 1:
                            if operator_x[op_count] >= 0 and operator_x[op_count] <= width - 1:
                                pvalue_array[array_x][array_y] = input_img[operator_y[op_count], operator_x[op_count]]
                                op_count += 1
                            else:
                                pvalue_array[array_x][array_y] = 0
                                op_count += 1
                        else:
                            pvalue_array[array_x][array_y] = 0
                            op_count += 1
                            

                                
                        
                        
                        
                        
                        
                        