#!/usr/bin/python3
"""Module that defines a Square class based on Rectangle."""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """A class that represents a square."""

    def __init__(self, size):
        """Initialize a Square after validating its size.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size
