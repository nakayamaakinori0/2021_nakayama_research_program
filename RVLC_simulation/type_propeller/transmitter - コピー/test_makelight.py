# -*- coding: utf-8 -*-
"""
Created on Tue Mar  9 19:52:07 2021

@author: frees
"""

import csv
from PIL import Image
import numpy as np
import cv2
import math
import sympy as sp
import random
import copy


def GetLine(shita,multiple,Radius,initial_phase,center,):  
    u_list_multiple = []
    v_list_multiple = []
    for Degree in range (0, shita, 1):
        u_list = []
        v_list = []
        for d in range (0, multiple, 1):
            u_list.append(round(Radius * math.cos(math.radians((Degree+d/10)-90)) + center[0]))
            v_list.append(round(Radius * math.sin(math.radians((Degree+d/10)-90)) + center[1]))
        u_list_multiple.append(u_list)
        v_list_multiple.append(v_list)
    return u_list_multiple, v_list_multiple


def MakeLight(EmptyImage,u_list_multiple, v_list_multiple):
    Im = copy.copy(EmptyImage)
    for D in range (0, len(u_list_multiple), 1):
            for d in range (0, len(u_list_multiple[0]), 1):
                Im[v_list_multiple[D][d], u_list_multiple[D][d]] = (0, D/2, D/2)
    return Im

height = 2400
width = 2400
center= [1200,1200]
#配列設定
empty_image = np.zeros((height, width, 3), np.uint8)
x, y = GetLine(360,10,1000,90,center)
im = MakeLight(empty_image,x,y)
cv2.imwrite("test_makelight.png",im)

