#!/usr/bin/python3
"""LockedClass - with no class or object attribute,
    that prevents the user from dynamically creating
    new instance attributes, except if the new instance
    attribute is called first_name
"""


class LockedClass:
    """A lockedClass object preventing dynamic creation
    of attributes other than "first_name"
    """
    __slots__ = ['first_name']
