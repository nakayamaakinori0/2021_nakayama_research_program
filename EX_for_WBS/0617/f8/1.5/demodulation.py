# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 05:11:38 2021

@author: akinori
"""

import numpy as np
import copy
from mylib import mymodules as mm
import csv
d_length = 60
ln = 9
d_range = 57
picked_pixel_value_by_header3 = np.loadtxt(
        fname = "picked_pixel_value_by_header3.csv",
        dtype = "int",
        delimiter = ","
        )


judge_threshold_by_header3_array = np.loadtxt(
        fname = "judge_threshold_arr_by_header3.csv",
        dtype = "int",
        delimiter = ","
        )

demodulated_value_by_header3 = np.array([0])
for i in range (0, d_length):
    for l in range(0, ln * d_range):
        if picked_pixel_value_by_header3[l+513*i] >= judge_threshold_by_header3_array[l]:
            demodulated_value_by_header3 = np.append(demodulated_value_by_header3, 1)
        if picked_pixel_value_by_header3[l+513*i] < judge_threshold_by_header3_array[l]:
            demodulated_value_by_header3 = np.append(demodulated_value_by_header3, 0)
demodulated_value_by_header3 = np.delete(demodulated_value_by_header3,0,0)

np.savetxt("recieved_signal_by_header3.csv",demodulated_value_by_header3, fmt = "%d", delimiter = ",")


            
