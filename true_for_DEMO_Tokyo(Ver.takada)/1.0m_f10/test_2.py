# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 15:03:40 2019

@author: Arailab
"""

#import numpy as np
import cv2
#import uEye
cap = cv2.VideoCapture(1)
#cap.set(cv2.CAP_PROP_FPS, 50)
#cap.set(cv2.CAP_PROP_EXPOSURE, 200)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1600) 
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1200)
fps = cap.get(cv2.CAP_PROP_FPS)
rokou = cap.get(cv2.CAP_PROP_EXPOSURE)
print(fps)
print(rokou)
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()