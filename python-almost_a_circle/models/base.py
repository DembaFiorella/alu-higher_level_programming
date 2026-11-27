#!/usr/bin/python3
"""Module base: defines the Base class."""


class Base:
    """Base class that manages the id attribute of all other classes."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new Base.

        Args:
            id (int): The id of the new Base. If None, an id is
                assigned automatically.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
