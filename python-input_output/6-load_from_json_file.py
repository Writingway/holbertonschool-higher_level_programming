#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""
import json


def load_from_json_file(filename):
    """Reads a text file and prints it to stdout."""
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
