# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 13:47:10 2019

@author: akinori
"""

# -*- coding: utf-8 -*-
"""
Created on Wed May 22 07:16:07 2019

@author: akinori
"""

import cv2
import math
import numpy as np

input_img = cv2.imread("src.png", 1)
width, height, chanel = input_img.shape

print(math.tan(math.radians(15)),math.sin(15),math.cos(15),math.atan(15))
size = tuple(np.array([width,height]))

afn_mat = np.float32([[math.cos(math.pi/6), -math.sin(math.pi/6), 0],
                      [math.sin(math.pi/6), math.cos(math.pi/6), 50],
                      [0, 0, 1]])

output_img = cv2.warpPerspective(input_img, afn_mat, size, flags = cv2.INTER_LINEAR)

cv2.imshow("input_img", input_img)
cv2.imshow("output_img", output_img)

cv2.imwrite("testtestaffine_change2.png",output_img)


cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
