#!/usr/bin/python3
"""Module 0-add_integer: defines a function that adds 2 integers."""


def add_integer(a, b=98):
    """Add two integers and return the result.

    a and b must be integers or floats. Floats are cast to integers.
    Raises a TypeError if a or b is not an integer or a float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
