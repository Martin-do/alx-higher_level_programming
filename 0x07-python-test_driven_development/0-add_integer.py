#!/usr/bin/python3

""" add_integer

Adds two integers (a, b) and returns integer sum
Floats get converted to integers, all others raise TypeError
"""


def add_integer(a, b=98):
    """ add_integer - adds two integers (a, b)
    Returns: integer sum
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b