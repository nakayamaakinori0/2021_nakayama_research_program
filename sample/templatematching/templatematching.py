import cv2
import numpy as np

img_src = cv2.imread('src.jpg', 1)
img_template = cv2.imread('template.jpg', 1)

w, h, ch = img_template.shape
img_dst = cv2.matchTemplate(img_src, img_template, cv2.TM_CCOEFF_NORMED)
min_val, max_val, min_pt, max_pt = cv2.minMaxLoc(img_dst)

cv2.rectangle(img_src, max_pt, (max_pt[0] + w, max_pt[1] + h), (255, 0, 0), 3)

cv2.imshow('src', img_src)
cv2.imshow('dst', img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
