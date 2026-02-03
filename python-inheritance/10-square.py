#!/usr/bon/python3
Rectangle = __import__('9-rectangle').Rectangle
"""
Defines a class Square based on Rectangle
"""


class Square(Rectangle):
    def __init__(self, size):
        """
        Initializes a Square instance with size
        """
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)
