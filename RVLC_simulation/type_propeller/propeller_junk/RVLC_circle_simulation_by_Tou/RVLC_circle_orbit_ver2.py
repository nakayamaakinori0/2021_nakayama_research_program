# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:24:42 2020

@author: Arailab
"""


from PIL import Image
import numpy as np
import cv2
import math
import sympy as sp
import copy

def circle_orbit2 (data, distance, LED_number, h, w):   
 
    d = distance #通信距離[m]
    
    r_max = 0.061 #一番外のLEDの回転半径　[m]
    
    LED_num = LED_number #LEDの数
    
    LED_interval = 0.0026 #一列のLED間の間隔 [m]
    
    f = 0.035 #焦点距離[m]
    
    p_s = 0.0000045 #カメラセンササイズ[m]
    
    l_s = 0.000285714285714286 #LEDの発光部サイズ[m]
    
    ##############################################
    ######重み付け　光広がりカーネル
    l_s_p = (f * l_s)/(d * p_s) #画像上LEDの発光部サイズ[pixel]
    a = copy.copy(l_s_p)
    #print(l_s_p)
    l_s_p = math.ceil(l_s_p)
    #print(l_s_p)
    weight = a - int(a)
    #print(weight)
    if a > 1:
        if l_s_p % 2 == 1:
            k_size = l_s_p #光の広がりサイズ
            expand = int(k_size / 2)
            #print(expand)
            k_r_size = expand*2 + k_size
            kernel_r = np.zeros((k_r_size, k_r_size))
            kernel_r[expand:expand+k_size, expand:expand+k_size] = (weight+1)/2
            kernel_r[expand+1:expand+k_size-1, expand+1:expand+k_size-1] = 1    
            #print(kernel_r)
            
            
        elif l_s_p % 2 == 0:
            k_size = l_s_p + 1#光の広がりサイズ
            expand = int(k_size / 2)
            k_r_size = expand*2 + k_size
            kernel_r = np.zeros((k_r_size, k_r_size))
            kernel_r[expand:expand+k_size, expand:expand+k_size] = weight/2
            kernel_r[expand+1:expand+k_size-1, expand+1:expand+k_size-1] = 1
            
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
    
    
    hight = h
    width = w
    
    #配列設定
    image = np.zeros((hight, width))
    #print(image)
    
    #円の中心
    a = hight/2
    b = width/2
    
    multiple = 50
    
    #回転角度
    shita = 360
    shita2 = shita * multiple
    
    LED_V_pixelcor_list = []
    LED_U_pixelcor_list = []
    #複数のLEDのピクセル座標 (LED_V_pixelcor_list = [[LED1_V][LED2_V]....])
    for n in range (LED_num):
        data_list = data[n]
        r = r_max - n * LED_interval
        r_p = (f * r)/(d * p_s) #LEDが画像上の半径[pixel]

        U_list = []
        V_list = []
        for CC in range (0, shita2, 1):
            cc = CC/multiple
            cc = math.radians(cc)
            U = r_p * math.sin(cc) + a
            V = -r_p * math.cos(cc) + b
            U_list.append(round(U))
            V_list.append(round(V))
            
        #print(U_list[99:100])
        #print(V_list[99:100])
        
        """
        v_list = []
        u_list = []
        for C in range (0, shita, 1):
            c = math.radians(C)
            u = r_p * math.sin(c) + a
            v = -r_p * math.cos(c) + b
            u_list.append(round(u))
            v_list.append(round(v))
        """
        
        #############################
        ######中心座標(復調データの判定用)
        U_cor_list = []
        V_cor_list = []
        for CCC in range(5, shita*10 + 5, 10):
            ccc = CCC/10
            ccc = math.radians(ccc)
            U_cor = r_p * math.sin(ccc) + a
            V_cor = -r_p * math.cos(ccc) + b
            U_cor = round(U_cor)
            V_cor = round(V_cor)
            U_cor_list.append(U_cor)
            V_cor_list.append(V_cor)
            
        LED_V_pixelcor_list.append(V_cor_list)
        LED_U_pixelcor_list.append(U_cor_list)
        #######################
    
        U_list_m = []
        V_list_m = []
        start = 0
        for n in range (shita):
            u_list_multiple = []
            v_list_multiple = []
            for m in range (start, start + multiple, 1):
                if m == 0:
                    uu = U_list[m]
                    vv = V_list[m]         
                    u_list_multiple.append(uu)
                    v_list_multiple.append(vv) 
                else:
                    uu = U_list[m]
                    vv = V_list[m] 
                    uu_dif = U_list[m] - U_list[m-1]
                    vv_dif = V_list[m] - V_list[m-1]
                    if uu_dif != 0 or vv_dif != 0:
                        u_list_multiple.append(uu)
                        v_list_multiple.append(vv)   
            U_list_m.append(u_list_multiple)
            V_list_m.append(v_list_multiple)
            start = start + multiple
        """
        #data_listの例（360度のOn-OFF）
        data_list = []
        for y in range (shita):
            Y = (y+1) % 2
            data_list.append(Y)
        #print(data_list)
        """

        for x in range (shita):        
            if data_list[x] == 1:
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
                num_pixel = len(V_list_m[x])
                for p in range (num_pixel):              
                    v_perd = V_list_m[x][p]
                    u_perd = U_list_m[x][p]
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

    return image_spread, LED_V_pixelcor_list, LED_U_pixelcor_list