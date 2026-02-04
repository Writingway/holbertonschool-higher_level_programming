#!/usr/bon/python3
"""
Module that creates a Square class based on Rectangle.
"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Represents a class of a square
    """

    def __init__(self, size):
        """
        Initializes a Square instance with size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the Square
        """
        return self.__size * self.__size
