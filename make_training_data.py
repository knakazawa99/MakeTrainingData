# -*- coding: utf-8 -*-
import os

from numpy import ndarray
import cv2

from config import SAVE_TRAINING_DIR


class MakeTrainingData:

    def __init__(self, file_extension: str = 'bmp'):
        self.save_path: str = SAVE_TRAINING_DIR
        self.file_extension: str = file_extension

    def execute(self, images: list, file_names: list, json_files: list) -> None:
        return self.__make_training_data(images, file_names, json_files)

    def __make_training_data(self, images: list, file_names: list, json_files: list) -> None:
        """

        Args:
            images(list): 画像のリスト
            file_names: 画像ファイルの名前のリスト
            json_files: バウンディングボックスのjsonをロードして，座標とラベルを入れてある

        Returns:

        """
        for index, image in enumerate(images):
            for json_file in json_files:
                if file_names[index] == json_file['file_name']:
                    self.__save_training_data(image, file_names[index], json_file)
        return None

    def __save_training_data(self, image: ndarray, file_name: str, json_file: dict) -> None:
        """

        Args:
            image(ndarray): 画像
            file_name(str): 画像ファイルの名前
            json_file(dict): バウンディングボックスのデータ
        Returns:

        """
        for index, region in enumerate(json_file['regions']):
            save_image: ndarray = image[int(region['top']): int(region['under']), int(region['left']): int(region['right'])]
            save_dir: str = self.save_path + "/{}/".format(region['label'])
            if not os.path.isdir(save_dir):
                os.mkdir(save_dir)
            cv2.imwrite(save_dir + "{}_{}.{}".format(file_name, index, self.file_extension), save_image)

        return None





