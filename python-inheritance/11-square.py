#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    def __init__(self, size):
        self.__size = size
        self.integer_validator("size", self.__size)
        super().__init__(size, size)

    def __str__(self):
        """
        Returns the string representation of the Rectangle
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
