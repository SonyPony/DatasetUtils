# coding=utf-8
"""
Tranposes images according to EXIF orientation flag.
"""

import os
import argparse
from PIL import Image, ExifTags


# argument parsing
parser = argparse.ArgumentParser(description="Rotates images in dataset according to its EXIF orientation flag.")
parser.add_argument("dataset_directory", type=str)
parser.add_argument(
    "--output_directory",
    type=str,
    default="",
    help="output dataset directory. If not specified, dataset output directory is set to dataset director."
)

# setting up
args = parser.parse_args()
DATASET_DIRECTORY = args.dataset_directory
OUTPUT_DIRECTORY = args.dataset_directory if not args.output_directory else args.output_directory # type: str

FILES_LIST = os.listdir(DATASET_DIRECTORY)
FILES_COUNT = len(FILES_LIST)


# transpose images
for i, filename in enumerate(FILES_LIST):
    print("Prcessing {}/{} {}".format(i + 1, FILES_COUNT, filename))

    # based on https://stackoverflow.com/questions/13872331/rotating-an-image-with-orientation-specified-in-exif-using-python-without-pil-in
    img = Image.open(os.path.join(DATASET_DIRECTORY, filename))
    try:
        # find orientation key
        orientation_key = None
        for key in ExifTags.TAGS.keys():
            if ExifTags.TAGS[key] == 'Orientation':
                orientation_key = key
                break

        # transpose
        exif = dict(img._getexif().items())
        orientation = exif[orientation_key]

        if orientation in (3, 4):
            img = img.rotate(180, expand=True)
        elif orientation in (5, 6):
            img = img.rotate(270, expand=True)
        elif orientation in (7, 8):
            img = img.rotate(90, expand=True)

        if orientation in (2, 4, 5, 7):
            img = img.mirror()

    except (AttributeError, KeyError, IndexError):
        # cases: image don't have getexif
        pass

    img.save(os.path.join(OUTPUT_DIRECTORY, filename))
    img.close()

