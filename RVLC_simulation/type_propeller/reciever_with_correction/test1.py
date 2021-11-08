# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 17:31:09 2021

@author: arailab
"""
import math
codn_x_ln_list1d = [10,20,30,40,41,50,60,70,80,90]
codn_y_ln_list1d = [10,20,30,40,41,50,60,70,80,90]
while len(codn_x_ln_list1d) > 9:
    for n in range(0, len(codn_x_ln_list1d)-1):
        print("n",n)
        diff = math.sqrt((codn_x_ln_list1d[n+1] - codn_x_ln_list1d[n])**2 +(
                         codn_y_ln_list1d[n+1] - codn_y_ln_list1d[n])**2)
        if diff <= 2:
            del codn_x_ln_list1d[n+1]
            del codn_y_ln_list1d[n+1]
            break