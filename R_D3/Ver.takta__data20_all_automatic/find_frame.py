# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:39:20 2019

@author: akinori
"""
import cv2
import numpy as np


def find_all_frame_cordinate(img_frame):
    img_frame_gray = cv2.cvtColor(img_frame, cv2.COLOR_BGR2GRAY)
    frame_threshold, img_binari_frame = cv2.threshold(img_frame_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    frame_labelnum, frame_labelimg, frame_contours, frame_GoCs = cv2.connectedComponentsWithStats(img_binari_frame)
    return frame_contours, frame_GoCs


def sort_frame_cordinate_by_area(frame_contours, frame_GoCs):
    frame_area = frame_contours[:, 4]
    sorted_index_by_area = np.argsort(-frame_area)
    sorted_frame_GoCs_by_area = frame_GoCs[sorted_index_by_area]
    return sorted_frame_GoCs_by_area


def get_true_frame_cordinate(sorted_frame_GoCs_by_area, LED_numbers):
    neccesary_frame_GoCs = sorted_frame_GoCs_by_area[0:LED_numbers * 2 - 1, :]
    x = neccesary_frame_GoCs[:, 0]
    y = neccesary_frame_GoCs[:, 1]
    frame_xmin_index = np.argmin(x)
    frame_ymim_index = np.argmin(y)
    frame_xmax_index = np.argmax(x)
    frame_ymax_index = np.argmax(y)

    frame_xmin = neccesary_frame_GoCs[frame_xmin_index, 0]
    frame_ymin = neccesary_frame_GoCs[frame_ymim_index, 1]
    frame_xmax = neccesary_frame_GoCs[frame_xmax_index, 0]
    frame_ymax = neccesary_frame_GoCs[frame_ymax_index, 1]
    return int(frame_xmin), int(frame_ymin), int(frame_xmax), int(frame_ymax)
