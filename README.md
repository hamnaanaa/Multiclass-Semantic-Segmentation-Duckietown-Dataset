# Multiclass-Semantic-Segmentation-Duckietown-Dataset
A dataset of multiclass semantic segmentation image annotations for the first 250 images of the ["Duckietown Object Detection Dataset"](https://docs.duckietown.org/daffy/AIDO/out/object_detection_dataset.html).

| Raw Image | Segmentated Image |
| --- | --- |
| <img width="915" alt="raw_image" src="https://user-images.githubusercontent.com/42655977/211690204-301193c3-a651-4a3a-bd66-6458cf3a8778.png"> | <img width="915" alt="segmentation_mask" src="https://user-images.githubusercontent.com/42655977/211690212-2c9ca63a-f3ae-4d65-a4e0-ea76b20a616f.png"> |


# Usage

*Notice*: Due to the rather large size of the original dataset (~750MB), this repository only contains annotations file stored in *CVAT for Images 1.1* format as well as two python files:
- `cvat_preprocessor.py`: A collection of helper functions to read the annotations file and extract the annotation masks stored as polygons.
- `dataloader.py`: A _PyTorch_-specific example implementation of a wrapper-dataset to use with PyTorch machine learning models. 
