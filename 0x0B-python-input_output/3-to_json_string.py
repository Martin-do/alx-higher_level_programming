#!/usr/bin/python3
"""returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """ returns the JSON representation of an object (string)

    Args:
        my_obj (object): list, dict, etc object

    Returns:
        strs: json representation
    """
    return json.dumps(my_obj)
