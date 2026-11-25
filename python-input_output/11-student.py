#!/usr/bin/python3
"""Module that defines a class Student with JSON serialization."""


class Student:
    """A class that defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student with a first name, last name and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of the student.

        If attrs is a list of strings, only those attributes are kept.
        """
        if type(attrs) is list and all(type(a) is str for a in attrs):
            return {k: v for k, v in self.__dict__.items() if k in attrs}
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes of the student from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
