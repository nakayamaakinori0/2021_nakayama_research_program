# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:54:03 2019

@author: akinori
"""

from PIL import Image

pil_im = Image.open('empire.jpg')

pil_im_gray = Image.open('empire.jpg').convert('L')
