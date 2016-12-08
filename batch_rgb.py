#!/usr/bin/env python3

"""
batch.py: run this file on a directory of images with an input.csv
"""

# system/file stuff
import sys
import csv

# SciPy and display stuff
import scipy.ndimage as ndimage

# GUI stuff
import easygui

# Our own stuff
import scripts.config as config
import scripts.imaging as imaging
import scripts.thermal as thermal


def main():
    print("Initializing ...")
    if len(sys.argv)>1: # check if there's a folder argument
        gui_enabled=False
        working_directory=sys.argv[1]
        if working_directory[-1]=="/":
            working_directory=working_directory[0:-1]
        source_csv=working_directory+"/input_rgb.csv"
        csv_exportname=working_directory+"/output.csv"
    else:
        gui_enabled=True
        working_directory=easygui.diropenbox("Select image folder")
        source_csv=working_directory+"/input.csv"
        csv_exportname=easygui.filesavebox("Save resulting CSV")
    pixel_range=(0,255)
    mask_threshold=255/2
    full_data=[["id","red", "blue", "green", "x","y",]]
    i=1
    with open(source_csv) as csv_file:
        csv_reader=csv.DictReader(csv_file)
        for frame in csv_reader:

            # say what we're doing
            print("Starting image "+str(i), end="")
            sys.stdout.flush()

            # process each entry in csv
            # csv format: id, image name, mask name
            image_filename=working_directory+"/"+frame["rgb_name"]
            mask_filename=working_directory+"/"+frame["mask_name"]
            temp_range=(0,1)
            id=frame["id"]

            # load rgb image
            main_image=ndimage.imread(image_filename)

            # process mask to boolean
            mask_image=ndimage.imread(mask_filename,flatten=True)
            mask_image=mask_image[:,:] < mask_threshold
            if not imaging.verify_mask(main_image, mask_image):
                raise Exception("Mask does not fit image")

            # make the dataset for this image
            frame_data=thermal.thermal_image_to_dataset(mask_image,
                                                        temp_range, pixel_range,
                                                        id, mask=mask_image,
                                                        rgb=main_image,
                                                        rgb_only=True)
            full_data.extend(frame_data)
            i+=1
            print("done!")

    # save the dataset
    print("Saving csv ...")
    with open(csv_exportname, mode="w", newline="") as file:
        write_obj=csv.writer(file)
        write_obj.writerows(full_data)
    print("Completed!")
    if gui_enabled: easygui.textbox("Processing complete!")

if __name__ == "__main__":
    main()