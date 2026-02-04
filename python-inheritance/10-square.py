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
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        Calculates and returns the area of the Square
        """
        return self.__size ** 2
