# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:32:45 2021

@author: akinori
"""

import numpy as np
import copy

ini_v = np.array([0,1,0,1,0,1,0,1,0,1,0,1])
vs = len(ini_v)
ini_p = np.array([0,3,5,11])
ln = 9
d_range = 57
d_length = 60
source_arr = copy.deepcopy(ini_v)
signal_arr = copy.deepcopy(ini_v[0:ln])
for l in range(0, d_range*d_length):# 出来上がるアレーなぜか１パケット（１２）多い
    insert_array = copy.deepcopy(source_arr[0+vs*l:(vs-1)+vs*l])
    jv = np.array([source_arr[ini_p[0]+vs*l],source_arr[ini_p[1]+vs*l],source_arr[ini_p[2]+vs*l],source_arr[ini_p[3]+vs*l]])
    if (np.sum(jv)) % 2 == 0:
        source_arr = np.append(source_arr, 0)
    if (np.sum(jv)) % 2 == 1:
        source_arr = np.append(source_arr, 1)
    if l == 0:
        source_arr = np.append(source_arr, ini_v[0:vs-1])
    if l != 0:
        source_arr = np.append(source_arr,insert_array)
for i in range(1, d_length*d_range):
        signal_arr = np.append(signal_arr, source_arr[0+vs*i:ln+vs*i])

np.savetxt("transmitted_signal_arr.csv",signal_arr, fmt="%d", delimiter=",")