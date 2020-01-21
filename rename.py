# coding=utf-8
"""
Renames files in dataset to numbers in specified format.
"""

import os
import argparse
from shutil import copyfile


# argument parsing
parser = argparse.ArgumentParser(description="Renames files in dataset to numbers in specified format.")
parser.add_argument("dataset_directory", type=str)
parser.add_argument("--format", type=str, default="{:06}", help="output filename format")
parser.add_argument("--start_index", type=int, default=1, help="number from which filenames will start.")
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
START_INDEX = args.start_index # type: int

FILES_LIST = os.listdir(DATASET_DIRECTORY)
FILES_COUNT = len(FILES_LIST)

# instead of copying to out directory, rename files in dataset directory with the new name
RENAME_IN_DATASET_DIR = os.path.abspath(DATASET_DIRECTORY) == os.path.abspath(OUTPUT_DIRECTORY)

# renaming files
for i, filename in enumerate(FILES_LIST):
    print("Prcessing {}/{}".format(i + 1, FILES_COUNT))

    _, ext =  os.path.splitext(filename)
    new_filename = "{filename}{ext}".format(
        filename=OUT_FILENAME_FORMAT.format(i + START_INDEX),
        ext=ext
    )

    if RENAME_IN_DATASET_DIR:
        os.rename(os.path.join(DATASET_DIRECTORY, filename), os.path.join(OUTPUT_DIRECTORY, new_filename))
    else:
        copyfile(os.path.join(DATASET_DIRECTORY, filename), os.path.join(OUTPUT_DIRECTORY, new_filename))

