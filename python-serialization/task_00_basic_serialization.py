#!/usr/bin/python3
"""
This module provides functions to serialize and deserialize Python objects
using the JSON format.
"""
import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, "wb") as file:
        new_dump = pickle.dump(data, file)
        return new_dump


def load_and_deserialize(filename):
    with open(filename, "rb") as file:
        new_load = pickle.load(file)
        return new_load
