# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 10:33:11 2020

@author: Arailab
"""
######
#Ex
#getlzp
#CalcuBER
######
import csv
from PIL import Image
import numpy as np
import cv2
import math
import sympy as sp
import random
import copy
#np.set_printoptions(threshold=np.inf) # 配列の中身を省略せずに全部表示。     
height = 2400
width = 2400

#output_dir = "im"

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
#LEDの間隔
LED_interval = 0.0026
#焦点距離
f = 0.035
#通信距離
d_max = 10
d_min = 1.0
#d_list = list(np.arange(1.0,10.5,0.5))

d_list = [1.0,1.5,2.0,2.5,3.0,3.5,4.0,4.5,5.0,5.5,6.0,6.5,7.0,7.5,8.0,8.5,9.0,9.5,10.0]
#ピクセルサイズ
pz = 0.0000045
#LEDの発光部サイズ
lz = 0.000285714285714286


#LEDの数
ln = 9
    #print (r*f/d/pz)
#回転角度
shita = 360
shifter = 1
multiple = 10 # 0.1度毎で軌跡座標作る用

u_list = []
v_list = []
u_list_m = []
v_list_m = []

ini_phase = 90


def GetCenter(shita,Radius,initial_phase,center):
    u_list = []
    v_list = []
    for Degree in range (0, shita, 1):
        u_list.append(round(Radius * math.cos(math.radians(Degree-initial_phase)) + center[0]))
        v_list.append(round(Radius * math.sin(math.radians(Degree-initial_phase)) + center[1]))
    return u_list, v_list
def Get_signal_Center(shita,Radius,initial_phase,center):
    u_list = []
    v_list = []
    for Degree in range (0, shita, 1):
        u_list.append(round(Radius * math.cos(math.radians(Degree-initial_phase+0.5)) + center[0]))
        v_list.append(round(Radius * math.sin(math.radians(Degree-initial_phase+0.5)) + center[1]))
    return u_list, v_list
    
def GetLine(shita,multiple,Radius,initial_phase,center,):  
    u_list_multiple = []
    v_list_multiple = []
    for Degree in range (0, shita, 1):
        u_list = []
        v_list = []
        for d in range (0, multiple, 1):
            u_list.append(round(Radius * math.cos(math.radians((Degree+d/10)-initial_phase)) + center[0]))
            v_list.append(round(Radius * math.sin(math.radians((Degree+d/10)-initial_phase)) + center[1]))
        u_list_multiple.append(u_list)
        v_list_multiple.append(v_list)
    return u_list_multiple, v_list_multiple
def Modulate_random (LED_number):
    all_data_list = []
    # N個のLEDのDataのまとめ
    LED_num = LED_number
    for N in range (LED_num):
        data_list = []
        for D in range (360):
            data_list.append(random.randint(0,1))
        all_data_list.append(data_list)
    return all_data_list
def Modulate_onoff (LED_number, shifter):
    all_data_list = []
    # N個のLEDのDataのまとめ
    LED_num = LED_number
    for N in range (LED_num):
        data_list = []
        for D in range (360):
            if D < shifter:
                data_list.append(0)
            else:
                data_list.append(1)
        all_data_list.append(data_list)
    return all_data_list
def Modulate_offon (LED_number,shifter):
    all_data_list = []
    # N個のLEDのDataのまとめ
    LED_num = LED_number
    for N in range (LED_num):
        data_list = []
        for D in range (360):
            if D < shifter:
                data_list.append(1)
            else:
                data_list.append(0)
        all_data_list.append(data_list)
    return all_data_list
"""

def MakeLightData(EmptyImage,data_list,u_list_multiple, v_list_multiple):
    Image = copy.copy(EmptyImage)
    for n in range (0, len(u_list_multiple), 1): # ０～８
        for D in range (0, len(u_list_multiple[0]), 1): # ０～３５９
            if D >= shifter:
                if data_list[n][D] == 1:
                    for d in range (0, len(u_list_multiple[0][0]), 1): # 0~9
                        Image[v_list_multiple[n][D][d], u_list_multiple[n][D][d]] = (255, 255, 255)
                else:
                    for d in range (0, len(u_list_multiple[0][0]), 1):
                        Image[v_list_multiple[n][D][d], u_list_multiple[n][D][d]] = (0, 0, 0)
    return Image

def MakeLightFull_OnOff(EmptyImage,u_list_multiple, v_list_multiple,shifter):
    Image = copy.copy(EmptyImage)
    for n in range (0, len(u_list_multiple), 1):
        for D in range (0, len(u_list_multiple[0]), 1):
            if D >= shifter:
                for d in range (0, len(u_list_multiple[0][0]), 1):
                    Image[v_list_multiple[n][D][d], u_list_multiple[n][D][d]] = (255, 255, 255)
    return Image

def MakeLightFull_OffOn(EmptyImage,u_list_multiple, v_list_multiple,shifter):
    Image = copy.copy(EmptyImage)
    for n in range (0, len(u_list_multiple), 1):
        for D in range (0, len(u_list_multiple[0]), 1):
            if D < shifter:
                for d in range (0, len(u_list_multiple[0][0]), 1):
                    Image[v_list_multiple[n][D][d], u_list_multiple[n][D][d]] = (255, 255, 255)
    return Image
"""

def Exlight(data_list, LEDSizeOnIm, u_list_multiple, v_list_multiple, inputIm):
        ######重み付け　光広がりカーネル
    a = copy.copy(LEDSizeOnIm)
    #print(LEDSizeOnIm)
    #LEDSizeOnIm = math.ceil(LEDSizeOnIm)
    LEDSizeOnIm = 2

    #print(LEDSizeOnIm)
    weight = a - int(a)
    #print(weight)
    if a > 1:
        if LEDSizeOnIm % 2 == 1:
            k_size = LEDSizeOnIm #光の広がりサイズ
            expand = int(k_size / 2)
            #print(expand)
            k_r_size = expand*2 + k_size
            kernel_r = np.zeros((k_r_size, k_r_size))
            kernel_r[expand:expand+k_size, expand:expand+k_size] = (weight+1)/2
            kernel_r[expand+1:expand+k_size-1, expand+1:expand+k_size-1] = 1    
            #print(kernel_r)
            
            
        elif LEDSizeOnIm % 2 == 0:
            k_size = LEDSizeOnIm + 1#光の広がりサイズ
            expand = int(k_size / 2)
            k_r_size = expand*2 + k_size
            kernel_r = np.zeros((k_r_size, k_r_size))
            kernel_r[expand:expand+k_size, expand:expand+k_size] = weight/2
            kernel_r[expand+1:expand+k_size-1, expand+1:expand+k_size-1] = 1
            #print(kernel_r)

        c = (k_r_size - 1) /2
        #print(c)
        center = (c, c)
        #print(kernel_r)
        scale_filter = (k_r_size-1) / 2
    
    if a <= 1:
        kernel_r = np.zeros((3, 3))
        kernel_r[1,1] = weight 
    
        kernel_r = np.zeros((1, 1))
        kernel_r[0,0] = weight 
        k_r_size = 1
        center = (0, 0)
        scale_filter = 0
        
    ##############################################
        ##############################################
    #配列設定
    #height and width are len(inputIm) and len(inputIm[0])
    image = np.zeros((len(inputIm), len(inputIm[0])))
    #print(image)
    
    
    #回転角度
    shita = 360

    for n in range (len(u_list_multiple)):
        for x in range (shita):        
            if data_list[n][x] == 1:
                ####################
                ###rotation kernel computing
                trans = cv2.getRotationMatrix2D(center, 360-x , 1.0) # retval= cv2.getRotationMatrix2D(center, angle, scale)
                Kernel_R = cv2.warpAffine(kernel_r, trans, (k_r_size,k_r_size))
                #第一引数に元画像（NumPy配列ndarray）、第二引数に2 x 3の変換行列（NumPy配列ndarray）、第三引数に出力画像のサイズ（タプル）を指定する。                print(trans)
                #print(trans)
                #print(Kernel_R)
                #print("-------")
                ####################
                
                #print(u_max)
                num_pixel = len(u_list_multiple[n][x])
                for p in range (num_pixel):              
                    v_perd = v_list_multiple[n][x][p]
                    u_perd = u_list_multiple[n][x][p]
                    image[v_perd, u_perd] = 255
                    #print(v_perd)
                    #print(u_perd)
                    #print("------")
                    for v in range (k_r_size):
                        for u in range (k_r_size):
                            mis_v = v - scale_filter
                            mis_u = u - scale_filter
                            V = int(v_perd + mis_v)
                            U = int(u_perd + mis_u)
                            #print(V, U)
                            
                            if (V==v_perd and U==u_perd):
                                image[V][U] += image[v_perd][u_perd] * Kernel_R[v][u]
                                
                            else:
                                image[V][U] += image[v_perd][u_perd] * Kernel_R[v][u]
                            
                            if image[V][U] >= 255:
                                image[V][U] = 255
                            elif image[V][U] <= 0:
                                image[V][U] = 0
                            
                            else:
                                image[V][U] = image[V][U]
    
    #光が広がった画像を生成する
    image = image.astype(np.uint8) 
    image_spread = image

    return image_spread



for d in d_list:
    output_dir = str(d)
    lzp = (f * lz)/(d * pz) #画像上LEDの発光部サイズ[pixel]
    random_data_list = Modulate_random(ln)
    rp_list = []
    u_list = []
    v_list = []
    su_list = []
    sv_list = []
    u_list_m = []
    v_list_m = []
    for i in range (0, ln, 1):
        r = max_r - (max_r-min_r)/ln*i
        rp = round(r*f/d/pz)
        rp_list.append(round(r*f/d/pz))
        u, v = GetCenter(shita,rp,ini_phase,c)
        su, sv = Get_signal_Center(shita,rp,ini_phase,c)
        U, V = GetLine(shita,multiple,rp,ini_phase,c)
        u_list.append(u)
        v_list.append(v)
        su_list.append(su)
        sv_list.append(sv)
        u_list_m.append(U)
        v_list_m.append(V)
    for shifter in range (0,360,1):
        print("distance",output_dir)
        print("shifter",shifter)
        onoff_data_list = Modulate_onoff(ln,shifter)
        offon_data_list = Modulate_offon(ln,shifter)
        OnOff_image = Exlight(onoff_data_list, lzp, u_list_m, v_list_m, empty_image)
        OffOn_image = Exlight(offon_data_list, lzp, u_list_m, v_list_m, empty_image)
        random_imgae = Exlight(random_data_list, lzp, u_list_m, v_list_m, empty_image)
        
        pil_img1 = Image.fromarray(OnOff_image)
        filename1 = output_dir + "/" + "im" + "/" + str(shifter) + 'shifted' + 'OnOff.png'
        pil_img1.save(filename1)
        
        pil_img1 = Image.fromarray(OffOn_image)
        filename1 = output_dir + "/" + "im" + "/" + str(shifter) + 'shifted' + 'OffOn.png'
        pil_img1.save(filename1)
        
        pil_img2 = Image.fromarray(random_imgae)
        filename2 = output_dir + "/" + "im" + "/" + str(shifter) + 'shifted' + 'random.png'
        pil_img2.save(filename2)
    
     # make the csv file of signal coordinates and random data
    x_object = open(output_dir + "/" +"cordinate_x_ideal.csv","w")
    y_object = open(output_dir + "/" +"cordinate_y_ideal.csv","w")
    data_object = open(output_dir + "/" +"random_data_vertual.csv","w")
    writer_x_object = csv.writer(x_object, lineterminator="\n")
    writer_y_object = csv.writer(y_object, lineterminator="\n")
    writer_data_object = csv.writer(data_object, lineterminator="\n")
    writer_x_object.writerows(su_list)
    writer_y_object.writerows(sv_list)
    writer_data_object.writerows(random_data_list)
    x_object.close
    y_object.close
    data_object.close    
"""
if __name__ == '__main__':
    main()
"""