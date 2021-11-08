# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 16:07:01 2020

@author: Arailab
"""

from PIL import Image
import numpy as np
import cv2
import math
import sympy as sp

hight = 540
width = 540

#配列設定
image =np.zeros((hight, width, 3), np.uint8)

#円の中心
a = 270
b = 270
O = (a, b)

#半径r
r = 100

#回転角度
shita = 360
shita2 = 3600
U_list = []
V_list = []
for D in range (0, shita2, 1):
    d = D/10
    d = math.radians(d)
    U = r * math.sin(d) + a
    V = -r * math.cos(d) + b
    U_list.append(round(U))
    V_list.append(round(V))

for j in range (len(V_list)):
    V_j = V_list[j]
    U_j = U_list[j]
    image[V_j, U_j] = (255, 255, 255)


#回転角度C
v_list = []
u_list = []
for C in range (0, shita, 10):
    c = math.radians(C)
    u = r * math.sin(c) + a
    v = -r * math.cos(c) + b
    u_list.append(round(u))
    v_list.append(round(v))
    #print(C)
    #print(u)
print(v_list[:9])
print(u_list[:9])

for i in range (len(v_list)):
    v_i = v_list[i]
    u_i = u_list[i]
    image[v_i, u_i] = (255, 0, 0)

pil_img = Image.fromarray(image)
filename = f'./image.png'
pil_img.save(filename)

