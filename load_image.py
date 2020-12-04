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
        files: list = glob.glob(self.image_dir + "/*.{}".format(self.file_extension))

        for file in tqdm(files):
            image: ndarray = cv2.imread(file, cv2.IMREAD_COLOR)
            images.append(image)
            file_name: str = os.path.basename(file)
            file_names.append(file_name)

        return images, file_names
