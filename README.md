# Multiclass-Semantic-Segmentation-Duckietown-Dataset
A dataset of multiclass semantic segmentation image annotations for the first 250 images of the ["Duckietown Object Detection Dataset"](https://docs.duckietown.org/daffy/AIDO/out/object_detection_dataset.html).

| Raw Image | Segmentated Image |
| --- | --- |
| ![raw_image]() | ![segmented_image]() |


# Usage

*Notice*: Due to the rather large size of the original dataset (~750MB), this repository only contains annotations file stored in *CVAT for Images 1.1* format as well as two python files:
- `cvat_preprocessor.py`: A collection of helper functions to read the annotations file and extract the annotation masks stored as polygons.
- `dataloader.py`: A _PyTorch_-specific example implementation of a wrapper-dataset to use with PyTorch machine learning models. 
