# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 10:40:38 2020

@author: Arailab
"""
import random

def circle_data_random (LED_number):
    Random_data_list = []
    # N個のLEDのDataのまとめ
    LED_num = LED_number
    for N in range (LED_num):
        if N == 0:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 1:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 2:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 3:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 4:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 5:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 6:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 7:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 8:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
    
    return Random_data_list
#print(Data_list)
        