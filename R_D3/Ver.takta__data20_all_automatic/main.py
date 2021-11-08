# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 22:39:16 2019

@author: akinori
"""
import cv2
import numpy as np
import find_heada
import find_trans_posi
import find_frame
"""
from find_cordinate import FIND_CORDINATE
from calcu_judge_threshold import CALCU_JUDGE_THRESHOLD
from demodulation import DEMODULATION
"""
c = 1
img_writed = 0
heada_numbers = 4
heada1 = 0
LED_numbers = 9
communication_start = False
delay = 100
number_of_a_protcol = 26
frame_count = 0
data_count = 1
frame_t0 = 0
frame_t1 = 0
frame_t2 = 0
frame_t3 = 0
best_sum_values = {'0.5m': 0,
                   '1.0m': 709139,
                   '1.5m': 0,
                   '2.0m': 0,
                   '2.5m': 0,
                   '3.0m': 0,
                   '3.5m': 0,
                   '4.0m': 0}

cap_file = cv2.VideoCapture('1.0m_f10.avi')
#cap_file = cv2.VideoCapture(1)
#cap_file.set(cv2.CAP_PROP_FPS, 5)           # カメラFPSを60FPSに設定
#cap_file.set(cv2.CAP_PROP_FRAME_WIDTH, 1600) # カメラ画像の横幅を1280に設定
#cap_file.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200) # カメラ画像の縦幅を720に設定
if not cap_file.isOpened():
    print('動画が読み込めないよ!!!!!!!!!')

while True:
    print(frame_count)
    if frame_count >= 1:
        frame_t2 = frame_t3
    if frame_count >= 2:
        frame_t1 = frame_t2
    if frame_count >= 3:
        frame_t0 = frame_t1
    ret, frame_t3 = cap_file.read()
    print(data_count)

    if ret:
        cv2.imshow('simple_img', frame_t3)

        if frame_count >= 1:
            if communication_start == False:
                img_mask = find_trans_posi.make_mask(frame_t3, frame_t2)
                Ex_sum_value = find_heada.get_heada_vlue(frame_t3, frame_t2, img_mask)
                for best_sum_value_key in best_sum_values:
                    diffrence_ratio = best_sum_values[best_sum_value_key] / Ex_sum_value
                    if 0.7 <= diffrence_ratio <= 1.3:
                        print('最大比', diffrence_ratio)
                        communication_start = True
                        print('通信スタート！！！！！！！！！！！')

            if communication_start == True and data_count >= 3:
                if not type(heada1) is np.ndarray:
                    heada1 = frame_t0
                    heada2 = frame_t1
                    heada3 = frame_t2
                    heada4 = frame_t3
                    frame_contours, frame_GoCs = find_frame.find_all_frame_cordinate(heada3)
                    sorted_frame_GoCs_by_area = find_frame.sort_frame_cordinate_by_area(frame_contours, frame_GoCs)
                    frame_xmin, frame_ymin, frame_xmax, frame_ymax = find_frame.get_true_frame_cordinate(sorted_frame_GoCs_by_area, LED_numbers)
                    #print('a', frame_xmin, frame_ymin, frame_xmax, frame_ymax)
                img_writed = cv2.rectangle(frame_t3, (frame_xmin, frame_ymin), (frame_xmax, frame_ymax), (0, 255, 0),3)
                print('img_writedの型', type(img_writed))
                #cv2.imshow('heada3' + str(c), heada3)
                #c += 1
                
                if type(img_writed) is np.ndarray:
                    cv2.imshow('img_writed', img_writed)

        if communication_start == True:
            data_count += 1
    if data_count > number_of_a_protcol:
        communication_start = False
        data_count = 1
        heada1 = 0
        heada2 = 0
        heada3 = 0
        heada4 = 0
        img_writed = 0
    frame_count += 1

    k = cv2.waitKey(delay)
    if k == 27:
        break
cap_file.release()
cv2.destroyAllWindows()
