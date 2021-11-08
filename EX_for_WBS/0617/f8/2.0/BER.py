# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 13:26:11 2018

@author: arailab
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 08:25:23 2018

@author: arailab
"""

import numpy as np
import copy
from mylib import mymodules as mm
import csv
np.set_printoptions(threshold=np.inf) # 配列の中身を省略せずに全部表示。        
num_data_part = 19
num_LED = 9
data_range = 57 

# 全復調値をｃｓｖから入力
recieved_signal_by_header3 = np.loadtxt(
        fname = "recieved_signal_by_header3.csv",
        dtype = "int",
        delimiter = ","
        )

 # 全答えをｃｓｖから入力
transmitted_signal = np.loadtxt(
        fname = "transmitted_signal_arr.csv",
        dtype = "int",
        delimiter = ","
        )
error_by_header3 = 0
for i in range(0, len(transmitted_signal)):
    if transmitted_signal[i] != recieved_signal_by_header3[i]:
        error_by_header3 += 1

BER_by_header3 = mm.culcBER(error_by_header3, num_data_part, num_LED, data_range)
print("BER_by_header3",BER_by_header3)
 