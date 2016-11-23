#!/usr/bin/env python3

"""
imaging.py: generic SciPy image-related functions
"""

import scripts.config as config
import scipy


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