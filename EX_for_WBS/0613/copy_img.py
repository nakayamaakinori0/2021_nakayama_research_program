# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:40:29 2019

@author: akinori
"""

import cv2
import glob
import os

distance = 5.5
date = "20210613"
# 最初に変えないといけない入力↑
input_dir = 'captured_im/'+date + "_" +str(distance) +".avi/*"
output_dir = str(distance) + '/capture_img/' # 作業ディレクトリを代入

 # 開始画像位置
start_No = 18
 # 画像総数(protocolの総フレーム数)
total_Img = 94 # 本当は95でも今回ミスでデータ部１少ないから
 # 画像リスト
list_Img = [] 

Img_count = 0

input_path = glob.glob(input_dir) # 入力画像のパス
#print('heada2_path', heada2_path)
for input_file_name in input_path:
    Img_src = cv2.imread(input_file_name, 1) #画像入力    
    #処理開始
    list_Img.append(Img_src) #line画像のラベル中心座標達を配列に
    
os.chdir(output_dir) # 作業ディレクトリを変更
for i in range(start_No, start_No+total_Img):
    #print(list_Img[i])
    cv2.imwrite(str(Img_count)+ '.png', list_Img[i])
    Img_count += 1



"""
for input_file_name in input_path:
    Img_src = cv2.imread(input_file_name, 0) #画像入力
    Img_dst = cv2.resize(Img_src, (Img_src.shape[1]*3, Img_src.shape[0]*3))
    
    a = 'capture_img/' # 入力画像のパスにディレクトリ名がダブっているから削除するため宣言している
    
    input_file_name = input_file_name[len(a):]# aから：の右までの文字列を消している
    
    output_file_name = output_dir+'/'+input_file_name
    cv2.imwrite(output_file_name, Img_dst)
"""