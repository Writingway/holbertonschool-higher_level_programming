#!/usr/bin/python3
"""
Defines an class Rectangle base on BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Represents a rectangle shape
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
