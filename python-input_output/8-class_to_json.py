#!/usr/bin/python3
"""Module that defines a function to get the dictionary of an object."""


def class_to_json(obj):
    """Return the dictionary description of an object for JSON.

    Args:
        obj: An instance of a class with serializable attributes.
    """
    return obj.__dict__
