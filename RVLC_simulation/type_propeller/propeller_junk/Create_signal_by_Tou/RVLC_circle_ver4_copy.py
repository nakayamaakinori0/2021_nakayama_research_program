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
import random
import copy
#np.set_printoptions(threshold=np.inf) # 配列の中身を省略せずに全部表示。     

shift_degree = 0


height = 1200
width = 1600


#配列設定
empty_image = np.zeros((height, width, 3), np.uint8)
#print(image)

#円の中心
c = [width/2,height/2]
#max_r = 0.016
#最大半径
max_r = 0.061
#最小半径
min_r = 0.045
#焦点距離
f = 0.035
#通信距離
d = 1.0
#ピクセルサイズ
pz = 0.0000045
#LEDの数
ln = 9
#半径算出
rp = []
for i in range (0, ln, 1):
    r = max_r - (max_r-min_r)/ln*i
    rp.append(round(r*f/d/pz))
    print (r*f/d/pz)
#回転角度
shita = 360
multiple = 10 # 0.1度毎で軌跡座標作る用
gap = 45

u_list = []
v_list = []
u_list_m = []
v_list_m = []

shifter = 45

def GetCenter(shita,Radius,Center,PixlSz):
    u_list = []
    v_list = []
    for D in range (0, shita, 1):
        radian = math.radians(D)
        u_list.append(round(Radius * math.sin(radian) + Center[0]))
        v_list.append(round(-Radius * math.cos(radian) + Center[1]))
    return u_list, v_list
    
def GetLine(shita,Radius,Center,multiple,PixlSz):
    
    u_list_multiple = []
    v_list_multiple = []
    for D in range (0, shita, 1):
        u_list = []
        v_list = []
        for d in range (0, multiple, 1):
            radian = math.radians(D+(d/10))
            u_list.append(round(Radius * math.sin(radian) + Center[0]))
            v_list.append(round(-Radius * math.cos(radian) + Center[1]))
        u_list_multiple.append(u_list)
        v_list_multiple.append(v_list)
    return u_list_multiple, v_list_multiple
    

def MakeData_random (LED_number):
    Random_data_list = []
    # N個のLEDのDataのまとめ
    LED_num = LED_number
    for N in range (LED_num):
        if N == 0:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 1:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 2:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 3:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 4:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 5:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 6:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 7:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
        elif N == 8:
            Data = []
            for x in range (360):
                data = random.randint(0, 1)
                Data.append(data)
            Random_data_list.append(Data)
    
    return Random_data_list


def MakeLightData(EmptyImage,Random_data_list,u_list_multiple, v_list_multiple):
    Image = copy.copy(EmptyImage)
    for n in range (0, len(u_list_multiple), 1): # ０～８
        for D in range (0, len(u_list_multiple[0]), 1): # ０～３５９
            if D >= shifter:
                if Random_data_list[n][D] == 1:
                    for d in range (0, len(u_list_multiple[0][0]), 1): # 0~9
                        Image[u_list_multiple[n][D][d], v_list_multiple[n][D][d]] = (255, 255, 255)
                else:
                    for d in range (0, len(u_list_multiple[0][0]), 1):
                        Image[u_list_multiple[n][D][d], v_list_multiple[n][D][d]] = (0, 0, 0)
    return Image

def MakeLightAll(EmptyImage,u_list_multiple, v_list_multiple):
    Image = copy.copy(EmptyImage)
    for n in range (0, len(u_list_multiple), 1):
        for D in range (0, len(u_list_multiple[0]), 1):
            if D >= shifter: 
                for d in range (0, len(u_list_multiple[0][0]), 1):
                    Image[v_list_multiple[n][D][d], u_list_multiple[n][D][d]] = (255, 255, 255)
    return Image

#def Exlight():

def main():

    for i in range (0,ln,1):
        u, v = GetCenter(shita,rp[i],c,pz)
        U, V = GetLine(shita,rp[i],c,multiple,pz)
        u_list.append(u)
        v_list.append(v)
        u_list_m.append(U)
        v_list_m.append(V)
    #print(len(u_list_m))

    data_list = MakeData_random(ln)
    data_image = MakeLightData(empty_image,data_list,u_list_m,v_list_m)
    all_light_image = MakeLightAll(empty_image,u_list_m,v_list_m)
    
    pil_img1 = Image.fromarray(all_light_image)
    filename1 = str(shift_degree) + 'shited.png'
    pil_img1.save(filename1)
    pil_img2 = Image.fromarray(data_image)
    filename2 = 'randomdata.png'
    pil_img2.save(filename2)
    
    #print (u_list_m)
    #print (data_list)
if __name__ == '__main__':
    main()

"""
u_listm = np.zeros((360, 1), np.uint8)
print(u_listm)
for m in range (360):
    for n in range (10):
        u_listm[m].append(U_list[n])
    n = n + 10
"""
