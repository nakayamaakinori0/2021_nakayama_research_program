# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:10:55 2019

@author: akinori
"""

import cv2
import glob
import numpy as np
import csv
import copy
from mylib import mymodules as mm
# 入力ディレクトリ
# 入力ディレクトリ
input_dir = "capture_img"
header1_dir = "header1"
header2_dir = "header2"
header3_dir = "header3"
header4_dir = "header4"
footer_dir = "footer"
header3_trimmed_dir = "header3_trimmed"
data_dir = "data"
# 出力ディレクトリ
eroded_dilated_dir = "eroded_dilated"
coloring_dir = "coloring"
# 入力画像のパス
input_path = glob.glob(input_dir + '/*')
header3_path = glob.glob(header3_dir + '/*')
header3_trimmed_path = glob.glob(header3_trimmed_dir + '/*')
data_path = glob.glob(data_dir + '/*')


# 縦方向の信号の数
length_signal_numbers = 9
# 横方向の信号の数
wide_signal_numbers = 61
# 切り出し座標
frame_xmin=610
frame_xmax=748
frame_ymin=997
frame_ymax=1054
# 切り出し座標誤差調整
adjust_xmin = 0
adjust_xmax = 0
#総座標数
all_elements_No = 0
#色付けの色
color_pallette = (0 , 255, 0)


#ヘッダ2の画素値の配列
pixel_values = []
#二次元型ｘ座標配列
signal_cordinate_x = np.zeros((length_signal_numbers,wide_signal_numbers), dtype=int)
#二次元型ｙ座標配列
signal_cordinate_y = np.zeros((length_signal_numbers,wide_signal_numbers), dtype=int)
#二次元型輝度値
piexel_value_arr = np.zeros((length_signal_numbers,wide_signal_numbers), dtype=int)


# risized画像のheader2達を入れる用のリスト
list_resized_img = []
#line画像のラベル中心座標達を入れる用のリスト
list_line_GoCs_x = []
list_line_GoCs_y = []
list_sorted_line_GoCs = []
#pixel_valuesのリスト
list_pixel_values = []

line_GoCs_array = np.array([[0,0]])
line_area_array = np.array([0])
sorted_line_GoCs_by_x = np.array([[0,0]])


count = 0
count1 = 3
count2 = 3
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

"""
 # Img_frameをラベリング
 # 画像入力
Img_frame = cv2.imread(header1_dir + "/" + "0.png", 0)
 # 画像の縦幅、横幅取得
height, width = Img_frame.shape
 # 二値化
threshold_frame, Img_frame_binari = cv2.threshold(Img_frame, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
cv2.imwrite("nitika.png", Img_frame_binari)
 # 収縮膨張処理
Img_frame_eroded_dilated = erosion_dilaition_module.erosion_dilation(Img_frame_binari, 8, 4)
 # ラベリング
frame_labelnum, frame_labelimg, frame_contours, frame_GoCs = cv2.connectedComponentsWithStats(Img_frame_binari)
 # frame_GoCsの0行目を削除
frame_GoCs = np.delete(frame_GoCs, 0, 0)

# 切り出し座標を取得
frame_xmin = int(frame_GoCs[0][0])
frame_ymin = int(frame_GoCs[0][1])
frame_xmax = int(frame_GoCs[frame_GoCs.shape[0]-1][0])
frame_ymax = int(frame_GoCs[frame_GoCs.shape[0]-1][1])
copy_frame_xmin = frame_xmin
copy_frame_ymin = frame_ymin
copy_frame_xmax = frame_xmax
copy_frame_ymax = frame_ymax

while Img_frame_binari[[frame_ymin],[frame_xmin]] > 0:
    frame_xmin -= 1
while Img_frame_binari[[frame_ymax],[frame_xmax]] > 0:
    frame_xmax += 1
while Img_frame_binari[[frame_ymin],[copy_frame_xmin]] > 0:
    frame_ymin -= 1
while Img_frame_binari[[frame_ymax],[copy_frame_xmax]] > 0:
    frame_ymax += 1
"""

 # ライン画像たちをトリミング
for input_file_name in header3_path:
    Img_src = cv2.imread(input_file_name, 0) #画像入力
    #処理開始
    #if count1 == 3 or count1 == 11: ###########注意!!!!!!! はみ出てるライン画像がある！！
        #Img_dst = Img_src[frame_ymin :frame_ymax , frame_xmin+adjust_xmin:frame_xmax+adjust_xmax] ###########注意!!!!!!!
    #else:
    Img_dst = Img_src[frame_ymin:frame_ymax, frame_xmin:frame_xmax]
    # 処理終了
    output_file_name1 = header3_trimmed_dir+'/'+str(count1) + ".png"
    cv2.imwrite(output_file_name1, Img_dst)

    count1 += 1


 # トリミングしたライン画像から座標取得
for input_file_name in header3_trimmed_path:
    Img_src = cv2.imread(input_file_name, 0) #画像入力
    #Img_aaa = cv2.imread("eroded_dilated" + "/" + str(count2) + ".png", 0)
    #処理開始
    line_threshold, Img_binari_line = cv2.threshold(Img_src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
    #line_threshold, Img_binari_aaa = cv2.threshold(Img_aaa, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
    #eroded_dilated_Img = erosion_dilaition_module.erosion_dilation(Img_binari_line, 8, 8) #収縮膨張処理
    #cv2.imwrite(eroded_dilated_dir + "/" + str(count2) + ".png", eroded_dilated_Img)
    #line_labelnum, line_labelimg, line_contours, line_GoCs = cv2.connectedComponentsWithStats(Img_aaa) #ラベリング
    line_labelnum, line_labelimg, line_contours, line_GoCs = cv2.connectedComponentsWithStats(Img_binari_line) #ラベリング　ラベルの数、ラベリング結果、オブジェクトの（開始点ｘ、ｙ、幅、高さ）、オブジェクトの重心
    line_GoCs = np.delete(line_GoCs, 0, 0) #line_GoCsの0行目を削除
    line_contours = np.delete(line_contours, 0, 0)#line_contoursの0行目を削除
    line_GoCs = np.round(line_GoCs) # 座標を四捨五入
    line_GoCs = line_GoCs.astype(np.int) # int型に変換
    line_area = line_contours[:,4]# ラベルの面積を一次元配列として保存(これはノイズをラベリングしていた場合の誤って取得した座標を消すため)
    line_area_array = np.append(line_area_array, line_area)
    line_GoCs_array = np.append(line_GoCs_array, line_GoCs,0)
line_area_array = np.delete(line_area_array, 0, 0)
line_GoCs_array = np.delete(line_GoCs_array, 0, 0)
sort_addres_area = np.argsort(-line_area_array)# line_areaをを降順に並べ替えたインデックスの一次元配列を生成
sorted_line_GoCs_by_area = line_GoCs_array[sort_addres_area]# 生成したインデックスで並び替える
sorted_line_GoCs_by_area = np.delete(sorted_line_GoCs_by_area, slice(549, len(sorted_line_GoCs_by_area)), 0)
for i in range ( 0, len(sorted_line_GoCs_by_area)):#座標の値を切り出す前に戻す
    sorted_line_GoCs_by_area[i,0] += frame_xmin
    sorted_line_GoCs_by_area[i,1] += frame_ymin
sort_addres_y = np.argsort((sorted_line_GoCs_by_area[:,1]))#ｙ座標で昇順に並べ替え
sorted_line_GoCs_by_y = sorted_line_GoCs_by_area[sort_addres_y]
for n in range (0, 9):
    arr = sorted_line_GoCs_by_y[n*61:n*61+61]
    sort_addres_x = np.argsort(-(arr[:,0]))
    sorted_arr = arr[sort_addres_x]
    sorted_line_GoCs_by_x = np.append(sorted_line_GoCs_by_x, sorted_arr, 0)
coordinate_array = np.delete(sorted_line_GoCs_by_x, 0, 0)
 # 取得した座標でcapture_imgに色を付けてる
for input_file_name in input_path:
    Img_src = cv2.imread(coloring_dir + "/" + str(count3) + ".png", 1) #画像入力
    #処理開始
    Img_dst = mm.coordinate_coloring_2D(Img_src, coordinate_array, color_pallette)
    cv2.imwrite(coloring_dir + "/" + str(count3) + ".png", Img_dst); # 処理結果の保存
    #処理終了
    count3 += 1

np.savetxt("coordinate_by_header3.csv", coordinate_array, fmt="%d", delimiter=",")
