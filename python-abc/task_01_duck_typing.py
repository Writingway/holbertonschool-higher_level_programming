#!/usr/bin/python3
"""
This module demonstrates duck typing with Shape classes.
"""


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    Abstract base class for shapes.
    """
    @abstractmethod
    def area(self):
        """
        Method to compute area.
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        Method to compute perimeter.
        """
        pass


class Circle(Shape):
    """
    Circle shape class.
    """
    def __init__(self, radius):
        """
        Initialize Circle with radius.
        """
        self.radius = radius

    def area(self):
        """
        Compute area of the circle.
        """
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """
        Compute perimeter of the circle.
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    Rectangle shape class.
    """
    def __init__(self, width, height):
        """
        Initialize Rectangle with width and height.
        """
        self.width = width
        self.height = height

    def area(self):
        """
        Compute area of the rectangle.
        """
        return self.width * self.height

    def perimeter(self):
        """
        Compute perimeter of the rectangle.
        """
        return 2 * (self.width + self.height)


def shape_info(cls):
    """
    Print area and perimeter of the shape.
    """
    print("Area: {}".format(cls.area()))
    print("Perimeter: {}".format(cls.perimeter()))

"""
Testing the classes and function
"""
circle = Circle(radius=8)
rectangle = Rectangle(width=3, height=4)
shape_info(circle)
shape_info(rectangle)
