#!/usr/bin/env python3

"""
main.py: run this file on images
"""

import scipy
import scipy.ndimage as ndimage
import sys
import scripts.static_process as static_process
import matplotlib
import matplotlib.pyplot as plt

image_filename=sys.argv[1]
csv_exportname=sys.argv[2]
cropsize=(10,10,250,200) #x offset, y offset, x size, y size

# load thermal image
test2=ndimage.imread(image_filename,flatten=True)

test2=static_process.image_crop(cropsize,image_filename)
