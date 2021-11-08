# -*- coding: utf-8 -*-
"""
Created on Wed Jun 12 10:17:39 2019

@author: akinori
"""

import cv2
import glob
import os
import numpy as np
import csv
from operator import itemgetter

def img_to_list(input_dir, start_no, end_no, chanel):
    input_path = glob.glob(input_dir + '/*')
    #if start_no is None:
    #    start_no = 0
    #if end_no is None:
    #    end_no = len(input_path)
    list_img = []
    count = start_no
    for input_file_name in input_path:
        if count <= end_no:
            Img_src = cv2.imread(input_dir + "/" + str(count) +".png", chanel)
            list_img.append(Img_src)
            count += 1
    return list_img