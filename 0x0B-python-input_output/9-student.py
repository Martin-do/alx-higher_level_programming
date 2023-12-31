#!/usr/bin/python3
"""A Student class"""


class Student:
    """Student class"""
    def __init__(self, first_name, last_name, age):
        """__init__ constructor method
        Args:
            first_name (str): first name
            last_name (str): last name
            age (int): age of student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
