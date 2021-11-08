# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:40:32 2021

@author: frees
"""
import numpy as np
import cv2

distance = 1.0
gap = 1
coordinate_x = np.loadtxt(
        fname = "../" + str(distance) + "/coordinate/" + "coordinate_x_ideal.csv",
        dtype = "int",
        delimiter = ","
        )

coordinate_y = np.loadtxt(
        fname = "../" + str(distance) + "/coordinate/" + "coordinate_y_ideal.csv",
        dtype = "int",
        delimiter = ","
        )

for gap in range (0, 360):
    print("gap",gap)
    first_demodulated_data_list = []
    second_demodulated_data_list = []
    first_demodulated_data_list_2D = []
    second_demodulated_data_list_2D = []
    first_error_counter = 0
    second_error_counter = 0
    first_error_counter_list = []
    second_error_counter_list = []
    #混在画像入力
    im_first_mixed_data = cv2.imread("../" + str(distance) + "/data_part/" + str(gap) + "shifted_first_mixed_data.png",0)
    im_second_mixed_data = cv2.imread("../" + str(distance) + "/data_part/" + str(gap) + "shifted_second_mixed_data.png",0)
    #混在シグナル入力
    first_mixed_signal =np.loadtxt(
            fname = "../"  + str(distance) + "/mixed_signal/" + str(gap) +"shifted_first_mixed_signal.csv",
            dtype = "int",
            delimiter = ","
            )
    second_mixed_signal =np.loadtxt(
            fname = "../" + str(distance) + "/mixed_signal/" + str(gap) +"shifted_second_mixed_signal.csv",
            dtype = "int",
            delimiter = ","
            )
    for ln in range(0, 9):
        first_demodulated_data_list = []
        second_demodulated_data_list = []
        for d in range (0, 360):
            #復調
            if im_first_mixed_data[coordinate_y[ln,d],coordinate_x[ln,d]] > 100:
                first_demodulated_data_list.append(1)
            else:
                first_demodulated_data_list.append(0)
                
            if im_second_mixed_data[coordinate_y[ln,d],coordinate_x[ln,d]] > 100:
                second_demodulated_data_list.append(1)
            else:
                second_demodulated_data_list.append(0)
        first_demodulated_data_list_2D.append(first_demodulated_data_list)
        second_demodulated_data_list_2D.append(second_demodulated_data_list)
    #エラーカウント
    for y in range(0,len(first_demodulated_data_list_2D)):
        for x in range(0,len(first_demodulated_data_list_2D[0])):
            if first_demodulated_data_list_2D[y][x] != first_mixed_signal[y,x]:
                first_error_counter += 1
            if second_demodulated_data_list_2D[y][x] != second_mixed_signal[y,x]:
                second_error_counter += 1
    print("first_error_counter",first_error_counter)
    print("second_error_counter",second_error_counter)
    first_error_counter_list.append(first_error_counter)
    second_error_counter_list.append(second_error_counter)
    
    
            
            
            
            
            
            
            
            
            
            
            
            
                