#!/usr/bin/python3
"""that returns an object (Python data structure)
represented by a JSON string
"""
import json


def from_json_string(my_str):
    """  returns an object (Python data structure)
    represented by a JSON string

    Args:
        my_str (JSON): JSON string

    Returns:
        obj: object
    """
    return json.loads(my_str)
