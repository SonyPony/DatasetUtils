# Dataset utils

Set of utilities for the dataset preprocessing.

## Renaming dataset files

Utility to rename files in dataset to number format for example `"foo.png"` -> `"0002.png"`. An example of calling renaming script:
``` 
$ python3 rename.py test/dataset_sample --start_index 2 --format {:03} --output_directory test/dataset_sample_out
```

where files will be renamed as follows:

```
"test/dataset_sample/foo.png"   -> "test/dataset_sample_out/002.png"
"test/dataset_sample/fooaa.png" -> "test/dataset_sample_out/003.png"
"test/dataset_sample/fu.png"    -> "test/dataset_sample_out/004.png"
```

Arguments `--start_index`, `--output_directory` and `--format` are optional. They specify output file format as follows:

```
--start_index       number name of the first image, default value is 1
--format python     style formatter with a single input (number), default value is {:06}
--output_directory  specifies output directory, if not specified, output directory is set to 
                    dataset directory. If output directory is same as the dataset directory, files
                    are only renamed (moved) instead of copied.

```

## Transpose images with EXIF orientation

Utility to transpose images according to EXIF orientation tag. If tag is not present, image is not transposed. An example of calling transpose script:

 ```
 $ python3 exif_transposer.py test/dataset_sample --output_directory test/dataset_sample_out
 ```

 ```
--output_directory  is optional and specifies the output directory, if not specified, output 
                     directoryis set to dataset directory. If output directory is same as the 
                     dataset directory, files are only renamed (moved) instead of copied.
```
