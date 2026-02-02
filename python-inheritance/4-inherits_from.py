#!/usr/bin/python3
"""
Defines a function to check if an object is an instance
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    """
    return type(obj) is a_class
