# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 14:04:12 2019

@author: Arailab
"""

# OpenCV のインポート
import cv2
import subprocess

# VideoCaptureのインスタンスを作成する。
# 引数でカメラを選べれる。
cap = cv2.VideoCapture(1)
#cap.set(cv2.CAP_PROP_FPS, 5)           # カメラFPSを60FPSに設定
#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0)
#cap.set(cv2.CAP_PROP_EXPOSURE, -1.0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200) # カメラ画像の縦幅を720に設定
fps = cap.get(cv2.CAP_PROP_FPS)
rokou = cap.get(cv2.CAP_PROP_EXPOSURE)
print(fps)
print(rokou)
while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # スクリーンショットを撮りたい関係で1/4サイズに縮小
    #frame = cv2.resize(frame, (int(frame.shape[1]/4), int(frame.shape[0]/4)))
    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)

    # 何か処理（ここでは文字列「hogehoge」を表示する）
    edframe = frame
    cv2.putText(edframe, 'hogehoge', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)

    # 加工済の画像を表示する
    cv2.imshow('Edited Frame', edframe)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()