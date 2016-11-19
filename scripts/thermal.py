#!/usr/bin/env python3

"""
thermal.py: functions relating to thermal images
"""

import scripts.config
import scipy


def thermal_image_to_dataset(image, temp_range, pixel_range, id, mask=None):
    """
    Takes a thermal image, converts it to a wide dataset
    :param image:
    :param temp_range:
    :param pixel_range:
    :param id:
    :param mask:
    :return:
    """
    export_data=[]
    i=0
    use_mask=True
    if mask is None:
        use_mask==False
    for y in range(len(image)):
        for x in range(len(image[0])):
            if use_mask:
                if not mask[y][x]:
                    continue
            raw=image[y][x]
            temp=pixel_to_temp(temp_range,pixel_range,raw)
            # format: id, temp, raw, x coord, y coord
            export_data.append([id, temp, raw, y, x])
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