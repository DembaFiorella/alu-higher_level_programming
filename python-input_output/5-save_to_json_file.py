#!/usr/bin/python3
"""Module that defines a function to write an object to a JSON file."""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using its JSON representation.

    Args:
        my_obj: The object to serialize.
        filename (str): The path of the file to write to.
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
