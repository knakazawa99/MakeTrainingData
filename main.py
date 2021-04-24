# -*- coding: utf-8 -*-
import os
import sys

from load_image import LoadImage
from load_json import LoadJson
from make_training_data import MakeTrainingData

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))

IMAGE_FILE_EXTENSION = 'bmp'


def main() -> None:
    """

    Returns: None

    """
    load_image = LoadImage(file_extension=IMAGE_FILE_EXTENSION)
    load_json = LoadJson()
    make_training_data = MakeTrainingData(file_extension=IMAGE_FILE_EXTENSION)

    images, file_names = load_image.execute()
    json_files = load_json.execute()
    make_training_data.execute(images, file_names, json_files)

    return None


if __name__ == '__main__':
    main()
