# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 18:50:50 2019

@author: arailab
"""

import cv2
import numpy as np
np.set_printoptions(threshold=np.inf)

img_src = cv2.imread("rakoiru.png")

gray = cv2.cvtColor(img_src,cv2.COLOR_BGR2GRAY)

ret, img_b = cv2. threshold(gray,220,225,cv2.THRESH_BINARY)

nLabels,labels,stats,centroids = cv2.connectedComponentsWithStats(img_b)
#stats = [u,v,width,height,size] 

#print(labels.shape)
"""
print(labels[0].shape)
print(labels[:,199])

print(labels[:,199].size)

print("a",len(labels[0]))
print("b", labels[0,0])
"""
print(centroids)
centroids = np.delete(centroids,0,1)
print(labels.shape)
print(centroids)

print(stats[2,4])
#print(nLabels)