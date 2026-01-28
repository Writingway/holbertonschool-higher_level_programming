#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    Docstring for Rectangle class.
    """
    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        Docstring for width getter.
        :param self: self
        :return: width
        """
        return (self.__width)

    @width.setter
    def width(self, value):
        """
        Docstring for width setter.
        :param self: self
        :param value: value
        """
        if not isinstance(self.__width, int):
            raise TypeError("size must be an integer")
        if self.__width < 0:
            raise ValueError("size must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Docstring for height getter.
        :param self: self
        :return: height
        """
        return (self.__height)

    @height.setter
    def height(self, value):
        """
        Docstring for height setter.
        :param self: self
        :param value: value
        """
        if not isinstance(self.__height, int):
            raise TypeError("size must be an integer")
        if self.__height < 0:
            raise ValueError("size must be >= 0")
        self.__height = value
