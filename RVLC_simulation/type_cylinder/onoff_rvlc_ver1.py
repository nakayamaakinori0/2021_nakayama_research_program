# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

from PIL import Image
import numpy as np
from numpy import random
import cv2
import math
import csv
import itertools
import copy

"""
im = np.array(Image.open('./src.png'))

im_R = im.copy()
im_R[:, :, (1, 2)] = 0
im_G = im.copy()
im_G[:, :, (0, 2)] = 0
im_B = im.copy()
im_B[:, :, (0, 1)] = 0

# 横に並べて結合（どれでもよい）
im_RGB = np.concatenate((im_R, im_G, im_B), axis=1)
# im_RGB = np.hstack((im_R, im_G, im_B))
# im_RGB = np.c_['1', im_R, im_G, im_B]

pil_img = Image.fromarray(im_RGB)
pil_img.save('./hoge.png')
"""

#固定パラメータ

d=3.5 #通信距離[m]

f=0.035 #焦点距離[m]

s_size = 0.0000045 #カメラセンササイズ[m]

t_radius = 0.058 #送信機半径[m]

No_LEDs = 9 #送信機のLED数

l_size = 0.000285714285714286 #LEDの発光部サイズ[m]

g_size = 0.00285714285714286 #LED間の間隔[m]


D_LED = math.degrees(math.atan(l_size/t_radius/2)) #LEDの幅に換算した角度
#print(D_LED)

Gsigma2 = 0.7 #ガウシアンフィルタの分散            
     
position = 200 # 信号位置

step = 1


Data_Range = 60 #データ範囲角度
data =np.zeros((Data_Range*No_LEDs), np.uint8)
r_data =np.zeros((Data_Range*No_LEDs), np.uint8)

random.seed(1)


#出力画像用パラメータ

r_width = round((t_radius*2*f/(d*s_size) + position),0) #出力画像横幅
r_hight = round((g_size*9*f/(d*s_size) + position),0) #出力画像縦幅

l_hight = round((f*l_size/(d*s_size)),0)

gap = round((g_size*f/(d*s_size)),0) # LED間の画素数


print(r_width)
print(r_hight)
print(l_hight)    
print(gap)

r_width = (int) (round((t_radius*2*f/(d*s_size) + position),0)) #出力画像横幅
r_hight = (int) (round((g_size*9*f/(d*s_size) + position),0)) #出力画像縦幅

l_hight = (int) (round((f*l_size/(d*s_size)),0))
          
          
gap = (int) (round((g_size*f/(d*s_size)),0)) # 縦のLED間の画素数
      
print(r_width)
print(r_hight)
print(l_hight)                     
print(gap)

if(l_hight==0):
    l_hight=1


#配列設定
r_image =np.zeros((r_hight, r_width, 3), np.uint8)


#### 幅がある光源 ###

#r_image =np.zeros([r_hight,r_width], np.uint8)
#r_image = np.zeros_like(r_image)

 
#a[(int)(r_hight/2)-1,(int)(r_width/2)-1] = 255
p_ini = (int)(position/4)
p_p = p_ini
for degree in range(0,181,step):
    print(degree)
    
    p_s = (f * t_radius * math.cos(math.radians(degree)))/((d+t_radius) - t_radius * math.sin(math.radians(degree)))
    p_e = (f * t_radius * math.cos(math.radians((degree+step))))/((d+t_radius) - t_radius * math.sin(math.radians(degree+step)))
    
    l_s = (f * t_radius * math.cos(math.radians(degree-D_LED)))/((d+t_radius) - t_radius * math.sin(math.radians(degree-D_LED)))
    l_e = (f * t_radius * math.cos(math.radians(degree+D_LED+step)))/((d+t_radius) - t_radius * math.sin(math.radians(degree+D_LED+step)))
    
    #print(p_s)
    #print(p_e)
    
    #print(l_s)
    #print(l_e)  
    
    n_p = (round(((p_s - p_e)/s_size),0))
    #print(n_p)
    n_p = (int) (n_p)
    print(n_p)
    
    n_p_l = (int)(round(((l_s - l_e)/s_size),0))
    print(n_p_l)
    
    dif_ls = (l_s - p_s)/s_size
    dif_le = (p_e - l_e)/s_size
   
    #print(dif_ls)
    #print(dif_le)
    
    dif_ls = (round(((l_s - p_s)/s_size),0))
    dif_le = (round(((p_e - l_e)/s_size),0))
   
    #print(dif_ls)
    #print(dif_le)
    
    dif_ls = (int) (dif_ls)
    dif_le = (int) (dif_le)
   
    #print(dif_ls)
    #print(dif_le)
    
    
    if(dif_ls+dif_le+n_p < n_p_l and 0 < dif_ls+dif_le+n_p):
        dif_le=dif_le+1
        #print("XXXXXXXX")
        #print(dif_le)
    
    if(n_p_l > 0):

            #if(degree==30):
                #print(n_p+dif_le)
        if(degree%2==0):
            s=1
        else:
            s=0
        for l in range(10):
            #s=random.randint(0, 2)
            #print(s)
            if(s==1):
                for y_l in range(l_hight):
                    for x_l in range(0-dif_ls, n_p+dif_le, 1):
                        #print(x_l)
                        r_image[p_ini + l*gap + y_l, p_p + x_l] = (255,255,255)
                    
                        #if(y_l==(int)(l_hight/2) and x_l==(int)(n_p/2)):
                                
                                #print(x_l)
                                #print(y_l)
                                #r_image[p_ini + l*gap + y_l, p_p + x_l] = (0,0,0)
        """
            else:
                for l in range(10):
                    for y_l in range(l_hight):
                        for x_l in range(0-dif_ls, n_p+dif_le, 1):
                            #print(x_l)
                            r_image[p_ini + l*gap + y_l, p_p + x_l] = (255,255,255)
                            
                            if(y_l==(int)(l_hight/2) and x_l==(int)(n_p/2)):
                                r_image[p_ini + l*gap + y_l, p_p + x_l] = (0,0,255)     
        """
        """
        else:
            for l in range(10):
                r_image[p_ini + l*gap +(int)(l_hight/2), p_p + (int)(n_p/2)] = (255,0,255)
        """    
        p_p = p_p + n_p
    else:
       p_p = p_p + n_p 
         
   
   
   
#print(r_image)

pil_img = Image.fromarray(r_image)
filename = f'./onoff_rvlc_{d}m.png'
pil_img.save(filename)

r_image_g = cv2.GaussianBlur(r_image, (5, 5), np.sqrt(Gsigma2))
#print(r_image_g)

pil_img = Image.fromarray(r_image_g)
filename = f'./onoff_rvlc_{d}m_Gauss{Gsigma2}.png'
pil_img.save(filename)
