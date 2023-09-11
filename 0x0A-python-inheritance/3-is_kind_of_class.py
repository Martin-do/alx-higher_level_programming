#!/usr/bin/python3


def is_kind_of_class(obj, a_class):
    """checks if object is an instance of or an instance
    of a class inherited from the specified class

    Args:
        obj (object): object
        a_class (class): class to compare

    Returns:
        bool: True if an instance or False if otherwise
    """
    if isinstance(obj, a_class):
        return True
    return False
