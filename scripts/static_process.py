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


def thermal_image_to_dataset(image, temp_range, pixel_range, id): #TODO
    export_data=[]
    i=0
    for y in range(len(image)):
        for x in range(len(image[0])):
            raw=image[y][x]
            temp=pixel_to_temp(temp_range,pixel_range,raw)
            # format: id, temp, raw, x coord, y coord
            export_data.append([id, temp, raw, y, x])
    return export_data


def pixel_to_temp(temp_range, pixel_range, pixel):
    maxtemp=temp_range[1]
    mintemp=temp_range[0]
    maxpixel=pixel_range[1]
    minpixel=pixel_range[0]
    normpixel=(pixel-minpixel)/(maxpixel-minpixel) #normalize pixel value
    temp=(maxtemp-mintemp)*normpixel+mintemp #reverse normalization with temperature scale
    return temp


def verify_mask(image, mask, binary=True):
    return True