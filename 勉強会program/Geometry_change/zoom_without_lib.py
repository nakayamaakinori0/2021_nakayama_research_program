# -*- coding: utf-8 -*-


import cv2
import glob
import os
import numpy as np
import csv
from operator import itemgetter

input_img = cv2.imread("src.png", 1)
width, height, chanel = input_img.shape

zoomed_img = input_img.repeat(3, axis=0).repeat(3,axis=1)

cv2.imshow("input_img", input_img)
cv2.imshow("zoomed_img", zoomed_img)

cv2.imwrite("zoomed_img_withour_lib.png",zoomed_img)


cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
