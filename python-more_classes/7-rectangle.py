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
    number_of_instances = 0
    print_symbol = "#"

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
        self.number_of_instances += 1

    @property
    def width(self):
        """
        Returns the width getter.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Returns the width setter.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Returns the height getter.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Returns the height setter.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        rectangle_area = self.__height * self.__width
        return rectangle_area

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
        """
        if self.__height == 0 or self.__width == 0:
            return 0

        result_perimeter = 2 * (self.__height + self.__width)
        return result_perimeter

    def __str__(self):
        """
        Returns the string representation of the rectangle
        """
        result = []
        if not self.__height or self.__width == 0:
            return ("")

        for i in range(self.__height):
            result.append(str(self.print_symbol) * self.__width)
        return ("\n".join(result))

    def __repr__(self):
        """
        Returns the string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        Prints a message when an instance of Rectangle is deleted.
        """
        print("Bye rectangle...")
        self.number_of_instances -= 1
