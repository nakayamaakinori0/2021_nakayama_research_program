# -*- coding: utf-8 -*-
"""
Created on Wed May 15 15:49:21 2019

@author: tzq84
"""

import cv2
import numpy as np
import copy
np.set_printoptions(threshold=np.inf)
 
#カーネルサイズ
N = 3

#閾値
Tr = 210

#σ^2
Gsigma2 = 0.1

src = cv2.imread("input/002.jpg") # 画像のロード

# グレースケール化
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
print(gray)
cv2.imshow("gray", gray)

#gray = cv2.GaussianBlur(gray, (3, 3), np.sqrt(Gsigma2))

height, width = gray.shape # 高さ・幅取得

#オペレータ
kernel = np.array([[-1, 0, 1],
                    [-2, 0, 2],
                    [-1, 0, 1]])

#print(kernel0[1][0])

#copy
gray_out = copy.copy(gray)

#オペレータサイゼが3x3時のフィルタ処理
for i in range (1, height-1, 1):
    for j in range (1, width-1, 1):
        gray_array = gray[ i - 1 : i + 2 , j - 1 : j + 2]  
        #print(gray_array)
        ccc = 0
        for m in range (N):
            for n in range (N):
                bbb = gray_array[m][n] * kernel[m][n]
                ccc = ccc + bbb
                gray_out[i][j] = ccc
                """
                if ccc >= Tr:                   
                    gray_out[i][j] = ccc
                else:
                    gray_out[i][j] = 0
                """
        #debug用
        """         
        if (i == 1 and j == 1):
            print(gray_array)
            print(ccc)
        """
print(gray_out)

#img = Image.fromarray(gray_out)
#img.show()
#cv2.imshow("gray", img)
cv2.imshow("gray_out", gray_out)
cv2.imwrite("gray_out.jpg", gray_out)
cv2.waitKey(0)
cv2.destroyAllWindows()