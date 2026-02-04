#!/usr/bin/python3
"""
Defines a class Square based on Rectangle
"""


Rectangle = __import__('10-square').Rectangle


class Square(Rectangle):
    """
    Represents a square, inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a Square instance with size
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
