# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:03:12 2019

@author: akinori
"""
import cv2
import numpy as np
import glob
import math
import random
import copy


def getCodn_cylinder (img_binari):
    line_labelnum, line_labelimg, line_contours, line_GoCs = cv2.connectedComponentsWithStats(img_binari) #ラベリング　ラベルの数、ラベリング結果、オブジェクトの（開始点ｘ、ｙ、幅、高さ）、オブジェクトの重心
    line_GoCs = np.delete(line_GoCs, 0, 0) #line_GoCsの0行目を削除
    line_GoCs = np.round(line_GoCs) # 座標を四捨五入
    line_GoCs = line_GoCs.astype(np.int) # int型に変換
    return line_GoCs

def getArea (img_binari):
    line_labelnum, line_labelimg, line_contours, line_GoCs = cv2.connectedComponentsWithStats(img_binari) #ラベリング　ラベルの数、ラベリング結果、オブジェクトの（開始点ｘ、ｙ、幅、高さ）、オブジェクトの重心
    line_contours = np.delete(line_contours, 0, 0)#line_contoursの0行目を削除
    line_area = line_contours[:,4]# ラベルの面積を一次元配列として保存(これはノイズをラベリングしていた場合の誤って取得した座標を消すため)
    return line_area

def remove_snoise(coordinate, area ,ln, data_range):#numpy, numpy, ledの数, データ範囲
    sort_addres_area = np.argsort(-area)# line_areaをを降順に並べ替えたインデックスの一次元配列を生成
    sorted_coordinate = coordinate[sort_addres_area]# 生成したインデックスで並び替える
    new_coordinate = np.delete(sorted_coordinate, slice(ln*data_range, len(sorted_coordinate)), 0)
    return new_coordinate

def erosion_dilation (binarization, erosion_neibor_number, dilation_neibor_number, erosion_iteration, dilation_iteration):#収縮膨張
         # ２近傍定義
    neiborhood2 = np.array([1, 1, 1],
                                np.uint8)
    
     # ４近傍定義
    neiborhood4 = np.array([[0, 1, 0],
                                [1, 1, 1],
                                [0, 1, 0]],
                                np.uint8)
     # ８近傍定義
    neiborhood8 = np.array([[1, 1, 1],
                                [1, 1, 1],
                                [1, 1, 1]],
                                np.uint8)
    
    all_neiborhood = {2:neiborhood2, 4:neiborhood4, 8:neiborhood8} # 定義した近傍設定を呼び出すための母体
    erosion_neiborhood = all_neiborhood[erosion_neibor_number] # 収縮時の近傍選択　２か４か８
    dilation_neiborhood = all_neiborhood[dilation_neibor_number] # 膨張時の近傍選択　２か４か８
    
    eroded = cv2.erode(binarization,erosion_neiborhood,erosion_iteration)
    return cv2.dilate(eroded, dilation_neiborhood, dilation_iteration)

def dilation_erosion(binarization, erosion_neibor_number, dilation_neibor_number, dilation_iteration, erosion_iteration):#膨張収縮
    neiborhood2 = np.array([1, 1, 1])
    
    neiborhood4 = np.array([[0, 1, 0],
                            [1, 1, 1],
                            [0, 1, 0]])
    neiborhood8 = np.array([[1, 1, 1],
                            [1, 1, 1],
                            [1, 1, 1]])
    
    all_neiborhood = {2:neiborhood2, 4:neiborhood4, 8:neiborhood8}
    erosion_neiborhood = all_neiborhood[erosion_neibor_number]
    dilation_neiborhood = all_neiborhood[dilation_neibor_number]
    
    dilated = cv2.dilate(binarization, dilation_neiborhood, dilation_iteration)
    return cv2.erode(dilated, erosion_neiborhood, erosion_iteration)

def img_to_list(input_dir, start_no, end_no, chanel):#入力ディレクトリ、何枚目から？、何枚目まで？、カラー：１グレー：０
    input_path = glob.glob(input_dir + '/*')
    #if start_no is None:
    #    start_no = 0
    #if end_no is None:
    #    end_no = len(input_path)
    list_img = []
    count = start_no
    for input_file_name in input_path:
        if count <= end_no:
            Img_src = cv2.imread(input_dir + "/" + str(count) +".png", chanel)
            list_img.append(Img_src)
            count += 1
    return list_img

def evaluateSignal(transmitted_signal_list,recieved_signal_list):#送信信号配列、受信信号配列
    signal_error=0
    for y in range (len(transmitted_signal_list)):
        for x in range (len(transmitted_signal_list[0])):
            if transmitted_signal_list[y][x] == recieved_signal_list[y][x]:
                signal_error = signal_error # 復調値と正解があっていればｋに入っている値を代入
            else:
                signal_error = signal_error + 1 # 間違っていればｋの値に＋１
    return signal_error
        
def culcBER(all_signal_error, num_data_part, num_LED, data_range):#信号エラー数、データフレーム数、LEDの数、データレンジ
    # BER算出、num_signalは一枚あたりのLED数
    BER = all_signal_error / (num_data_part*num_LED * data_range)
    return BER

###############################################################################
###############################################################################
#############################type_cylinder#####################################
###############################################################################
###############################################################################
def on_off_judge (Img_src,signal_cordinate_x, signal_cordinate_y, jujge_threshold_arr):
    
    true_singo = np.zeros((signal_cordinate_x.shape[0], signal_cordinate_x.shape[1]), dtype = 'str')
    for rows in range (0, signal_cordinate_x.shape[0]):
        for column in range (0, signal_cordinate_x.shape[1] ):
            if Img_src[signal_cordinate_y[rows, column],signal_cordinate_x[rows, column]] > jujge_threshold_arr[rows, column]:
                true_singo[rows,column] = '1'
                #ko_singo.append('1')
            else:
                true_singo[rows,column] = '_'
                #ko_singo.append(' ')
    return true_singo

def coordinate_coloring (Img_src, signal_cordinate_x, signal_cordinate_y, color_pallette):
    
    Img_dst = Img_src
    for rows in range (0, signal_cordinate_x.shape[0]):
        for column in range (0, signal_cordinate_x.shape[1]):
            Img_dst[signal_cordinate_y[rows][column], signal_cordinate_x[rows][column]] = color_pallette
    return Img_dst

def coordinate_coloring_2D(img_src, coordinate_list, color_pallette):
    for i in range (0, len(coordinate_list)):
        img_src[coordinate_list[i,1], coordinate_list[i,0]] = color_pallette
    return img_src

###############################################################################
###############################################################################
#############################type_propeller####################################
###############################################################################
###############################################################################
#transmitter
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

#####################################################################################################
#reciever
def getCodn(im_all_light, initial_phase): # 座標取得
    height, width = im_all_light.shape
    shita = 360
    codn_x_list = []
    codn_y_list = []
    codn_x_ln_list1d = []
    codn_y_ln_list1d = []
    codn_x_deg_list2d = []
    codn_y_deg_list2d = []
    a_threshold, im_a_binary = cv2.threshold(im_all_light, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    a_nlabels, a_label_im, a_data_list, a_center_list = cv2.connectedComponentsWithStats(im_a_binary)
    center_x_int, center_y_int = round(a_center_list[1,0]), round(a_center_list[1,1])
    #print(a_center_list)
    diagonal = round(math.sqrt(height**2 + width**2))
    for degree in range (0, shita):#
        codn_x_ln_list1d = []
        codn_y_ln_list1d = []
        for radius in range (0, diagonal//2,1):
            codn_x = int(round(radius * math.cos(math.radians(degree-initial_phase + 0.5)) + center_x_int))
            codn_y = int(round(radius * math.sin(math.radians(degree-initial_phase + 0.5)) + center_y_int))
            if codn_x < width and codn_y < height:
                if im_a_binary[codn_y, codn_x] == 255:
                    codn_x_list.append(codn_x)
                    codn_y_list.append(codn_y)
                elif im_a_binary[codn_y, codn_x] == 0:
                    if len(codn_x_list) != 0:
                        if len(codn_x_list) == 1:# If signal is line
                            codn_x_ln_list1d.append(codn_x_list[0])
                            codn_y_ln_list1d.append(codn_y_list[0])
                        elif len(codn_x_list) == 2:# If sisnal width is 2
                            codn_x_ln_list1d.append(codn_x_list[0])
                            codn_y_ln_list1d.append(codn_y_list[0])
                        elif len(codn_x_list) % 2 == 1:# If signal width is odd
                            quotient = len(codn_x_list) // 2
                            del codn_x_list[quotient+1:]
                            del codn_y_list[quotient+1:]
                            del codn_x_list[0:quotient]
                            del codn_y_list[0:quotient]
                            codn_x_ln_list1d.append(codn_x_list[0])
                            codn_y_ln_list1d.append(codn_y_list[0])
                            #print("Odd")
                        elif len(codn_x_list) % 2 == 0:# If signal width is even
                            quotient = len(codn_x_list) // 2
                            del codn_x_list[quotient:]
                            del codn_y_list[quotient:]
                            del codn_x_list[0:quotient-1]
                            del codn_y_list[0:quotient-1]
                            codn_x_ln_list1d.append(codn_x_list[0])
                            codn_y_ln_list1d.append(codn_y_list[0])
                            #print("Even")
                        codn_x_list = []
                        codn_y_list = []
        codn_x_deg_list2d.append(codn_x_ln_list1d)
        codn_y_deg_list2d.append(codn_y_ln_list1d)
    codn_x_array = np.array(codn_x_deg_list2d)
    codn_y_array = np.array(codn_y_deg_list2d)
    codn_x_array = codn_x_array.T
    codn_y_array = codn_y_array.T
    codn_x_array = np.flipud(codn_x_array)
    codn_y_array = np.flipud(codn_y_array)
    return codn_x_array, codn_y_array


def detectGap(im_first, codn_x_array, codn_y_array, OnOff_threshold): # ずれ角度検出
    gap_counter = 0
    f_threshold, im_f_binary = cv2.threshold(im_first, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    for d in range (0, len(codn_x_array)):
        if im_f_binary[codn_y_array[0,d], codn_x_array[0,d]] == 255:
            gap_counter += 1
    gap_counter = abs(360-gap_counter)
    return gap_counter

def pickPV(im_first, im_second, codn_x_array, codn_y_array, gap): # 輝度抽出
    ln = len(codn_x_array)
    degree = len(codn_x_array[0])
    pv_list_1d = []
    pv_list_2d = []
    for n in range(ln):
        pv_list_1d = []
        for d in range(degree):
            if d < gap:
                pv_list_1d.append(im_first[codn_y_array[n,d],codn_x_array[n,d]])
            if d >= gap:
                pv_list_1d.append(im_second[codn_y_array[n,d],codn_x_array[n,d]])
        pv_list_2d.append(pv_list_1d)
    return pv_list_2d


def demodulateOnOff(pv_list, OnOff_threshold):# オンオフ判定（復調）
    signal_list = copy.deepcopy(pv_list)
    for ln in range(0, len(pv_list)):
        for d in range(0, len(pv_list[0])):
            if pv_list[ln][d] > OnOff_threshold:
                signal_list[ln][d] = 1
            else:
                signal_list[ln][d] = 0
    return signal_list

def evaluateGap(true_gap,detected_gap): # 検出角度評価
    if true_gap != detected_gap:
        gap_error = abs(true_gap - detected_gap)
    else:
        gap_error = 0
    return gap_error
    
def culcGER(all_gap_diff_list): # GapErrorRate算出(0~359度、全360ずれ角度中何度誤ったか)
    gap_error_count = 0
    for i in range(0, len(all_gap_diff_list)):
        if all_gap_diff_list[i] != 0:
            gap_error_count += 1
    GER = gap_error_count/360
    return GER

