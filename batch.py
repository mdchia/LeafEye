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
import numpy as np

# Our own stuff
import scripts.config as config
import scripts.imaging as imaging
import scripts.thermal as thermal


def main():
    working_directory=sys.argv[1]
    source_csv=working_directory+"/input.csv"
    csv_exportname=working_directory+"/output.csv"
    pixel_range=(0,255)
    mask_threshold=255/2
    full_data=[["id","temp","raw","x","y"]]
    i=1
    with open(source_csv) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for frame in csv_reader:
            # say what we're doing
            print("Starting image "+str(i), end="")
            # process each entry in csv
            # csv format: id, image name, mask name, max temp, min temp, crop details (2 points)
            image_filename=working_directory+frame["image_name"]
            mask_filename=working_directory+frame["mask_name"]
            temp_range=(float(frame["max_temp"]),float(frame["min_temp"]))
            cropsize=(int(frame["topleft_x"]), int(frame["topleft_y"]),
                      int(frame["bottomright_x"])-int(frame["topleft_x"]),
                      int(frame["bottomright_y"])-int(frame["topleft_y"]))
            start_coords=(int(frame["topleft_x"]), int(frame["topleft_y"]))
            id=frame["id"]
            # load thermal image
            main_image=ndimage.imread(image_filename,flatten=True)
            cropped_image=imaging.crop(cropsize,main_image)

            # process mask to boolean
            mask_image=ndimage.imread(mask_filename,flatten=True)
            cropped_mask=imaging.crop(cropsize,mask_image)
            cropped_mask=cropped_mask[:,:] < mask_threshold
            if not imaging.verify_mask(main_image, mask_image):
                raise Exception("Mask does not fit image")

            # make the dataset for this image
            frame_data=thermal.thermal_image_to_dataset(cropped_image, temp_range, pixel_range, id, cropped_mask, start_coords)
            full_data.extend(frame_data)
            i+=1
            print("done!")

    # save the dataset
    with open(csv_exportname, mode="w", newline="") as file:
        write_obj=csv.writer(file)
        write_obj.writerows(full_data)

if __name__ == "__main__":
    main()