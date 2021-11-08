# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""
import cv2
import numpy as np
import math
import pprint
import csv
import copy
from mylib import type_propeller as tpp
from mylib import mymodules as mm
np.set_printoptions(threshold = np.inf)
#下記関数にトリミングする座標と二値化する閾値の引数追加する必要がある

 # def main():
 # 変数宣言とディレクトリ設定
color_pallette = [0,0,255]
center_x_arr = np.array([])
center_y_arr = np.array([])
gap_error2D = []#gap_errorは何度間違えたか
signal_error2D = []#signal_errorは何bit間違えたか
GER1D = []
BER2D = []
num_data_part = 1
num_LED = 9
data_range = 360
initial_phase = 90
OnOff_threshold = 100
codn_threshold = 100
for d in range(10, 55, 5):
    distance = d / 10
    gap_error1D = []
    signal_error1D = []
    BER1D = []
    counter1D = 0
    for shifted in range(0, 360, 1):
        print("distance", distance)
        print("shifted",shifted)
        input_dir = "../transmitter/" + str(distance)
        output_dir_coordinate = str(distance) + "/result_coordinate/"
        output_dir_pv = str(distance) + "/result_pv" + "/"
        # 画像入力
        im_all_light = cv2.imread(input_dir + "/heada_part/" +"0shifted_OnOff" + ".png", 1) #画像入力
        im_all_light_gray = cv2.cvtColor(im_all_light, cv2.COLOR_BGR2GRAY)
        #bin_threshold, im_all_bin = cv2.threshold(im_all_light_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        #dilated_eroded_im_all = mm.dilation_erosion(im_all_bin, 8 , 8, 1, 1)
        im_heada_first = cv2.imread(input_dir + "/heada_part/" + str(shifted) + "shifted_OnOff" + ".png", 0)
        #
        im_heada_first_color = cv2.imread(input_dir + "/heada_part/" + str(shifted) + "shifted_OnOff" + ".png", 1)
        #
        im_heada_second = cv2.imread(input_dir + "/heada_part/" + str(shifted) + "shifted_OffOn" + ".png", 0)
        im_data_first = cv2.imread(input_dir + "/data_part/" + str(shifted) + "shifted_first_mixed_data" + ".png", 0)
        im_data_second = cv2.imread(input_dir + "/data_part/" + str(shifted) + "shifted_second_mixed_data" + ".png", 0)
        transmitted_signal_arr = np.loadtxt(
                fname = input_dir + "/transmitted_signal/" + "B_transmitted_signal.csv",
                dtype = "int",
                delimiter = ","
                )
        # 中心座標取得
        center_x, center_y = tpp.getCtr(im_all_light_gray)
        #center_x = 998
        #center_y = 999
        # 中心座標補正
        #corrcted_ctr_x, corrected_ctr_y = tpp.correctCtr(center_x, center_y, im_all_light_gray, codn_threshold)
         # 座標取得
        codn_x_array, codn_y_array = tpp.getCodn(im_all_light_gray, initial_phase, codn_threshold, center_x, center_y)
        #print("codn_x_array",codn_x_array)
         # 座標色付け
        im_heada_first_colored = mm.coordinate_coloring(im_heada_first_color, codn_x_array, codn_y_array, color_pallette)
        cv2.imwrite(str(distance) + "/plot_codn/" + str(shifted) + "shifted_OnOff_colored.png", im_heada_first_colored);
         # 座標記録
        x_object = open(output_dir_coordinate + "/" +"codn_x_array_result.csv","w")
        y_object = open(output_dir_coordinate + "/" +"codn_y_array_result.csv","w")
        writer_x_object = csv.writer(x_object, lineterminator="\n")
        writer_y_object = csv.writer(y_object, lineterminator="\n")
        writer_x_object.writerows(codn_x_array)
        writer_y_object.writerows(codn_y_array)
        x_object.close
        y_object.close
         # ズレ検出（全点灯と一次混在画像（OnOff））
        detected_gap = tpp.detectGap(im_heada_first, codn_x_array, codn_y_array, OnOff_threshold)
        print(detected_gap)
         # 輝度抽出
        first_pv_list = tpp.pickPV(im_data_first, codn_x_array, codn_y_array)
        second_pv_list = tpp.pickPV(im_data_second, codn_x_array, codn_y_array)
         # ずれ補正
        corrected_pv_list = tpp.correction(first_pv_list, second_pv_list, detected_gap)
         # 復調
        recieved_signal_list = tpp.demodulateOnOff(corrected_pv_list, OnOff_threshold)
         # 評価
        gap_error = tpp.evaluateGap(shifted, detected_gap)
        gap_error1D.append(gap_error)
        signal_error = tpp.evaluateSignal(transmitted_signal_arr, recieved_signal_list)
        signal_error1D.append(signal_error)
        BER = tpp.culcBER(signal_error,num_data_part, num_LED, data_range)
        BER1D.append(BER)
         # 補正前画素値記録
        first_pv_object = open(output_dir_pv + "/" + str(shifted) + "shifted_pvlist_first.csv", "w")
        writer_first_pv_object = csv.writer(first_pv_object, lineterminator = "\n")
        writer_first_pv_object.writerows(first_pv_list)
        first_pv_object.close
        second_pv_object = open(output_dir_pv + "/" + str(shifted) + "shifted_pvlist_second.csv", "w")
        writer_second_pv_object = csv.writer(second_pv_object, lineterminator = "\n")
        writer_second_pv_object.writerows(second_pv_list)
        second_pv_object.close
         # 補正済み画素値記録
        corrected_pv_object = open(output_dir_pv + "/" + str(shifted) + "shifted_pvlist_corrected.csv", "w")
        writer_pv_object = csv.writer(corrected_pv_object, lineterminator = "\n")
        writer_pv_object.writerows(corrected_pv_list)
        corrected_pv_object.close
         # 復調結果記録
        recieved_signal_object = open(output_dir_pv + "/" + str(shifted) + "shifted_recieved_signal.csv", "w")
        writer_rs_object = csv.writer(recieved_signal_object, lineterminator = "\n")
        writer_rs_object.writerows(recieved_signal_list)
        recieved_signal_object.close
    center_x_arr = np.append(center_x_arr, center_x)
    center_y_arr = np.append(center_y_arr, center_y)
    gap_error2D.append(gap_error1D)
    GER = tpp.culcGER(gap_error1D)
    GER1D.append(GER)
    signal_error2D.append(signal_error1D)
    BER2D.append(BER1D)
     # 検出角度誤差記録
    gap_error_object = open(output_dir_pv + "/" + "gap_error.csv", "w")
    writer_ge_object = csv.writer(gap_error_object, lineterminator = "\n")
    writer_ge_object.writerows(gap_error2D)
    gap_error_object.close
     # GER記録
    GER_object = open(output_dir_pv + "/" + "GER.csv", "w")
    writer_GER_object = csv.writer(GER_object, lineterminator = "\n")
    writer_GER_object.writerow(GER1D)
    GER_object.close
     # 復調結果誤差記録
    signal_error_object = open(output_dir_pv + "/" + "signal_error.csv", "w")
    writer_se_object = csv.writer(signal_error_object, lineterminator = "\n")
    writer_se_object.writerows(signal_error2D)
    signal_error_object.close
     # BER記録
    BER_object = open(output_dir_pv + "/" + "BER.csv", "w")
    writer_BER_object = csv.writer(BER_object, lineterminator = "\n")
    writer_BER_object.writerows(BER2D)
    BER_object.close
    # 中心座標記録
    np.savetxt(output_dir_pv + "/" + "center_x.csv", center_x_arr,fmt = "%.0f")
    np.savetxt(output_dir_pv + "/" + "center_y.csv", center_y_arr,fmt = "%.0f")



"""
coordinate_x = np.loadtxt(
        fname = input_dir + "/" + "cordinate_x_ideal.csv",
        dtype = "int",
        delimiter = ","
        )

coordinate_y = np.loadtxt(
        fname = input_dir + "/" + "cordinate_y_ideal.csv",
        dtype = "int",
        delimiter = ","
        )
"""
"""
im_a_colored = im_all_light
for rows in range (0, codn_x_array.shape[0]):
    for column in range (0, codn_y_array.shape[1]):
        im_a_colored[int(codn_y_array[rows][column]), int(codn_x_array[rows][column])] = (0,column/2,column/2)
cv2.imwrite("im_colored_real.png",im_a_colored);
"""
#pprint.pprint(codn_x_deg)
    
#if __name__ == '__main__':
#    main()
    
