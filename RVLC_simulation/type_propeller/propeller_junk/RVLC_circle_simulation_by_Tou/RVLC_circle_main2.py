# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 13:52:54 2020

@author: Arailab
"""

import cv2
from PIL import Image
import numpy as np
#from RVLC_circle_data import circle_data
#from RVLC_circle_orbit import circle_orbit
from RVLC_circle_orbit_ver2 import circle_orbit2
from RVLC_circle_random_data import circle_data_random
np.set_printoptions(threshold=np.inf)

d = 1.0

LED_num = 9

hight = 2400 #画像の高さ

width = 2400 #画像の幅

Threshold = 128

trials = 1

Gsigma2 = 1

dB = 1 #Eb/N0

Energy = 255 #信号エネルギー

N_sigma = np.sqrt(Energy/2/(10**(dB/10)))

BER_LED1_total = 0
BER_LED2_total = 0
BER_LED3_total = 0
BER_LED4_total = 0
BER_LED5_total = 0
BER_LED6_total = 0
BER_LED7_total = 0
BER_LED8_total = 0
BER_LED9_total = 0

print("Com_distance = " +repr(d) + "m")

for x in range (trials):
    ##############################
    ## Data
    #Data = circle_data(LED_num)
    Random_data = circle_data_random(LED_num)
    #print(len(Random_data))
    LED1_data = Random_data[0]
    LED2_data = Random_data[1]
    LED3_data = Random_data[2]
    LED4_data = Random_data[3]
    LED5_data = Random_data[4]
    LED6_data = Random_data[5]
    LED7_data = Random_data[6]
    LED8_data = Random_data[7]
    LED9_data = Random_data[8]
    #print(LED1_data)
    #print(len(LED1_data))
    data_num = len(LED1_data) #1個のLEDのデータ数
    ##############################
    
    
    ##############################
    ## Sending pattern and Pixel_coordinate
    Outp_RCO = circle_orbit2(Random_data, d, LED_num, hight, width)
    Blinking_circle = Outp_RCO[0] 
    LEDs_v = Outp_RCO[1]
    LEDs_u = Outp_RCO[2]
    #print(LEDs_v)
    #print(LEDs_u)
    
    """
    LED1_v = LEDs_v[0] #一番外側のLEDのv座標
    LED2_v = LEDs_v[1]
    LED3_v = LEDs_v[2]
    LED4_v = LEDs_v[3]
    LED5_v = LEDs_v[4]
    LED6_v = LEDs_v[5]
    LED7_v = LEDs_v[6]
    LED8_v = LEDs_v[7]
    LED9_v = LEDs_v[8] #一番内側のLEDのv座標
    
    LED1_u = LEDs_u[0] #一番外側のLEDのu座標
    LED2_u = LEDs_u[1]
    LED3_u = LEDs_u[2]
    LED4_u = LEDs_u[3]
    LED5_u = LEDs_u[4]
    LED6_u = LEDs_u[5]
    LED7_u = LEDs_u[6]
    LED8_u = LEDs_u[7]
    LED9_u = LEDs_u[8] #一番内側のLEDのu座標
    """
    #print(LED1_v)
    #print(LED1_u)
    #print(Blinking_circle[33, 272])
    ##############################
    
    
    ##############################
    ## Converting sending pattern to an image (ideally)
    pil_img = Image.fromarray(Blinking_circle)
    filename = f'./RVLC_circle2_on-off_1.0m.png'
    pil_img.save(filename)
    ##############################
    
    """
    ##############################
    ## Channel
    # Bluring
    s_img = Blinking_circle
    s_img_g = cv2.GaussianBlur(s_img, (3, 3), np.sqrt(Gsigma2))
    
    #AWGN
    s_img_g_float = s_img_g.astype(np.float64)
    noise_matrix = np.random.normal(0.0, 1.0, (hight, width))*N_sigma
    s_img_g_A_float = s_img_g_float + noise_matrix
    s_img_g_A =s_img_g_A_float.astype(np.uint8)  
    
    ##############################
    
    ##############################
    ##Converting sending pattern to an image (actually)
    pil_img = Image.fromarray(s_img_g_A)
    filename = f'./RVLC_circle_on-off_G_A.png'
    pil_img.save(filename)
    ##############################
    
    
    ##############################
    ## Receiving and decoding process
    r_img = s_img
    """
    
    """
    # For LED1
    r_data_LED1_list = []
    err_num1 = 0 # LED1のエラー数
    for x in range (36):
        v = LED1_v[x]
        u = LED1_u[x]
        #print(v)
        #print(u)
        #print(r_img[v, u][0])
        #print(Threshold)
        if (r_img[v, u][0] >= Threshold):
            r_data1 = 1
        else:
            r_data1 = 0
        
        #print(r_data1)
        #print("-------")
        r_data_LED1_list.append(r_data1)
        
    #print(len(data_LED1_list))
    print(r_data_LED1_list)
    
    for y in range (data_num):
        if LED1_data[y] != r_data_LED1_list[y]:
            err_num1 += 1
        else:
            err_num1 = err_num1
    
    BER_LED1 = err_num1 / data_num / trials
    
    print(err_num1)
    print(BER_LED1)
    """
    """
    err_num_LEDs = 0 #全部のLEDのエラー数
    Individual_LED_ber_list = [] #一番外のLEDからそれぞれのLEDのBER
    for z in range (LED_num):
        r_data_LED_list = []
        err_num = 0 # 1個ずつのLEDのエラー数
        for x in range (360):
            v = LEDs_v[z][x]
            u = LEDs_u[z][x]
            #print(v)
            #print(u)
            #print(r_img[v, u][0])
            #print(Threshold)
            if (r_img[v, u] >= Threshold):
                r_data = 1
            else:
                r_data = 0
            
            #print(r_data1)
            #print("-------")
            r_data_LED_list.append(r_data)
            
        #print(len(data_LED1_list))
        #print(r_data_LED_list)
        
        for y in range (data_num):
            if Random_data[z][y] != r_data_LED_list[y]:
                err_num += 1
            else:
                err_num = err_num
        #print(err_num)        
        ber_LED = err_num / data_num
        #print(BER_LED)
        Individual_LED_ber_list.append(ber_LED)   
        
        err_num_LEDs += err_num
    
    #print(Individual_LED_ber_list)
    ber_LEDs = err_num_LEDs / data_num / LED_num
    #print(ber_LEDs)

    BER_LED1_total = BER_LED1_total + Individual_LED_ber_list[0]
    BER_LED2_total = BER_LED2_total + Individual_LED_ber_list[1]
    BER_LED3_total = BER_LED3_total + Individual_LED_ber_list[2]
    BER_LED4_total = BER_LED4_total + Individual_LED_ber_list[3]
    BER_LED5_total = BER_LED5_total + Individual_LED_ber_list[4]
    BER_LED6_total = BER_LED6_total + Individual_LED_ber_list[5]
    BER_LED7_total = BER_LED7_total + Individual_LED_ber_list[6] 
    BER_LED8_total = BER_LED8_total + Individual_LED_ber_list[7]  
    BER_LED9_total = BER_LED9_total + Individual_LED_ber_list[8]
    #print(BER_LED9_once)
    
BER_LED1 = BER_LED1_total / trials
BER_LED2 = BER_LED2_total / trials
BER_LED3 = BER_LED3_total / trials
BER_LED4 = BER_LED4_total / trials
BER_LED5 = BER_LED5_total / trials
BER_LED6 = BER_LED6_total / trials
BER_LED7 = BER_LED7_total / trials
BER_LED8 = BER_LED8_total / trials
BER_LED9 = BER_LED9_total / trials

BER_LEDs = (BER_LED1 + BER_LED2 + BER_LED3 + BER_LED4 + BER_LED5 + BER_LED6 +
            BER_LED7 + BER_LED8 + BER_LED9 ) / 9

print(BER_LED1) 
print(BER_LED2) 
print(BER_LED3) 
print(BER_LED4) 
print(BER_LED5) 
print(BER_LED6) 
print(BER_LED7) 
print(BER_LED8) 
print(BER_LED9)
print("------------")    
print(BER_LEDs) 
    #############################
"""