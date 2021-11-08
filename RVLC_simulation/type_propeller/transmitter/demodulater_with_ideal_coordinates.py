# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import cv2
import numpy as np
import math
import pprint
import csv
import copy
from mylib import type_propeller as tpp
from mylib import mymodules as mm

input_dir = "../transmitter"
header_dir = "header_part"
data_dir = "data_part"
coordinate_dir = "coordinate"
signal_dir = "transmitted_signal"
mixed_signal_dir = "mixed_signal"


#画像入力
im_all_light = cv2.imread(input_dir + str(distance + ))
