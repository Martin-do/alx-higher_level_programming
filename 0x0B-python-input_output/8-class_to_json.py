#!/usr/bin/python3
"""a function that returns the dictionary description"""
import json


def class_to_json(obj):
    """Serialize class attributes to dictionary
    Args:
        obj (object): object to be serialized
    """
    return (obj.__dict__)
