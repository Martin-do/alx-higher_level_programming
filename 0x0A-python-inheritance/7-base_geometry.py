#!/usr/bin/python3
""" BaseGeometry class"""


class BaseGeometry:
    """BaseGeometry class"""
    def area(self):
        """area not implemented

        Raises:
            Exception: an error message
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
