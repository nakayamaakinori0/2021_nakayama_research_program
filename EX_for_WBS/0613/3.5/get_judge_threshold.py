# -*- coding: utf-8 -*-
"""
Created on Sun Jun 13 23:41:29 2021

@author: akinori
"""

import cv2
import numpy as np

header1_dir = "header1"
header3_dir = "header3"
header4_dir = "header4"
footer_dir = "footer"
header3_trimmed_dir = "header3_trimmed"
header4_trimmed_dir = "header4_trimmed"
data_dir = "data"
# 出力ディレクトリ
eroded_dilated_dir = "eroded_dilated"
coloring_dir = "coloring"
np.set_printoptions(threshold=np.inf)


judge_threshold_by_header3_array = np.array([0], dtype="int32")
judge_threshold_by_header4_array = np.array([0], dtype="int32")
header1_1 = cv2.imread(header1_dir + "/0.png",0)
header1_2 = cv2.imread(header1_dir + "/1.png",0)
header1_1 = header1_1.astype('int32')
header1_2 = header1_2.astype('int32')

coordinate_by_header3_array = np.loadtxt(
        fname = "coordinate_by_header3.csv",
        dtype = "int",
        delimiter = ","
        )

coordinate_by_header4_array = np.loadtxt(
        fname = "coordinate_by_header4.csv",
        dtype = "int",
        delimiter = ","
        )

for i in range (0, len(coordinate_by_header3_array)):
    xcoordinate_by_header3 = coordinate_by_header3_array[i,0]
    ycoordinate_by_header3 = coordinate_by_header3_array[i,1]
    xcoordinate_by_header4 = coordinate_by_header4_array[i,0]
    ycoordinate_by_header4 = coordinate_by_header4_array[i,1]
    #print(header1_1[ycoordinate_by_header3,xcoordinate_by_header3]-header1_2[ycoordinate_by_header3,xcoordinate_by_header3])
    judge_threshold_by_header3_array = np.append(judge_threshold_by_header3_array,
                                                 (header1_1[ycoordinate_by_header3,xcoordinate_by_header3] 
                                                 + header1_2[ycoordinate_by_header3,xcoordinate_by_header3])/2)
    judge_threshold_by_header4_array = np.append(judge_threshold_by_header4_array,
                                                 (header1_1[ycoordinate_by_header4,xcoordinate_by_header4] 
                                                 + header1_2[ycoordinate_by_header4,xcoordinate_by_header4])/2)
judge_threshold_by_header3_array = np.delete(judge_threshold_by_header3_array,0,0)
judge_threshold_by_header4_array = np.delete(judge_threshold_by_header4_array,0,0)
np.savetxt("judge_threshold_arr_by_header3.csv", judge_threshold_by_header3_array, fmt="%d", delimiter=",")
np.savetxt("judge_threshold_arr_by_header4.csv", judge_threshold_by_header4_array, fmt="%d", delimiter=",")    
