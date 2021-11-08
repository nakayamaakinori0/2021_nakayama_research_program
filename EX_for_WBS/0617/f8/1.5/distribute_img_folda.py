# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:47:42 2019

@author: akinori
"""
import cv2
from mylib import mymodules as mm


# 入力ディレクトリ
input_dir = "capture_img"
header1_dir = "header1"
header2_dir = "header2"
header3_dir = "header3"
footer_dir = "footer"
protocol_frame = [2,1,10,60,2]
trimming_heada2_dir = "trimming_header2"
data_dir = "data"

list_input_img = mm.img_to_list(input_dir, 0, 75, 1)


for i in range(0, len(list_input_img)):
    #print(list_Img[i])
    if i < sum(protocol_frame[:1]):
        cv2.imwrite(header1_dir+'/'+str(i)+ '.png', list_input_img[i])
    elif i < sum(protocol_frame[:2]):
        cv2.imwrite(header2_dir+'/'+str(i)+ '.png', list_input_img[i])
    elif i < sum(protocol_frame[:3]):
        cv2.imwrite(header3_dir+'/'+str(i)+ '.png', list_input_img[i])
    elif i < sum(protocol_frame[:4]):
        cv2.imwrite(data_dir+'/'+str(i)+ '.png', list_input_img[i])
    elif i < sum(protocol_frame[:5]):
        cv2.imwrite(footer_dir+'/'+str(i)+ '.png', list_input_img[i])
    

        

