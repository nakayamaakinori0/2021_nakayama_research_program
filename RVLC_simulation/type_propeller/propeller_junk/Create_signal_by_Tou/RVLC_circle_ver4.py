# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:33:11 2020

@author: Arailab
"""


from PIL import Image
import numpy as np
import cv2
import math
import sympy as sp

np.set_printoptions(threshold=np.inf) # 配列の中身を省略せずに全部表示。     


shift_degree = 0


hight = 540
width = 540


#配列設定
image = np.zeros((hight, width, 3), np.uint8)
#print(image)

#円の中心
a = 270
b = 270
O = (a, b)

#半径r
r = 100

multiple = 10

#回転角度
shita = 360
shita2 = shita * multiple

U_list = []
V_list = []
for D in range (0, shita2, 1):
    d = D/10
    d = math.radians(d)
    U = r * math.sin(d) + a
    V = -r * math.cos(d) + b
    U_list.append(round(U))
    V_list.append(round(V))
#print(U_list[:20])
#print(V_list[:50])
print(len(V_list))
for j in range (len(V_list)):
    V_j = V_list[j]
    U_j = U_list[j]
    image[V_j, U_j] = (255, 255, 255)
print(image)


v_list = []
u_list = []
for C in range (0, shita, 1):
    c = math.radians(C)
    u = r * math.sin(c) + a
    v = -r * math.cos(c) + b
    u_list.append(round(u))
    v_list.append(round(v))
    #print(C)
    #print(u)
#print(v_list[:9])
#print(u_list[:10])

for i in range (len(v_list)):
    v_i = v_list[i]
    u_i = u_list[i]
    image[v_i, u_i] = (0, 0, 0)

pil_img = Image.fromarray(image)
filename = f'./image_ver4.png'
pil_img.save(filename)

#回転1度分の横ピクセル座標
U_list_m = []
start = 0
for n in range (shita):
    u_list_multiple = []
    for m in range (start, start + multiple, 1):
        u_list_multiple.append(U_list[m])
    U_list_m.append(u_list_multiple)
    start = start + multiple
    #print(u_list_multiple)
#print(U_list_m)
#print(len(U_list_m))

#回転1度分の縦ピクセル座標
V_list_m = []
start = 0
for n in range (shita):
    v_list_multiple = []
    for m in range (start, start + multiple, 1):
        v_list_multiple.append(V_list[m])
    V_list_m.append(v_list_multiple)
    start = start + multiple
    #print(u_list_multiple)
#print(V_list_m)
#print(len(V_list_m))

#data_listの例（360度のOn-OFF）
data_list = []
for y in range (360):
    if y >= shift_degree:
        #Y = y % 2
        Y = 1
    else:
        Y = 0
    data_list.append(Y)
#print(data_list)

for x in range (shita):
    if data_list[x] == 1:
        for p in range (multiple):
            v_m = V_list_m[x][p]
            u_m = U_list_m[x][p]
            image[v_m, u_m] = (255, 255, 255)
    else:
        for p in range (multiple):
            v_m = V_list_m[x][p]
            u_m = U_list_m[x][p]
            image[v_m, u_m] = (0, 0, 0)
        
pil_img = Image.fromarray(image)
filename = str(shift_degree) + 'degree_shifted.png'
#filename = str(shift_degree) + 'degree_shifted_offon.png'

pil_img.save(filename)         


"""
u_listm = np.zeros((360, 1), np.uint8)
print(u_listm)
for m in range (360):
    for n in range (10):
        u_listm[m].append(U_list[n])
    n = n + 10
"""