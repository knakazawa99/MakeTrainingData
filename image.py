# -*- coding: utf-8 -*-

from numpy import ndarray


class Image:

    def __init__(self, image: ndarray, name: str) -> None:
        self.__image: ndarray = image
        self.__name: str = name

    @property
    def image(self) -> None:
        pass

    @image.getter
    def image(self) -> ndarray:
        return self.__image

    @property
    def name(self) -> None:
        pass

    @name.setter
    def name(self) -> str:
        return self.__name
