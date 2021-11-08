# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:16:07 2019

@author: akinori
"""

import cv2
import math
import numpy as np

input_img = cv2.imread("src.png", 1)
width, height, chanel = input_img.shape

size = tuple(np.array([width,height]))

afn_mat = np.float32([[math.cos(45), math.sin(45), ((1-math.cos(45))*width/2)-(math.sin(45)*height/2)],
                      [-math.sin(45), math.cos(45), ((math.sin(45)*width/2)+(1-math.cos(45))*height/2)+100]])#変換行列

output_img = cv2.warpAffine(input_img, afn_mat, size, flags = cv2.INTER_LINEAR)
#(入力画像、変換行列、出力画像のサイズ、補間方法)
"""
補間方法
cv2.INTER_NEAREST: 最近傍補間法
cv2.INTER_LINEAR: バイリニア補間
cv2.INTER_CUBIC: バイキュービック補間
cv2.INTER_AREA: ピクセル領域の関係を利用したリサンプリング
cv2.INTER_LANCZOS4: Lanczos法補間
"""

cv2.imshow("input_img", input_img)
cv2.imshow("output_img", output_img)

cv2.imwrite("test_affine_change.png",output_img)


cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
