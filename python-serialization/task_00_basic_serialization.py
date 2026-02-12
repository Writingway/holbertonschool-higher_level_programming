#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize Python objects
using the JSON format.
"""
import json


def serialize_and_save_to_file(data, filename):
    with open(filename, "w") as file:
        new_dump = json.dump(data, file)
        return new_dump


def load_and_deserialize(filename):
    with open(filename, "r") as file:
        new_load = json.load(file)
        return new_load
