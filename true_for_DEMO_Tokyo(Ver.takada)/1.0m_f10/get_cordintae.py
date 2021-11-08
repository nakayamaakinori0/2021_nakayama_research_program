# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 20:10:55 2019

@author: akinori
"""

import cv2
import glob
import numpy as np
import csv
from my_demodulation_lib import on_off_judge_module
from my_demodulation_lib import erosion_dilaition_module
from my_demodulation_lib import cordinate_coloring_module
# 入力ディレクトリ
# 入力ディレクトリ
input_dir = "capture_img"
heada1_dir = "heada1"
heada2_dir = "heada2"
trimming_heada2_dir = "trimming_heada2"
data_dir = "data"
# 出力ディレクトリ
eroded_dilated_dir = "eroded_dilated"
coloring_dir = "coloring"
# 入力画像のパス
input_path = glob.glob(input_dir + '/*')
heada2_path = glob.glob(heada2_dir + '/*')
trimming_heada2_path = glob.glob(trimming_heada2_dir + '/*')
data_path = glob.glob(data_dir + '/*')


# 縦方向の信号の数
length_signal_numbers = 9
# 横方向の信号の数
wide_signal_numbers = 61
# 切り出し座標
frame_xmin=254
frame_xmax=1096
frame_ymin=446
frame_ymax=761
# 切り出し座標誤差調整
adjust_xmin = 10
adjust_xmax = -10
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


# risized画像のheada2達を入れる用のリスト
list_resized_img = []
#line画像のラベル中心座標達を入れる用のリスト
list_line_GoCs_x = []
list_line_GoCs_y = []
list_sorted_line_GoCs = []
#pixel_valuesのリスト
list_pixel_values = []


count = 0
count1 = 2
count2 = 2
count3 = 0
count4 = 0
count5 = 0
count6 = 0
count7 = 0

"""
 # Img_frameをラベリング
 # 画像入力
Img_frame = cv2.imread(heada1_dir + "/" + "0.png", 0)
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
for input_file_name in heada2_path:
    Img_src = cv2.imread(heada2_dir + "/" + str(count1) + ".png", 0) #画像入力
    #処理開始
    if count1 == 3 or count1 == 11: ###########注意!!!!!!! はみ出てるライン画像がある！！
        Img_dst = Img_src[frame_ymin :frame_ymax , frame_xmin+adjust_xmin:frame_xmax+adjust_xmax] ###########注意!!!!!!!
    else:
        Img_dst = Img_src[frame_ymin:frame_ymax, frame_xmin:frame_xmax]
    # 処理終了
    output_file_name1 = trimming_heada2_dir+'/'+str(count1) + ".png"
    cv2.imwrite(output_file_name1, Img_dst)

    count1 += 1


 # トリミングしたライン画像から座標取得
for input_file_name in trimming_heada2_path:
    Img_src = cv2.imread(trimming_heada2_dir + "/" + str(count2) + ".png", 0) #画像入力
    #Img_aaa = cv2.imread("eroded_dilated" + "/" + str(count2) + ".png", 0)
    #処理開始
    line_threshold, Img_binari_line = cv2.threshold(Img_src, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
    #line_threshold, Img_binari_aaa = cv2.threshold(Img_aaa, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU) #二値化
    eroded_dilated_Img = erosion_dilaition_module.erosion_dilation(Img_binari_line, 8, 8) #収縮膨張処理
    cv2.imwrite(eroded_dilated_dir + "/" + str(count2) + ".png", eroded_dilated_Img)
    #line_labelnum, line_labelimg, line_contours, line_GoCs = cv2.connectedComponentsWithStats(Img_aaa) #ラベリング
    line_labelnum, line_labelimg, line_contours, line_GoCs = cv2.connectedComponentsWithStats(eroded_dilated_Img ) #ラベリング

    line_GoCs = np.delete(line_GoCs, 0, 0) #line_GoCsの0行目を削除
    line_contours = np.delete(line_contours, 0, 0)#line_contoursの0行目を削除
    line_GoCs = np.round(line_GoCs) # 座標を四捨五入
    line_GoCs = line_GoCs.astype(np.int) # int型に変換
    line_area = line_contours[:,4]# ラベルの面積を一次元配列として保存(これはノイズをラベリングしていた場合の誤って取得した座標を消すため)
    sort_addres_area = np.argsort(-line_area)# line_areaをを降順に並べ替えたインデックスの一次元配列を生成
    sorted_line_GoCs_by_area = line_GoCs[sort_addres_area]# 生成したインデックスで並び替える

    if count2 == 2:# 一フレーム目のヘッダ1は一列多いため総信号数は9*7の63個なのでifで分けてる
        trimming_line_GoCs_by_area = sorted_line_GoCs_by_area[0:63,:] #この時のヘッダ１に存在する信号の数は63個なので，それ以上座標が取れていた場合ノイズである，そのノイズの座標を消す
        #ノイズを消すときに順番がバラバラになった，それを並びなおさないといけない，そのため，並びなおした配列を入れる為sorted_line_GoCsを宣言している．
        sorted_line_GoCs = np.zeros((len(trimming_line_GoCs_by_area[0]),len(trimming_line_GoCs_by_area[1])), dtype = int)
        #y座標で昇順に並び替えたインデックスを生成
        sort_addres_y = np.argsort(trimming_line_GoCs_by_area[:,1])
        #生成したインデックスで並び替える
        sorted_line_GoCs_by_y = trimming_line_GoCs_by_area[sort_addres_y,:]

        sorted_line_GoCs_rows1 = sorted_line_GoCs_by_y[0:7]#1行目のヘッダ1の信号座標
        sorted_line_GoCs_rows2 = sorted_line_GoCs_by_y[7:7*2]#2行目のヘッダ1の信号座標
        sorted_line_GoCs_rows3 = sorted_line_GoCs_by_y[7*2:7*3]#3行目のヘッダ1の信号座標
        sorted_line_GoCs_rows4 = sorted_line_GoCs_by_y[7*3:7*4]#4行目のヘッダ1の信号座標
        sorted_line_GoCs_rows5 = sorted_line_GoCs_by_y[7*4:7*5]#5行目のヘッダ1の信号座標
        sorted_line_GoCs_rows6 = sorted_line_GoCs_by_y[7*5:7*6]#6行目のヘッダ1の信号座標
        sorted_line_GoCs_rows7 = sorted_line_GoCs_by_y[7*6:7*7]#7行目のヘッダ1の信号座標
        sorted_line_GoCs_rows8 = sorted_line_GoCs_by_y[7*7:7*8]#8行目のヘッダ1の信号座標
        sorted_line_GoCs_rows9 = sorted_line_GoCs_by_y[7*8:7*9]#9行目のヘッダ1の信号座標


        sorted_line_GoCs_rows1 = sorted_line_GoCs_rows1[np.argsort(sorted_line_GoCs_rows1[:,0]),:]#1行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows2 = sorted_line_GoCs_rows2[np.argsort(sorted_line_GoCs_rows2[:,0]),:]#2行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows3 = sorted_line_GoCs_rows3[np.argsort(sorted_line_GoCs_rows3[:,0]),:]#3行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows4 = sorted_line_GoCs_rows4[np.argsort(sorted_line_GoCs_rows4[:,0]),:]#4行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows5 = sorted_line_GoCs_rows5[np.argsort(sorted_line_GoCs_rows5[:,0]),:]#5行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows6 = sorted_line_GoCs_rows6[np.argsort(sorted_line_GoCs_rows6[:,0]),:]#6行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows7 = sorted_line_GoCs_rows7[np.argsort(sorted_line_GoCs_rows7[:,0]),:]#7行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows8 = sorted_line_GoCs_rows8[np.argsort(sorted_line_GoCs_rows8[:,0]),:]#8行目のx座標を昇順に並べ替え
        sorted_line_GoCs_rows9 = sorted_line_GoCs_rows9[np.argsort(sorted_line_GoCs_rows9[:,0]),:]#9行目のx座標を昇順に並べ替え

        #上で生成した9行で分けた座標を結合して代入
        sorted_line_GoCs = np.concatenate((sorted_line_GoCs_rows1,sorted_line_GoCs_rows2,sorted_line_GoCs_rows3,
                                           sorted_line_GoCs_rows4,sorted_line_GoCs_rows5,sorted_line_GoCs_rows6,
                                           sorted_line_GoCs_rows7,sorted_line_GoCs_rows8,sorted_line_GoCs_rows9),
                                           axis=0)

    else:#一フレーム目以外のヘッダ1の送信号数は9*6の５４個で上と送信号数が違うだけでこのelse下記でやっていることは同じ
        trimming_line_GoCs_by_area = sorted_line_GoCs_by_area[0:54,:]

        sorted_line_GoCs = np.zeros((len(trimming_line_GoCs_by_area[0]),len(trimming_line_GoCs_by_area[1])), dtype = int)

        sort_addres_y = np.argsort(trimming_line_GoCs_by_area[:,1])
        sorted_line_GoCs_by_y = trimming_line_GoCs_by_area[sort_addres_y,:]

        sorted_line_GoCs_rows1 = sorted_line_GoCs_by_y[0:6]
        sorted_line_GoCs_rows2 = sorted_line_GoCs_by_y[6:6*2]
        sorted_line_GoCs_rows3 = sorted_line_GoCs_by_y[6*2:6*3]
        sorted_line_GoCs_rows4 = sorted_line_GoCs_by_y[6*3:6*4]
        sorted_line_GoCs_rows5 = sorted_line_GoCs_by_y[6*4:6*5]
        sorted_line_GoCs_rows6 = sorted_line_GoCs_by_y[6*5:6*6]
        sorted_line_GoCs_rows7 = sorted_line_GoCs_by_y[6*6:6*7]
        sorted_line_GoCs_rows8 = sorted_line_GoCs_by_y[6*7:6*8]
        sorted_line_GoCs_rows9 = sorted_line_GoCs_by_y[6*8:6*9]

        sorted_line_GoCs_rows1 = sorted_line_GoCs_rows1[np.argsort(sorted_line_GoCs_rows1[:,0]),:]
        sorted_line_GoCs_rows2 = sorted_line_GoCs_rows2[np.argsort(sorted_line_GoCs_rows2[:,0]),:]
        sorted_line_GoCs_rows3 = sorted_line_GoCs_rows3[np.argsort(sorted_line_GoCs_rows3[:,0]),:]
        sorted_line_GoCs_rows4 = sorted_line_GoCs_rows4[np.argsort(sorted_line_GoCs_rows4[:,0]),:]
        sorted_line_GoCs_rows5 = sorted_line_GoCs_rows5[np.argsort(sorted_line_GoCs_rows5[:,0]),:]
        sorted_line_GoCs_rows6 = sorted_line_GoCs_rows6[np.argsort(sorted_line_GoCs_rows6[:,0]),:]
        sorted_line_GoCs_rows7 = sorted_line_GoCs_rows7[np.argsort(sorted_line_GoCs_rows7[:,0]),:]
        sorted_line_GoCs_rows8 = sorted_line_GoCs_rows8[np.argsort(sorted_line_GoCs_rows8[:,0]),:]
        sorted_line_GoCs_rows9 = sorted_line_GoCs_rows9[np.argsort(sorted_line_GoCs_rows9[:,0]),:]

        sorted_line_GoCs = np.concatenate((sorted_line_GoCs_rows1,sorted_line_GoCs_rows2,sorted_line_GoCs_rows3,
                                           sorted_line_GoCs_rows4,sorted_line_GoCs_rows5,sorted_line_GoCs_rows6,
                                           sorted_line_GoCs_rows7,sorted_line_GoCs_rows8,sorted_line_GoCs_rows9),
                                           axis=0)


    # line_GoCs_x,line_GoCs_yを9*7または9*6の二次元配列に
    reshaped_line_GoCs_x = np.reshape(sorted_line_GoCs[:,0],(length_signal_numbers,int((len(sorted_line_GoCs))/length_signal_numbers)))
    reshaped_line_GoCs_y = np.reshape(sorted_line_GoCs[:,1],(length_signal_numbers,int((len(sorted_line_GoCs))/length_signal_numbers)))
    #　line画像のラベル中心座標達を三次元配列にまとめる
    list_line_GoCs_x.append(reshaped_line_GoCs_x)
    list_line_GoCs_y.append(reshaped_line_GoCs_y)

    # 取得した座標のオンの時の画素値の配列を作る
    for rows in range (0, reshaped_line_GoCs_x.shape[0]):
        for column in range (0, reshaped_line_GoCs_x.shape[1]):
            pixel_values.append(Img_src[reshaped_line_GoCs_y[rows, column],reshaped_line_GoCs_x[rows, column]])
    reshaped_pixel_values = np.reshape(pixel_values,(length_signal_numbers,int((len(pixel_values))/length_signal_numbers)))
    list_pixel_values.append(reshaped_pixel_values)
    pixel_values = []
    #処理終了
    #cv2.imwrite(eroded_dilated_dir + '/' + str(count2) + ".png", eroded_dilated_Img)
    count2 += 1


 # 座標をトリミングする前に戻す
list_line_GoCs_x[0] += frame_xmin
list_line_GoCs_x[1] += frame_xmin + adjust_xmin ###########注意!!!!!!!
list_line_GoCs_x[2] += frame_xmin
list_line_GoCs_x[3] += frame_xmin
list_line_GoCs_x[4] += frame_xmin
list_line_GoCs_x[5] += frame_xmin
list_line_GoCs_x[6] += frame_xmin
list_line_GoCs_x[7] += frame_xmin
list_line_GoCs_x[8] += frame_xmin
list_line_GoCs_x[9] += frame_xmin + adjust_xmin ###########注意!!!!!!!

list_line_GoCs_y[0] += frame_ymin
list_line_GoCs_y[1] += frame_ymin
list_line_GoCs_y[2] += frame_ymin
list_line_GoCs_y[3] += frame_ymin
list_line_GoCs_y[4] += frame_ymin
list_line_GoCs_y[5] += frame_ymin
list_line_GoCs_y[6] += frame_ymin
list_line_GoCs_y[7] += frame_ymin
list_line_GoCs_y[8] += frame_ymin
list_line_GoCs_y[9] += frame_ymin


 #座標と輝度値の配列を画像の形の二次元配列に
for x in range (0,7):
    for z in range (0, 10):
        if x == 6 and z>0:
            break
        else:
            signal_cordinate_x[:,count6] = list_line_GoCs_x[z][:,x]
            signal_cordinate_y[:,count6] = list_line_GoCs_y[z][:,x]
            piexel_value_arr[:,count6] = list_pixel_values[z][:,x]
            count6 += 1

tsignal_cordinate_x = np.delete(signal_cordinate_x,[0,1,signal_cordinate_x.shape[1]-2,signal_cordinate_x.shape[1]-1],1)
tsignal_cordinate_y = np.delete(signal_cordinate_y,[0,1,signal_cordinate_y.shape[1]-2,signal_cordinate_y.shape[1]-1],1)
piexel_value_arr = np.delete(piexel_value_arr,[0,1,piexel_value_arr.shape[1]-2,piexel_value_arr.shape[1]-1],1)
judge_threshold_arr = piexel_value_arr*2/3

"""
 # 取得した座標でcapture_imgに色を付けてる
for input_file_name in input_path:
    Img_src = cv2.imread(input_dir + "/" + str(count3) + ".png", 1) #画像入力
    #処理開始
    Img_dst = cordinate_coloring_module.cordinate_coloring(Img_src, tsignal_cordinate_x, tsignal_cordinate_y, color_pallette)
    cv2.imwrite(coloring_dir + "/" + str(count3) + ".png", Img_dst); # 処理結果の保存
    #処理終了
    count3 += 1
"""
#座標csvに書き込み
x_object = open("cordinate_x.csv", "w")
y_object = open("cordinate_y.csv", "w")
judge_threshold_object = open("judge_threshold.csv", "w")
writer_x_object = csv.writer(x_object, lineterminator="\n")
writer_y_object = csv.writer(y_object, lineterminator="\n")
writer_judge_threshold_object = csv.writer(judge_threshold_object, lineterminator="\n")
writer_x_object.writerows(tsignal_cordinate_x)
writer_y_object.writerows(tsignal_cordinate_y)
writer_judge_threshold_object.writerows(judge_threshold_arr)
x_object.close
y_object.close
judge_threshold_object.close
"""
# 全データ復調値ｃｓｖ書き込みの準備
result_object = open("all_demodulation_value.csv", "w")
writer_result_object = csv.writer(result_object, lineterminator="\n")

for input_file_name in data_path:
    img_src = cv2.imread(input_file_name, 0) # 入力画像（カラー）の読み込み
    #処理開始
    # 取得した座標の画素値を順に判断していき、黒なら０白なら１の値をsingo配列に代入
    singo = on_off_judge_module.on_off_judge(img_src,tsignal_cordinate_x, tsignal_cordinate_y, judge_threshold_arr)
    #処理終了
    # 全データの復調値をｃｓｖに保存
    writer_result_object.writerows(singo)

result_object.close
"""