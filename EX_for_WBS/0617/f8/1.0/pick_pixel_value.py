# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:47:00 2019

@author: akinori
"""

import cv2
import glob
import numpy as np


data_dir = "data"
data_path = glob.glob(data_dir + '/*')

coordinate_by_header3_array = np.loadtxt(
        fname = "coordinate_by_header3.csv",
        dtype = "int",
        delimiter = ","
        )


picked_pixel_value_by_header3 = np.array([0])
picked_pixel_value_by_header4 = np.array([0])

for input_file_name in data_path:
    img_data = cv2.imread(input_file_name, 0)
    for i in range(0, len(coordinate_by_header3_array)):
        xcoordinate_by_header3 = coordinate_by_header3_array[i,0]
        ycoordinate_by_header3 = coordinate_by_header3_array[i,1]
        picked_pixel_value_by_header3 = np.append(picked_pixel_value_by_header3,img_data[ycoordinate_by_header3,xcoordinate_by_header3])

picked_pixel_value_by_header3 = np.delete(picked_pixel_value_by_header3,0,0)
np.savetxt("picked_pixel_value_by_header3.csv", picked_pixel_value_by_header3 ,fmt="%d", delimiter=",")
