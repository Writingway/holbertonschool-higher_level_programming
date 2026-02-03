#!/usr/bin/python3
"""
Defines a function to check if an object is an instance
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    else:
        return False
