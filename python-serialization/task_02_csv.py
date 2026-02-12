#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            with open("data.json", "w") as json_file:
                json.dump(data, json_file)
        return True
    except Exception:
        return False
