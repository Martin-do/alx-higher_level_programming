#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, 'r', encoding="UTF-8") as json_data:
        read_data = json.load(json_data)
    return read_data
