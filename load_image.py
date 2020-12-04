# -*- coding: utf-8 -*-
import os
import glob

from tqdm import tqdm
from numpy import ndarray
import cv2
import numpy as np


class LoadImage:

    def __init__(self):
        self.image_dir: str = os.pardir + '/MakeTrainingData/images'
        self.image_extension: str = 'tif'

    def execute(self) -> tuple:
        images: list = []
        file_names: list = []
        directories: list = os.listdir(self.image_dir)
        for directory in tqdm(directories):
            # files: list = glob.glob(self.image_dir + '/' + directory + "/*.".format(self.image_extension))
            files: list = glob.glob(self.image_dir + "/" + directory)
            for file in files:
                image: ndarray = cv2.imread(file, cv2.IMREAD_COLOR)
                images.append(image)
                file_name = os.path.basename(file)
                file_names.append(file_name)

        return images, file_names

