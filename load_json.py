# -*- coding: utf-8 -*-
import os
import json

from tqdm import tqdm


class LoadJson:

    def __init__(self):
        self.file_dir: str = os.pardir + '/MakeTrainingData/json_files'
        self.file_extension: str = 'json'

    def execute(self):
        json_files: list = []
        files: list = os.listdir(self.file_dir)
        for file in tqdm(files):
            if not file.endswith(self.file_extension):
                continue

            with open(self.file_dir + "/" + file) as f:
                json_load = json.load(f)

            regions = []
            for region in json_load['regions']:
                bounding_box: dict = self.__get_bounding_box(region)
                regions.append(bounding_box)

            json_file: dict = {
                'file_name': json_load['asset']['name'],
                'regions': regions
            }
            json_files.append(json_file)
        return json_files

    @staticmethod
    def __get_bounding_box(region: dict) -> dict:
        height: float = region['boundingBox']['height']
        width: float = region['boundingBox']['width']
        top: float = region['boundingBox']['top']
        left: float = region['boundingBox']['left']
        under: float = top + height
        right: float = left + width

        bounding_box: dict = {
            'under': under,
            'top': top,
            'left': left,
            'right': right,
            'label': region['tags'][0]
        }
        return bounding_box
