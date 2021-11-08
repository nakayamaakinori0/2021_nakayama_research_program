# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 05:11:38 2021

@author: akinori
"""

import numpy as np
import copy
from mylib import mymodules as mm
import csv
picked_pixel_value_by_header3 = np.loadtxt(
        fname = "picked_pixel_value_by_header3.csv",
        dtype = "int",
        delimiter = ","
        )

picked_pixel_value_by_header4 = np.loadtxt(
        fname = "picked_pixel_value_by_header4.csv",
        dtype = "int",
        delimiter = ","
        )

judge_threshold_by_header3_array = np.loadtxt(
        fname = "judge_threshold_arr_by_header3.csv",
        dtype = "int",
        delimiter = ","
        )

judge_threshold_by_header4_array = np.loadtxt(
        fname = "judge_threshold_arr_by_header4.csv",
        dtype = "int",
        delimiter = ","
        )
demodulated_value_by_header3 = np.array([0])
demodulated_value_by_header4 = np.array([0])
for i in range (0, 19):
    for l in range(0, 57*9):
        if picked_pixel_value_by_header3[l+513*i] >= judge_threshold_by_header3_array[l]:
            demodulated_value_by_header3 = np.append(demodulated_value_by_header3, 1)
        if picked_pixel_value_by_header3[l+513*i] < judge_threshold_by_header3_array[l]:
            demodulated_value_by_header3 = np.append(demodulated_value_by_header3, 0)
        if picked_pixel_value_by_header4[l+513*i] >= judge_threshold_by_header4_array[l]:
            demodulated_value_by_header4 = np.append(demodulated_value_by_header4, 1)
        if picked_pixel_value_by_header4[l+513*i] < judge_threshold_by_header4_array[l]:
            demodulated_value_by_header4 = np.append(demodulated_value_by_header4, 0)
demodulated_value_by_header3 = np.delete(demodulated_value_by_header3,0,0)
demodulated_value_by_header4 = np.delete(demodulated_value_by_header4,0,0)

np.savetxt("recieved_signal_by_header3.csv",demodulated_value_by_header3, fmt = "%d", delimiter = ",")
np.savetxt("recieved_signal_by_header4.csv",demodulated_value_by_header4, fmt = "%d", delimiter = ",")


            
