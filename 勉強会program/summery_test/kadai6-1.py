import cv2
import numpy as np

src = cv2.imread("kadai.png")
mask = cv2.imread("mask.png")

height, widht, color = src.shape
dst = np.zeros((height,widht,3), dtype="uint8")

for y in range(0,height):
    for x in range(0,widht):
        if (mask[y][x] > 200).all():
            dst[y][x] = src[y][x]
        else:
            dst[y][x] = 0
               
cv2.imshow("6-1",dst)
cv2.imwrite("6-1.png",dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
