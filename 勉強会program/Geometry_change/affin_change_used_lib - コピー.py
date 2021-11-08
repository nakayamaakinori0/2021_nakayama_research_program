

import cv2
import math
import numpy as np

input_img = cv2.imread("src.png", 1)
width, height, chanel = input_img.shape
center = tuple(np.array([0, 0]))
#center = tuple(np.array([input_img.shape[1]*0.5, input_img.shape[0]*0.5]))
angle = -30.0
scale = 1.0
size = tuple(np.array([input_img.shape[1], input_img.shape[0]]))
rot_mat = cv2.getRotationMatrix2D(center, angle, scale)
output_img = cv2.warpAffine(input_img, rot_mat, size, flags = cv2.INTER_LINEAR)

cv2.imshow("input_img", input_img)
cv2.imshow("output_img", output_img)

cv2.imwrite("affine_change_used_lib.png",output_img)


cv2.waitKey(0) # キー入力待ち
cv2.destroyAllWindows()
