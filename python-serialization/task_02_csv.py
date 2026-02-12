#!/usr/bin/python3

import csv
import json


def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, 'r') as f:
            reader = csv.DictReader(f)
            data = [row for row in reader]
            return json.dumps(data)
        return True
    except Exception:
        return False
