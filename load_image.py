# -*- coding: utf-8 -*-
import os
import glob

from tqdm import tqdm
from numpy import ndarray
import cv2


class LoadImage:

    def __init__(self, file_extension: str = 'bmp'):
        self.image_dir: str = os.pardir + '/MakeTrainingData/images'
        self.file_extension: str = file_extension

    def execute(self) -> tuple:
        """
        画像と画像のファイル名を読み込む
        Returns:
        
        """
        images: list = []
        file_names: list = []
        directories: list = os.listdir(self.image_dir)
        for directory in tqdm(directories):
            files: list = glob.glob(self.image_dir + "/" + directory + "/*.{}".format(self.file_extension))
            for file in files:
                image: ndarray = cv2.imread(file, cv2.IMREAD_COLOR)
                images.append(image)
                file_name = os.path.basename(file)
                file_names.append(file_name)

        return images, file_names
