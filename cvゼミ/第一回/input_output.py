# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import cv2

path = "input/src.png"
img_src = cv2.imread(path,1)
cv2.imshow("input",img_src)
gray_src = cv2.cvtColor(img_src, cv2.COLOR_BGR2GRAY)
cv2.imshow("imgsrc",gray_src)
cv2.imwrite("output.png", gray_src)
cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
