#!/usr/bin/env python3

"""
static_process.py: contains file pre-processing functions, such as cropping and
renaming
"""

import scripts.config
import scipy

def image_import(filename):
    scipy.ndimage.imread(filename)