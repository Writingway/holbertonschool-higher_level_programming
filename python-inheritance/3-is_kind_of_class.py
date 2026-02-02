#!/usr/bin/python3
"""
Defines a function to check if an object is an instance
of a class or its subclass.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if obj is an instance of a_class or its subclass.
    Returns True if it is, False otherwise.
    """
    return isinstance(obj, a_class)
