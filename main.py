#!/usr/bin/env python3

"""
main.py: run this file on images
"""

import scipy.ndimage as ndimage
import sys
import scripts.static_process as static_process
import matplotlib.pyplot as plt
import csv


def main():
    image_filename=sys.argv[1]
    csv_exportname=sys.argv[2]
    cropsize=(10,30,290,180) #x offset, y offset, x size, y size
    temp_range=(31.5,20.5)
    pixel_range=(0,255)

    # load thermal image
    main_image=ndimage.imread(image_filename,flatten=True)

    cropped_image=static_process.image_crop(cropsize,main_image)

    plt.imshow(cropped_image)
    #plt.show() # debug

    test_datset=static_process.thermal_image_to_dataset(cropped_image,
                                                        temp_range, pixel_range,
                                                        "1")
    with open(csv_exportname, mode="w", newline="") as file:
        write_obj=csv.writer(file)
        write_obj.writerows(test_datset)


if __name__ == "__main__":
    main()