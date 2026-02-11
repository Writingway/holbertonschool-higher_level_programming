#!/usr/bin/python3
"""Defines a function that writes an object to a text file using
JSON representation."""
import json


def save_to_json_file(my_obj, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
