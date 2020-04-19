# coding=utf-8
"""
Renames files in dataset to numbers in specified format.
"""

import os
import argparse
from shutil import copyfile
from PIL import Image


# argument parsing
parser = argparse.ArgumentParser(description="Renames files in dataset to numbers in specified format.")
parser.add_argument("dataset_directory", type=str)
parser.add_argument("--format", type=str, default="jpg", help="output image format")
parser.add_argument(
    "--output_directory",
    type=str,
    default="",
    help="output dataset directory. If not specified, dataset output directory is set to dataset director."
)

# setting up
args = parser.parse_args()
DATASET_DIRECTORY = args.dataset_directory
OUT_FILENAME_FORMAT = args.format # type: str
OUTPUT_DIRECTORY = args.dataset_directory if not args.output_directory else args.output_directory # type: str

FILES_LIST = os.listdir(DATASET_DIRECTORY)
FILES_COUNT = len(FILES_LIST)

# instead of copying to out directory, rename files in dataset directory with the new name
RENAME_IN_DATASET_DIR = os.path.abspath(DATASET_DIRECTORY) == os.path.abspath(OUTPUT_DIRECTORY)

# renaming files
count = 0
for i, filename in enumerate(FILES_LIST):
    print("Prcessing {}/{}".format(i + 1, FILES_COUNT))

    stem, ext =  os.path.splitext(filename)
    image_path = os.path.join(DATASET_DIRECTORY, filename)
    new_filename = "{stem}.{ext}".format(stem=stem, ext=OUT_FILENAME_FORMAT)
    new_image_path = os.path.join(OUTPUT_DIRECTORY, new_filename)

    if ext.replace(".", "").lower() == OUT_FILENAME_FORMAT:
        if ext.replace(".", "") != OUT_FILENAME_FORMAT:
            if RENAME_IN_DATASET_DIR:
                print(new_image_path)
                os.rename(src=image_path, dst=new_image_path)
            else:
                copyfile(src=image_path, dst=new_image_path)
        continue


    img = Image.open(image_path)

    img.save(new_image_path)

    if RENAME_IN_DATASET_DIR:
        os.remove(image_path)


