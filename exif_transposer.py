# coding=utf-8
"""
Tranposes images according to EXIF orientation flag.
"""

import os
import argparse
from PIL import Image, ImageOps


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
print(FILES_LIST)
for i, filename in enumerate(FILES_LIST):
    print("Prcessing {}/{} {}".format(i + 1, FILES_COUNT, filename))

    # based on https://stackoverflow.com/questions/13872331/rotating-an-image-with-orientation-specified-in-exif-using-python-without-pil-in
    img = Image.open(os.path.join(DATASET_DIRECTORY, filename))
    img = ImageOps.exif_transpose(img) # type: Image

    img.save(os.path.join(OUTPUT_DIRECTORY, filename))

