#!/usr/bin/python3
"""
This module defines a Square class.
"""


class Square:
    """
    Square class.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes the square with a given size.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    def area(self):
        """
        Calculates the area of the square.
        """
        square_area = self.__size * self.__size
        return square_area

    @property
    def size(self):
        """
        Calculates the area of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the area of the square.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Gets the position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square.
        """
        if isinstance(value, tuple) == 2:
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")

    def my_print(self):
        """
        method for print the square with the # character
        """
        if self.__size == 0:
            print("")
            return
        if self.__position[1] > 0:
            for _ in range(self.__position[1]):
                print("")
        for i in range(self.__size):
            if self.__position[0] > 0:
                print("_" * self.__position[0], end="")
            print("#" * self.__size)
