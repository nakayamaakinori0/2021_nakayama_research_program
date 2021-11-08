# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:32:45 2021

@author: akinori
"""

import numpy as np
import copy

initial_value = np.array([0,1,0,1,0,1,0,1,0,1,0,1])
initial_posi = np.array([0,3,5,11])
array1 = copy.deepcopy(initial_value)
answer_array = copy.deepcopy(initial_value[0:9])
for l in range(0, 57*19):# 出来上がるアレーなぜか１パケット（１２）多い
    insert_array = copy.deepcopy(array1[0+12*(l):11+12*(l)])
    if (array1[initial_posi[0]+12*l] + array1[initial_posi[1]+12*l] + array1[initial_posi[2]+12*l] + array1[initial_posi[3]+12*l]) % 2 == 0:
        array1 = np.append(array1, 0)
    if (array1[initial_posi[0]+12*l] + array1[initial_posi[1]+12*l] + array1[initial_posi[2]+12*l] + array1[initial_posi[3]+12*l]) % 2 == 1:
        array1 = np.append(array1, 1)
    if l == 0:
        array1 = np.append(array1, initial_value[0:11])
    if l != 0:
        array1 = np.append(array1,insert_array)
for i in range(1, 19*57):
        answer_array = np.append(answer_array, array1[0+12*i:9+12*i])

np.savetxt("answer_array.csv",answer_array, fmt="%d", delimiter=",")