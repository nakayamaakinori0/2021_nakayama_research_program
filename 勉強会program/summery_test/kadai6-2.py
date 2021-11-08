import cv2
import numpy as np  
     
img_src1 = cv2.imread("kadai.png")
img_src2 = cv2.imread("hama.png")
 
img_gray1 = cv2.cvtColor(img_src1, cv2.COLOR_BGR2GRAY)
img_gray2 = cv2.cvtColor(img_src2, cv2.COLOR_BGR2GRAY)

img_diff = cv2.absdiff(img_gray1,img_gray2)

img_diffm = cv2.threshold(img_diff, 15, 255, cv2.THRESH_BINARY)[1]

operator = np.ones((3, 3), np.uint8)
img_dilate = cv2.dilate(img_diffm, operator, iterations=7)
img_mask = cv2.erode(img_dilate, operator, iterations=7)

img_dst = cv2.bitwise_and(img_gray1, img_mask)
     
cv2.imshow("6-2", img_dst)
cv2.imwrite("6-2.png", img_dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
