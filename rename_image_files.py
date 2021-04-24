# -*- coding: utf-8 -*-
import os
import glob

from tqdm import tqdm
import cv2
from numpy import ndarray

from config import IMAGE_DIR, SAVE_DIR, IMAGE_EXTENSION


def main():
    directories: list = os.listdir(IMAGE_DIR)
    count: int = 1
    for directory in tqdm(directories):
        print(directory)
        files: list = glob.glob(IMAGE_DIR + '/' + directory + "/*.{}".format(IMAGE_EXTENSION))
        for index, file in enumerate(files):
            image: ndarray = cv2.imread(file, cv2.IMREAD_COLOR)
            cv2.imwrite(SAVE_DIR + "/{}_{}.{}".format(directory, index+1, IMAGE_EXTENSION), image)

        count += 1


if __name__ == '__main__':
    main()
