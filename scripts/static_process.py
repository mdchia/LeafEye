#!/usr/bin/env python3

"""
static_process.py: contains basic file functions, such as cropping and
renaming
"""

import scripts.config
import scipy

def image_crop(params, image):
    startx, starty, xsize, ysize=params
    return image[starty:starty+ysize,startx:startx+xsize]

def thermal_image_to_dataset(image, temp_range, pixel_range, id):
    export_data=[]
    for y in len(image):
        for x in len(image[0]):
            raw=image[y][x]
            #temp=

def pixel_to_temp(temp_range, pixel_range, pixel):
    maxtemp=temp_range[1]
    mintemp=temp_range[0]
    maxpixel=pixel_range[1]
    minpixel=pixel_range[0]
    normpixel=(pixel-minpixel)/(maxpixel-minpixel) #normalize pixel value
    temp=(maxtemp-mintemp)*normpixel+mintemp #reverse normalization with temperature scale
    return temp