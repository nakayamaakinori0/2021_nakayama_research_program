# -*- coding: utf-8 -*-
import cv2
import numpy as np
import sys

size_square = 24.0 # チェスボードの正方形のサイズ[mm]
size_corner = (10, 7)  # チェスボード内のコーナー数（縦，横）

pattern_points = np.zeros((np.prod(size_corner), 3), np.float32)
pattern_points[:, :2] = np.indices(size_corner).T.reshape(-1, 2)
pattern_points *= size_square

obj_points = []
img_points = []

# カメラからの画像取得の準備
cap = cv2.VideoCapture(0)

# カメラから5枚キャプチャ
for i in range(5):    
    print(i)
    #img_src = cv2.imread(i, 1)
    while(True):
        ret, img_src = cap.read()
        img_gry = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)

        # チェスボードのコーナーを検出
        ret, corner = cv2.findChessboardCorners(img_gry, size_corner)

        # コーナーが見つかった場合，描画
        if ret:
            cv2.drawChessboardCorners(img_src, size_corner, corner, ret)
        
        cv2.imshow('src', img_src)
        
        # キーボードからスペースが入力されたらコーナーを保存，qで終了
        key = cv2.waitKey(1) & 0xFF
        if key == ord(' ') and ret:
            break
        elif key == ord('q'):
            print('exit')
            cap.release()
            cv2.destroyAllWindows()
            sys.exit()

    # img_pointsにコーナーを保存
    img_points.append(corner.reshape(-1, 2))
    # img_pointsに三次元座標を保存
    obj_points.append(pattern_points)

# カメラパラメータを計算
rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (img_src.shape[1], img_src.shape[0]), None, None)
print(rms, camera_matrix, dist_coefs, rvecs, tvecs)

# カメラパラメータを保存
np.savetxt("camera_matrix.csv", camera_matrix, delimiter =',',fmt="%0.8f")
np.savetxt("dist_coefs.csv", dist_coefs, delimiter =',',fmt="%.8f")

# 歪み補正
while(True):
    ret, img_src = cap.read()     
    img_dst = cv2.undistort(img_src, camera_matrix, dist_coefs)
    cv2.imshow('dst', img_dst)
    # キーボードから 'q' が入力されたらwhileループを終了
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# カメラからの画像取得終了
cap.release()

cv2.destroyAllWindows()
