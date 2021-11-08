# -*- coding: utf-8 -*-
"""
カメラ入力サンプルプログラム

カラーカメラ映像をグレイスケールに変換して表示
'q'キーで終了
"""

# 数値計算ライブラリの導入
import numpy as np
# OpenCVライブラリの導入
import cv2

# カメラからの画像取得の準備
cap = cv2.VideoCapture(0)

while(True):
    # 1フレームをキャプチャ
    ret, frame = cap.read() 

    # キャプチャしたフレーム画像をウィンドウ表示
    cv2.imshow('original', frame)

    # キャプチャしたフレーム画像をグレイスケールに変換
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # グレイスケールに変換した画像をウィンドウ表示
    cv2.imshow('frame', gray)

    # キーボードから 'q' が入力されたらwhileループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# カメラからの画像取得終了
cap.release()

# 表示されているウィンドウをすべて閉じる
cv2.destroyAllWindows()