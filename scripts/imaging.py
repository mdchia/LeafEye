#!/usr/bin/env python3

"""
imaging.py: generic SciPy image-related functions
"""

import scripts.config as config
import numpy as np


def crop(params, image):
    """
    Crops an image that is a SciPy array.
    :param params: Tuple of (top left x, top left y, x length, y length)
    :param image: Image to be cropped
    :return: Cropped image
    """
    startx, starty, xsize, ysize=params
    return image[starty:starty+ysize,startx:startx+xsize]


def verify_mask(image, mask, binary=True):
    """
    Checks an image mask is the same dimensions as the image
    :param image:
    :param mask:
    :param binary:
    :return:
    """
    if len(image)!=len(mask):
        return False
    if len(image[0])!=len(mask[0]):
        return False
    return True

def mask_crop_size(mask):
    """
    Checks a mask for min-max x and y coordinates, returns something to pass to
    crop function
    :param mask: Mask to crop to
    :return: Tuple of (top left x, top left y, x length, y length)
    """
    true_value_list=np.where(mask) # returns a list of x and a list of y coords
    startx=min(true_value_list[1])
    starty=min(true_value_list[0])
    xsize=max(true_value_list[1])-startx+1
    ysize=max(true_value_list[0])-starty+1
    return (startx,starty,xsize,ysize)
