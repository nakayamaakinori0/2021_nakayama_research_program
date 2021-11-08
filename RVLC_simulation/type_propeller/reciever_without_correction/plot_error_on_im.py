# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 14:53:09 2021

@author: arailab
"""

import cv2
import numpy as np
import math
import pprint
import csv
import copy
from mylib import type_propeller as tpp
from mylib import mymodules as mm

tras_dr = "../transmitter"
head_dr = "header_part"
data_dr = "data_part"
t_codn_dr = "coordinate"
r_codn_dr =  "result_coordinate"
t_sig_dr = "transmitted_signal"
t_sigm_dr = "mixed_signal"
r_sigm_dr = "result_pv"
out_dr = "error_plot"
#distance = 1.0
#gap = 200
color_pallette = [0,0,255]

for d in range(10, 50, 5):
    distance = d/10
    for gap in range (0, 360, 1):
        print("distance", distance)
        print("gap",gap)
        #画像入力
        im_first_data = cv2.imread(tras_dr + "/" + str(distance) + "/" + data_dr + "/" + str(gap) + "shifted_first_mixed_data.png",1)
        im_second_data = cv2.imread(tras_dr + "/" + str(distance) + "/" + data_dr + "/" + str(gap) + "shifted_second_mixed_data.png",1)
        
        #座標入力
         #trasmitter side
        codx_idl_arr = np.loadtxt(tras_dr + "/" + str(distance) + "/" + t_codn_dr + "/" + "coordinate_x_ideal.csv",delimiter = ",", dtype = int) 
        cody_idl_arr = np.loadtxt(tras_dr + "/" + str(distance) + "/" + t_codn_dr + "/" + "coordinate_y_ideal.csv",delimiter = ",", dtype = int)
         #reciever side
        codx_ex_arr = np.loadtxt(str(distance) + "/" + r_codn_dr + "/" + "codn_x_array_result.csv",delimiter = ",", dtype = int)
        cody_ex_arr = np.loadtxt(str(distance) + "/" + r_codn_dr + "/" + "codn_y_array_result.csv",delimiter = ",", dtype = int)
         
        #signal入力
         #transmitter side
        t_sigB_arr = np.loadtxt(tras_dr + "/" + str(distance) + "/" + t_sig_dr + "/" + "B_transmitted_signal.csv",delimiter = ",")
        t_sigm1_arr = np.loadtxt(tras_dr + "/" + str(distance) + "/" + t_sigm_dr + "/" + str(gap) + "shifted_first_mixed_signal.csv",delimiter = ",")
        t_sigm2_arr = np.loadtxt(tras_dr + "/" + str(distance) + "/" + t_sigm_dr + "/" + str(gap) + "shifted_second_mixed_signal.csv",delimiter = ",")
         #reciever side
        r_sig_arr = np.loadtxt(str(distance) + "/" + r_sigm_dr + "/" + str(gap) + "shifted_recieved_signal.csv",delimiter = ",")
        ln = len(codx_ex_arr)
        degree = len(codx_ex_arr[0])
        for n in range(0, ln):
            for d in range(0, degree):
                if t_sigB_arr[n,d] != r_sig_arr[n,d]:
                    if d < gap:
                        im_first_data[codx_ex_arr[n][d], cody_ex_arr[n][d]] = color_pallette
                    elif d >= gap:
                        im_second_data[codx_ex_arr[n][d], cody_ex_arr[n][d]] = color_pallette
        cv2.imwrite(str(distance) + "/" + out_dr + "/" + str(gap) + "shifted_first_mixed_data_ploted.png", im_first_data)
        cv2.imwrite(str(distance) + "/" + out_dr + "/" + str(gap) + "shifted_second_mixed_data_ploted.png", im_second_data)
            






