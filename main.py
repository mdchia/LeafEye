#!/usr/bin/env python3

"""
main.py: run this file on images
"""

# system/file stuff
import sys
import os
import csv

# SciPy and display stuff
import matplotlib.pyplot as plt
import scipy.ndimage as ndimage

# Our own stuff
import scripts.config as config
import scripts.static_process as static_process
import scripts.imaging as imaging
import scripts.thermal as thermal


def main():
    image_filename=sys.argv[1]

    csv_exportname=sys.argv[2]
    cropsize=(10,30,290,180) #x offset, y offset, x size, y size
    temp_range=(17.0, 12.9)
    pixel_range=(0,255)
    mask_threshold=255/2

    # load thermal image
    main_image=ndimage.imread(image_filename,flatten=True)

    if len(sys.argv)==4:
        mask_filename=sys.argv[3]
        mask_image=ndimage.imread(mask_filename,flatten=True)
        cropped_mask=imaging.crop(cropsize,mask_image)
        cropped_mask=cropped_mask[:,:] < mask_threshold
        if not imaging.verify_mask(main_image, mask_image):
            raise Exception("Mask does not fit image")
        if config.debug:
            plt.imshow(cropped_mask)
            plt.show()
    else:
        cropped_mask=None

    cropped_image=imaging.crop(cropsize,main_image)

    if (config.debug):
        plt.imshow(cropped_image)
        plt.show()

    test_datset=thermal.thermal_image_to_dataset(cropped_image, temp_range, pixel_range, "1", cropped_mask)

    with open(csv_exportname, mode="w", newline="") as file:
        write_obj=csv.writer(file)
        write_obj.writerows(test_datset)

if __name__ == "__main__":
    main()