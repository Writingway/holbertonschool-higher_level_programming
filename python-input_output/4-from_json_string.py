#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string."""
    return json.loads(my_str)
