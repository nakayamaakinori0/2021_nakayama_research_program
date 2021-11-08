import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)

img_src = cv2.imread("modoki.png")

gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

img_b = cv2. threshold(gray,200,255,cv2.THRESH_BINARY_INV) [1]

operator = np.ones((3, 3), np.uint8)
img_dilate = cv2.dilate(img_b, operator, iterations=3)
img_mask = cv2.erode(img_dilate, operator, iterations=3)

reverse = 255 - img_mask

nLabels,labels,stats,centroids = cv2.connectedComponentsWithStats(img_mask)

print(nLabels)
