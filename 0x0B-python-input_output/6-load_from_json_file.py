#!/usr/bin/python3
"""creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """crate and object from a "JSON file" """
    with open(filename, 'r', encoding="UTF-8") as json_data:
        read_data = json.load(json_data)
    return read_data
