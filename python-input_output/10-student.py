#!/usr/bin/python3
"""Module that defines a Student class with filtered JSON output."""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student.

        Args:
            attrs (list): Attribute names to retrieve. If it is not a
                list of strings, all attributes are retrieved.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
