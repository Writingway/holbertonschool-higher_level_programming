#!/usr/bin/python3
class Square:
    """
    Docstring for Square class.
    Represents a square with height and width attributes.
    Attributes:
        height (str): The height of the square. Default is "0".
        width (str): The width of the square. Default is "0".
    """
    def __init__(self, height="0", width="0"):
        """
        Docstring for __init__
        Initializes a Square instance with height and width.
        :param self: self
        :param height:
        The height of the square. Default is "0".
        :param width:
        The width of the square. Default is "0".
        """
        self.height = height
        self.width = width
