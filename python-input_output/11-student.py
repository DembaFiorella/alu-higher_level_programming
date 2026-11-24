#!/usr/bin/python3
"""Defines a Student class."""

class Student:
    """Defines a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return the dictionary representation of a Student."""
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: value
                for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__.copy()

    def reload_from_json(self, json):
        """Replace all attributes using a dictionary."""
        self.__dict__.clear()
        self.__dict__.update(json)
