# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:47:00 2019

@author: akinori
"""

import cv2
import numpy as np
from my_demodulation_lib import on_off_judge_module
np.set_printoptions(threshold=np.inf) # 配列の中身を省略せずに全部表示。        
#np.set_printoptions(linewidth = 57) # 配列の中身を省略せずに全部表示。        
str_singo = []
cap_file = cv2.VideoCapture(1)
#cap_file.set(cv2.CAP_PROP_FPS, 5)           # カメラFPSを60FPSに設定
cap_file.set(cv2.CAP_PROP_FRAME_WIDTH, 1600) # カメラ画像の横幅を1280に設定
cap_file.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200) # カメラ画像の縦幅を720に設定

cordinate_x = np.loadtxt(
        fname = "cordinate_x.csv",
        dtype = "int",
        delimiter = ","
        )

cordinate_y = np.loadtxt(
        fname = "cordinate_y.csv",
        dtype = "int",
        delimiter = ","
        )

judge_threshold_arr = np.loadtxt(
        fname = "judge_threshold.csv",
        dtype = "float",
        delimiter = ","
        )

while True:
    ret, frame = cap_file.read()
    frame = cv2.flip(frame, -1)
    cv2.imshow('Raw Frame', frame)
    if ret:
        singo = on_off_judge_module.on_off_judge(frame[:,:,2],cordinate_x, cordinate_y, judge_threshold_arr)
        print("\n")
        for cols in range(singo.shape[0]):
            print(''.join(singo[cols]))
            
            

                
        
    #print(singo)
    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break
# キャプチャをリリースして、ウィンドウをすべて閉じる
cap_file.release()
cv2.destroyAllWindows()
