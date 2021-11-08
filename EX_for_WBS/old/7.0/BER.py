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

import cv2
import numpy as np
import csv
import copy
import random
import sys
np.set_printoptions(threshold=np.inf) # 配列の中身を省略せずに全部表示。        

# 全復調値をｃｓｖから入力
all_demodulation_value = np.loadtxt(
        fname = "all_demodulation_value.csv",
        dtype = "int",
        delimiter = ","
        )
print ("all_demodulation_value",all_demodulation_value)


 # 全答えをｃｓｖから入力
all_data_answer = np.loadtxt(
        fname = "all_data_answer.csv",
        dtype = "int",
        delimiter = ","
        )
print ("all_data_answer",all_data_answer)
print (all_data_answer.shape)


#Ber 計算
k=0
for m in range (all_data_answer.shape[0]):
    for n in range (all_data_answer.shape[1]):
        if all_data_answer[m][n] == all_demodulation_value[m][n]: # 正解と復調した値が正しいならば（an[0][0]が一列目の最初の値、[0][1]が次の値、[1][0]が二列目の最初の値）
            k = k # 復調値と正解があっていればｋに入っている値を代入
        else:
            k = k + 1 # 間違っていればｋの値に＋１
Ber = k / (all_data_answer.size) # 復調値の配列内が間違っている確率
print("エラー数",k)
print("BER",Ber)

    
    
    
    
 