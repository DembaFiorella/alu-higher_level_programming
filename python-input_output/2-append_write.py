#!/usr/bin/python3
"""Module that defines a function to append a string to a text file."""


def append_write(filename="", text=""):
    """Append a string at the end of a UTF8 text file.

    Args:
        filename (str): The path of the file to append to.
        text (str): The string to append.

    Returns:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
