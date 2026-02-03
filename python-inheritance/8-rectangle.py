#!/usr/bin/python3
"""
Defines an class BaseGeometry
"""


class BaseGeometry:
    """
    Empty class BaseGeometry
    """
    def area(self):
        """
        Raises an exception indicating that the area method is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))


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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        if not type(width) is int or width <= 0:
            raise TypeError("width must be an integer")
        if not type(height) is int or height <= 0:
            raise TypeError("height must be an integer")
