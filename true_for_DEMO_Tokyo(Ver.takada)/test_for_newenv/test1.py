# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 10:40:03 2019

@author: akinori
"""
import cv2
import numpy as np
import random
import copy
from my_demodulation_lib import erosion_dilaition_module
from my_demodulation_lib import cordinate_coloring_module

Input_img = cv2.imread("src.png",1)
Img_src = cv2.cvtColor(Input_img, cv2.COLOR_BGR2GRAY)
height, width = Img_src.shape[:2]
label_coloring = copy.copy(Img_src)
color_pallette = (0 , 255, 0)

gamma = 0.1
Img_max = Img_src.max()
Img_gamma = Img_max * (Img_src / Img_max) ** (1 / gamma)
cv2.imwrite("Img_gamma.png", Img_gamma)

bin_threshold, Img_binari = cv2.threshold(Img_src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
cv2.imwrite("Img_bin.png", Img_binari)

eroded_dilated_Img = erosion_dilaition_module.erosion_dilation(Img_binari, 8, 8) #収縮膨張処理
cv2.imwrite("eroded_dilated_Img.png", eroded_dilated_Img)


labelnum, labelimg, contours, GoCs = cv2.connectedComponentsWithStats(eroded_dilated_Img) #ラベリング
GoCs = np.delete(GoCs, 0, 0) #line_GoCsの0行目を削除
GoCs = np.round(GoCs) # 座標を四捨五入
GoCs = GoCs.astype(np.int) # int型に変換
"""
colors = []
for i in range(1, labelnum + 1):
    colors.append(np.array([random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]))

for y in range(0, height):
    for x in range(0, width):
        if labelimg[y, x] > 0:
            label_coloring[y, x] = colors[labelimg[y, x]]
        else:
            label_coloring[y, x] = [0, 0, 0]
"""

 # 取得した座標でcapture_imgに色を付けてる
cordinate_coloring = Input_img
for o in range (0, len(GoCs[:,0])):
    cordinate_coloring[GoCs[:,0],GoCs[:,1]] = (0, 0, 250)
cv2.imwrite("cordinate_coloring.png", cordinate_coloring); # 処理結果の保存

print(len(GoCs[:,0]))
                
cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()