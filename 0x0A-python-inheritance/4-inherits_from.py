#!/usr/bin/python3


def inherits_from(obj, a_class):
    """checks if object is an instance of a class
    that inherited (directly or indirectly) from the specified class

    Args:
        obj (object): object
        a_class (class): class to compare

    Returns:
        bool: True if an instance or False if otherwise
    """
    if issubclass(type(obj), a_class):
        if type(obj) is not a_class:
            return True
    return False
