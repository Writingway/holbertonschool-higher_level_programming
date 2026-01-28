#!/usr/bin/python3
class Square:
    """
    Docstring for Square class.
    Represents a square with height and width attributes.
    """
    def __init__(self, size=0):
        """
        Initializes the square with a given size.
        Args:
        size (int): The size of the square's sides.
        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self._Square__size = size
