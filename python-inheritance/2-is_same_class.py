#!/usr/bin/python3
"""
Module that defines a function to check
if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if obj is exactly an instance of a_class.
    Returns True if it is, False otherwise.
    """
    return type(obj) is a_class
