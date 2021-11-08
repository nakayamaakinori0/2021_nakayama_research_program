# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 18:40:40 2019

@author: Arailab
"""

import cv2

cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FPS, 60)           # カメラFPSを60FPSに設定
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280) # カメラ画像の横幅を1280に設定
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720) # カメラ画像の縦幅を720に設定
while True:
    # VideoCaptureから1フレーム読み込む
    ret, frame = cap.read()

    # スクリーンショットを撮りたい関係で1/4サイズに縮小
    #frame = cv2.resize(frame, (int(frame.shape[1]), int(frame.shape[0])))
    # 加工なし画像を表示する
    cv2.imshow('Raw Frame', frame)

    # 何か処理（ここでは文字列「hogehoge」を表示する）
    edframe = frame
    #cv2.putText(edframe, 'hogehoge', (0,50), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255,0), 3, cv2.LINE_AA)

    # 加工済の画像を表示する
    cv2.imshow('Edited Frame', edframe)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()