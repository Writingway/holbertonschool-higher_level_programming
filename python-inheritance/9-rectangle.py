#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""
Defines an class Rectangle base on BaseGeometry
"""


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
        if not type(width) is int or width <= 0:
            raise TypeError("width must be an integer")
        if not type(height) is int or height <= 0:
            raise TypeError("height must be an integer")

    def area(self):
        """
        Calculates and returns the area of the Rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns the string representation of the Rectangle
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
