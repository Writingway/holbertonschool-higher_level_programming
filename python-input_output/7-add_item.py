#!/usr/bin/python3
"""
Defines a script that adds all arguments to a Python list, and then save
"""
import sys
import json
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = sys.argv
filename = "add_item.json"
with open(filename, 'a', encoding="utf-8") as f:
    """Adds all arguments to a Python list, and then save them to a file."""
    try:
        my_list = load_from_json_file(filename)
    except Exception:
        my_list = []
    for i in range(1, len(args)):
        my_list.append(args[i])
    save_to_json_file(my_list, filename)
