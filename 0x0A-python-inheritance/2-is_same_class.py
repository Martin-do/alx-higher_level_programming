#!/usr/bin/python3


def is_same_class(obj, a_class):
    """checks if an object is exact instance of
    specified class

    Args:
        obj (object): object
        a_class (class): class to compare to

    Returns:
        bool: True if an instance or False if otherwise
    """
    if type(obj).__name__ == a_class.__name__:
        return True
    return False
