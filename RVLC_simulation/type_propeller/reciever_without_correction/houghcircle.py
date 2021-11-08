# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 08:50:19 2021

@author: frees
"""
import cv2
import numpy as np
from IPython.display import Image, display
from matplotlib import pyplot as plt
from mylib import type_propeller as tpp


def imshow(img):
    """ndarray 配列をインラインで Notebook 上に表示する。
    """
    ret, encoded = cv2.imencode(".png", img)
    display(Image(encoded))

tras_dr = "../transmitter"
head_dr = "heada_part"
data_dr = "data_part"
t_codn_dr = "coordinate"
r_codn_dr =  "result_coordinate"
t_sig_dr = "transmitted_signal"
t_sigm_dr = "mixed_signal"
r_sigm_dr = "result_pv"
out_dr = "error_plot"
distance = 1.0
gap = 0
# 画像を読み込む。
img = cv2.imread(tras_dr + "/" + str(distance) + "/" + head_dr + "/" + str(gap) + "shifted_OnOff.png",1)
"""
# グレースケールに変換する。
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
binim = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# ハフ変換で円検出する。
circles = cv2.HoughCircles(
    gray, cv2.HOUGH_GRADIENT, dp=0.1, minDist=1000, param1=80, param2=100
    )
#print(circles)
circles=circles.squeeze(axis=0)
#circles=circles.squeeze(axis=0)
#center, radius = cv2.minEnclosingCircle(binim)
#print(circles.squeeze(axis=0))
# 検出結果を描画する。

if circles is not None:
    for cx, cy, r in circles.squeeze(axis=0).astype(int):
        # 円の円周を描画する。
        cv2.circle(img, (cx, cy), r, (0, 255, 0), 2)
        # 円の中心を描画する。
        cv2.circle(img, (cx, cy), 2, (0, 255, 0), 2)
"""
x, y = tpp.getCtr(img)
#imshow(img)

#cv2.imwrite("hough_converted.png",img)