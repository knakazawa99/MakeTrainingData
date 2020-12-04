# -*- coding: utf-8 -*-
import os
import sys
import glob

from tqdm import tqdm
import cv2
from numpy import ndarray

sys.path.append(os.path.join(os.path.dirname(__file__), os.pardir))


IMAGE_DIR = os.pardir + '/MakeTrainingData/original_images'
SAVE_DIR = os.pardir + '/MakeTrainingData/images'
IMAGE_EXTENSION = 'bmp'


def main():
    directories: list = os.listdir(IMAGE_DIR)
    count: int = 1
    for directory in tqdm(directories):
        files: list = glob.glob(IMAGE_DIR + '/' + directory + "/*.{}".format(IMAGE_EXTENSION))
        for index, file in enumerate(files):
            image: ndarray = cv2.imread(file, cv2.IMREAD_COLOR)
            cv2.imwrite(SAVE_DIR + "/{}_{}.{}".format(count, index+1, IMAGE_EXTENSION), image)

        count += 1


if __name__ == '__main__':
    main()
