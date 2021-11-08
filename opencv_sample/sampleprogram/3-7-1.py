# -*- coding: utf-8 -*-
import cv2
import math
import numpy as np

file_src = 'src.png'
file_dst = 'dst.png'

img_src = cv2.imread(file_src, 1)
b,g,r = img_src[10, 20] #(y座標, x座標)
print(b,g,r)

img_src[30, 50] = [0, 0, 255] #Blue Green Red の順番

cv2.line(img_src, (10, 10), (100, 200), (255, 255, 0), 5)

cv2.circle(img_src, (100, 150), 10, (255, 0, 255), 3)

cv2.circle(img_src, (150, 100), 20, (255, 0, 255), -1)

cv2.rectangle(img_src, (200, 200), (250, 250), (0, 255, 255), 3)

cv2.rectangle(img_src, (200, 300), (250, 350), (0, 255, 255), -1)

fontType = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img_src, "12345", (300, 100), fontType, 1, (255, 255, 255), 2)


cv2.namedWindow('src')
cv2.namedWindow('dst')

# ここに核となる処理を記述する
img_dst = cv2.flip(img_src, flipCode = 0) # 垂直反転

h, w, ch = img_dst.shape
img_dst = cv2.resize(img_dst, (int(h/2), int(w/2)))
                  
h, w, ch = img_dst.shape
img_dst2 = img_dst[0:int(h/2), 0:w] #上半分

cv2.imshow('dst2', img_dst2) #img_dst2を表示

cv2.imshow('src', img_src) # 入力画像を表示
cv2.imshow('dst', img_dst) # 出力画像を表示
cv2.imwrite(file_dst, img_dst) # 処理結果の保存

cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
