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


def main():
    image_filename=sys.argv[1]
    #csv_exportname=sys.argv[2]
    cropsize=(10,30,290,180) #x offset, y offset, x size, y size
    temprange=(31.5,20.5)

    # load thermal image
    main_image=ndimage.imread(image_filename,flatten=False)

    cropped_image=static_process.image_crop(cropsize,main_image)

    plt.imshow(cropped_image)
    plt.show() # debug


if __name__ == "__main__":
    main()