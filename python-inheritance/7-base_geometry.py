#!/usr/bin/python3
"""
Defines an empty class BaseGeometry
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
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
