# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです
"""

import cv2

Width = 300
Height = 100
path = "input/src.png"
img_src = cv2.imread(path)
for x in range(Height):
    for y in range(Width):
        b,g,r = img_src[x,y]
        if (b,g,r)==(255,255,255):
            continue
        img_src[x,y] = b,g,0
cv2.imshow("imgsrc",img_src)
cv2.imwrite("output.png", img_src)
cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
