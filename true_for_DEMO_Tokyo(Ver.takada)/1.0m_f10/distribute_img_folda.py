# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:47:42 2019

@author: akinori
"""
import cv2
import glob
import os
import numpy as np
import csv
from operator import itemgetter
from my_demodulation_lib import img_to_list_module


# 入力ディレクトリ
input_dir = "capture_img"
heada1_dir = "heada1"
heada2_dir = "heada2"
trimming_heada2_dir = "trimming_heada2"
data_dir = "data"

list_input_img = img_to_list_module.img_to_list(input_dir, 0, 71, 1)


for i in range(0, len(list_input_img)):
    #print(list_Img[i])
    if i == 0 or i == 1:
        cv2.imwrite(heada1_dir+'/'+str(i)+ '.png', list_input_img[i])
    elif i > 1 and i <= 11:
        cv2.imwrite(heada2_dir+'/'+str(i)+ '.png', list_input_img[i])
    elif i > 11 and i <= 71:
        cv2.imwrite(data_dir+'/'+str(i)+ '.png', list_input_img[i])

