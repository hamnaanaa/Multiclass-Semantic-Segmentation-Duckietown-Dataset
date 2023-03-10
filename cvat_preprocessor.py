import xml.etree.ElementTree as ET


class CVATPreprocessor():
    """Helper class to preprocess annotations in `CVAT for images 1.1` XML-encoded format"""
    @staticmethod
    def get_all_image_names(annotation_path):
        """Returns a list of all image names present in the annotation file"""
        annotations = ET.parse(annotation_path).getroot()
        images = annotations.findall("image")
        return [image.attrib["name"] for image in images]

    @staticmethod
    def get_all_image_polygons(image_name, annotation_path):
        """
        Returns a dictionary of all polygons for the given image name.
        The key is the label and the value is a list of polygons (= each a list of points) associated with that label.
        """
        annotations = ET.parse(annotation_path).getroot()
        image = annotations.find(f"image[@name='{image_name}']")
        raw_polygons = image.findall("polygon")
        
        # Extract the label and the raw points for each polygon, 
        # parse the points to (x, y) and store each label-polygon pair in a list
        processed_polygons = {}
        for raw_polygon in raw_polygons:
            label, points = raw_polygon.attrib["label"], raw_polygon.attrib["points"].split(";")
            # Parse the points to (x, y) int pairs
            points = [(int(float(point.split(",")[0])), int(float(point.split(",")[1]))) for point in points]
            processed_polygons[label] = processed_polygons.get(label, []) + [points]

        return processed_polygons


if __name__ == "__main__":
    # Example usage
    PATH_TO_ANNOTATIONS = "offline learning/semantic segmentation/data/annotations/"
    PATH_TO_IMAGES = "offline learning/semantic segmentation/data/frames/"
    CVAT_XML_FILENAME = "segmentation_annotation.xml"
    imgs = CVATPreprocessor.get_all_image_names(PATH_TO_ANNOTATIONS + CVAT_XML_FILENAME)
    polygons = CVATPreprocessor.get_all_image_polygons(imgs[0], PATH_TO_ANNOTATIONS + CVAT_XML_FILENAME)
    print(f"Loaded {len(imgs)} images from {PATH_TO_ANNOTATIONS + CVAT_XML_FILENAME}")
    print(f"Image '{imgs[0]} has {len(polygons)} polygon categories")
