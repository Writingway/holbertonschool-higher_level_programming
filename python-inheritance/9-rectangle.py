#!/usr/bin/python3
BaseGeometry = __import__('8-rectangle').BaseGeometry
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
