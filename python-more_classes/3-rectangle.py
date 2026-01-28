#!/usr/bin/python3
"""
This module defines a Rectangle class.
"""


class Rectangle:
    """
    Rectangle class.
    width: width of the rectangle
    height: height of the rectangle
    """
    def __init__(self, width=0, height=0):
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """
        Method for width getter.
        :param self: self
        :return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Method for width setter.
        :param self: self
        :param value: value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Method for height getter.
        :param self: self
        :return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Method for height setter.
        :param self: self
        :param value: value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Method for area
        :param self: self
        """
        rectangle_area = self.__height * self.__width
        return (rectangle_area)

    def perimeter(self):
        """
        Method for perimeter
        :param self: self
        """
        if not self.__height or self.__width == 0:
            result_perimeter = 0
            return (result_perimeter)

        result_perimeter = 2 * (self.__height + self.__width)
        return (result_perimeter)

    def __str__(self):
        """
        Method for perimeter
        :param self: self
        """
        result = []
        if not self.__height or self.__width == 0:
            return ("")

        for i in range(self.__height):
            result.append("#" * self.__width)
        return ("\n".join(result))
