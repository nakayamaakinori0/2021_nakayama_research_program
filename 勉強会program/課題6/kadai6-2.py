
import cv2
import numpy as np  
     
img_src1 = cv2.imread("1.png")
img_src2 = cv2.imread("Squirtle.png")
 
img_gray1 = cv2.cvtColor(img_src1, cv2.COLOR_BGR2GRAY)
img_gray2 = cv2.cvtColor(img_src2, cv2.COLOR_BGR2GRAY)
# 画像配列の引き算
img_diff = cv2.absdiff(img_gray1,img_gray2)
 
img_diffm = cv2.threshold(img_diff, 50, 255, cv2.THRESH_BINARY)[1]
cv2.imshow("a",img_diffm)
operator = np.ones((3, 3), np.uint8)
img_dilate = cv2.dilate(img_diffm, operator, iterations=20)
img_mask = cv2.erode(img_dilate, operator, iterations=20)

height, widht, color = img_src1.shape
dst = np.zeros((height,widht,3), dtype="uint8")

for y in range(0,height):
    for x in range(0,widht):
        if (img_mask[y][x] > 200).all():
            dst[y][x] = img_src1[y][x]
        else:
            dst[y][x] = 0
     
 
cv2.imshow("2", dst)
cv2.imwrite("2.png", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()