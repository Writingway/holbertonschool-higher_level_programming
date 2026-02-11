#!/usr/bin/python3
"""Defines a function that write a text file"""


def write_file(filename="", text=""):
    """Writes a text file and returns the number of characters written."""
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(text)
