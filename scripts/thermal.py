#!/usr/bin/env python3

"""
thermal.py: functions relating to thermal images
"""

import scripts.config as config
import scipy
import numpy as np
import math
import sys


def thermal_image_to_dataset(image, temp_range, pixel_range, id, mask=None,
                             start=(0,0), target=None, rgb=None, rgb_only=False):
    """
    Takes a thermal image, converts it to a wide dataset
    :param image:
    :param temp_range:
    :param pixel_range:
    :param id:
    :param mask:
    :param target:
    :param rgb: Optional rgb image to overlay data
    :return: Array as id, temp, raw, x,y, optional: distance, red, green, blue
    """
    export_data=[]
    checkpoint=math.floor(len(image)/10.01) # 10.01 is a hack for better consistency
    print(".", end="")
    for y in range(len(image)):
        for x in range(len(image[0])):
            if mask is not None:
                if not mask[y][x]:
                    continue
            raw=image[y][x]
            temp=pixel_to_temp(temp_range,pixel_range,raw)
            export_line=[id, temp, raw, x+start[0],y+start[1]]

            if target is not None:
                current_pixel=np.array((y+start[1],x+start[0]))
                distance=np.linalg.norm(target-current_pixel)
                distance=[distance] # to make it work with .extend()
                export_line.extend(distance)

            if rgb is not None:
                red = rgb[y][x][0]
                green = rgb[y][x][1]
                blue = rgb[y][x][2]
                color_data=[red,green,blue]
                export_line.extend(color_data)
                if rgb_only:
                    export_line=[id, red,green,blue, x+start[0],y+start[1]]
            export_data.append(export_line)
        if y % checkpoint==0: # Print a dot for every 10% of progress
            print(".", end="")
            sys.stdout.flush()
    return export_data


def pixel_to_temp(temp_range, pixel_range, pixel):
    """
    Converts a pixel value to a temperature.
    :param temp_range: Tuple of (min temperature, max temperature)
    :param pixel_range: Tuple of (min pixel value, max pixel value)
    :param pixel: Value of pixel.
    :return: Temperature
    """
    maxtemp=temp_range[1]
    mintemp=temp_range[0]
    maxpixel=pixel_range[1]
    minpixel=pixel_range[0]
    normpixel=(pixel-minpixel)/(maxpixel-minpixel) #normalize pixel value
    temp=(maxtemp-mintemp)*normpixel+mintemp #reverse normalization with temperature scale
    return temp