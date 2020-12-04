# -*- coding: utf-8 -*-
import os
import sys

from MakeTrainingData.load_image import LoadImage
from MakeTrainingData.load_json import LoadJson
from MakeTrainingData.make_training_data import MakeTrainingData

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))


def main() -> None:
    """

    Returns: None

    """
    load_image = LoadImage()
    load_json = LoadJson()
    make_training_data = MakeTrainingData()

    images, file_names = load_image.execute()
    json_files = load_json.execute()
    make_training_data.execute(images, file_names, json_files)

    return None


if __name__ == '__main__':
    main()
