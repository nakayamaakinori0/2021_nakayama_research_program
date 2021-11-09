# -*- coding: utf-8 -*-
import cv2
import numpy as np

# チェスボード画像（最低3枚は必要）
files = ['1.bmp', '2.bmp', '3.bmp', '4.bmp', '5.bmp'] 

size_square = 24.0 # チェスボードの正方形のサイズ[mm]
size_corner = (10, 7)  # チェスボード内のコーナー数（縦，横）

pattern_points = np.zeros((np.prod(size_corner), 3), np.float32)
pattern_points[:, :2] = np.indices(size_corner).T.reshape(-1, 2)
pattern_points *= size_square

obj_points = []
img_points = []

# ファイルを順に読み込み
for i in files:
    print(i)
    img_src = cv2.imread(i, 1)
    #img_src = cv2.imread('chesspattern.jpg', 1)
    img_gry = cv2.cvtColor(img_src, cv2.COLOR_RGB2GRAY)

    # チェスボードのコーナーを検出
    ret, corner = cv2.findChessboardCorners(img_gry, size_corner)
    #print(corner)
    
    # コーナーを描画
    cv2.drawChessboardCorners(img_src, size_corner, corner, ret)
    cv2.imshow('src', img_src)
    cv2.waitKey(0)
    
    # img_pointsにコーナーを格納
    img_points.append(corner.reshape(-1, 2))
    # img_pointsに三次元座標を格納
    obj_points.append(pattern_points)

# カメラパラメータを計算
rms, camera_matrix, dist_coefs, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, (img_src.shape[1], img_src.shape[0]), None, None)
print(rms, camera_matrix, dist_coefs, rvecs, tvecs)

# カメラパラメータを保存
np.savetxt("camera_matrix.csv", camera_matrix, delimiter =',',fmt="%0.8f")
np.savetxt("dist_coefs.csv", dist_coefs, delimiter =',',fmt="%.8f")

# 歪み補正
for i in files:
    img_src = cv2.imread(i, 1)
    img_dst = cv2.undistort(img_src, camera_matrix, dist_coefs)
    cv2.imshow('dst', img_dst)
    cv2.waitKey(0)

cv2.destroyAllWindows()
