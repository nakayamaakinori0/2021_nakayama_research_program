# -*- coding: utf-8 -*-
"""
Created on Mon Dec 23 08:59:22 2019

@author: akinori
"""

from PIL import Image
import os

filelist = {'foo.jpg', 'bar.bmp', 'zot.png'}

for infile in filelist:
    outfile = os.path.splitext(infile)[0] + ".jpg"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
        except IOError:
            print "cannot convert", infile