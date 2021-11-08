# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import cv2
import numpy as np
import math
from my_demodulation_lib import on_off_judge_module
np.set_printoptions(threshold=np.inf) # 配列の中身を省略せずに全部表示。     

shifted = 45

x_list=[]
y_list=[]
full_signal = cv2.imread("Gap_images" + "/" + "0shiftedOnOff" + ".png", 1) #画像入力
shifted_signal = cv2.imread("Gap_images" + "/" + str(shifted) + "shiftedOnOff" + ".png", 1)
shifted_signal2 = cv2.imread("Gap_images" + "/" + str(shifted) + "shiftedOffOn" + ".png", 1)
colored_signal = shifted_signal.copy()
corrected_signal = shifted_signal2.copy()
full_signal_gray = cv2.cvtColor(full_signal, cv2.COLOR_BGR2GRAY)
shifted_signal_gray = cv2.cvtColor(shifted_signal, cv2.COLOR_BGR2GRAY)
height, width, channel = shifted_signal.shape

threshold, binary_Full = cv2.threshold(full_signal_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
threshold, binary_Shifted = cv2.threshold(shifted_signal_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
f_nLabels, f_labelImages, f_data, f_center = cv2.connectedComponentsWithStats(binary_Full) #ラベリング
s_nLabels, s_labelImages, s_data, s_center = cv2.connectedComponentsWithStats(binary_Shifted) #ラベリング
#ずれ角度
gap_Float_On = 360 * s_data[1,4] / f_data[1,4] # onの信号の角度範囲
gap_Float_Off = 360 - gap_Float_On # offの信号の角度範囲
gap_Int = round(gap_Float_Off)
gap_Rad = math.radians(gap_Int)
#半径
r = round(f_data[1,2] / 2) +1
#傾き
a = -(math.sin(gap_Rad) / math.cos(gap_Rad)) # 二次元画像空間の事象は普通と逆なのでずれ直線の傾きはマイナスにする
#切片
#欠落部の座標取得と合成部の色付け
b = f_center[1,1] - a * f_center[1,0]
for x in range (0, width):
    for y in range (0, height):
        if gap_Int <= 180:
            if (x - f_center[1,0])**2 + (y - f_center[1,1])**2 <= r**2 and x >= f_center[1,0]  and y < a * x + b:
                x_list.append(x)
                y_list.append(y)
                colored_signal[y,x] = (0, 255, 0)
        if 180 < gap_Int <= 360:
            if ((x - f_center[1,0])**2 + (y - f_center[1,1])**2 <= r**2) and (x >= f_center[1,0] or  y > a * x + b):
                x_list.append(x)
                y_list.append(y)
                colored_signal[y,x] = (0, 255, 0)
                
#画像合成
for add in range (0, len(x_list)):
        corrected_signal[y_list[add], x_list[add]] = shifted_signal[y_list[add], x_list[add]]

      
cv2.imshow("shifted_signal", shifted_signal)
cv2.imshow("colored_signal", colored_signal)
cv2.imshow("shifted_signal2", shifted_signal2)
cv2.imshow("corrected_signal", corrected_signal)

          
cv2.imwrite("shifted_signal.png", shifted_signal)
cv2.imwrite("colored_signal.png", colored_signal)
cv2.imwrite("shifted_signal2.png", shifted_signal2)
cv2.imwrite(str(shifted) + "corrected_signal.png", corrected_signal)

 

cv2.waitKey(0)
cv2.destroyAllWindows()

#cv2.imwrite(")