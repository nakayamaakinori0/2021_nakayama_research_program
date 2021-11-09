#!/usr/bin/python
# -*- coding: utf-8 -*-
import cv2
import argparse
import os
import numpy as np
 
parser = argparse.ArgumentParser()
parser.add_argument("source_dir")
parser.add_argument("target_dir")
args = parser.parse_args()
 

print("Input x") #始点x座標
x = input()

print("Input y") #始点y座標
y = input()

print("Input l") #切り出す長さ
l = input()

print(int(x), int(y), int(l))

end_x = int(x) + int(l)
end_y = int(y) + int(l)

print(int(end_x), int(end_y))


target_shape = (256, 256)
output_side_length=256

for source_imgpath in os.listdir(args.source_dir):
  print(source_imgpath)
  img = cv2.imread(args.source_dir+"/"+source_imgpath, 0)
  
  #トリミング
  dst = img[int(y):int(end_y),int(x):int(end_x)] #[始点y:終点y, 始点x:終点x]

  #リサイズ(256x256)
  resized_img = cv2.resize(dst, (output_side_length, output_side_length))
  cv2.imwrite(args.target_dir+"/"+source_imgpath, resized_img) 
  

