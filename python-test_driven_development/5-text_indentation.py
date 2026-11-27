#!/usr/bin/python3
"""Module 5-text_indentation: defines a function that indents text."""


def text_indentation(text):
    """Print a text with 2 new lines after each of the characters . ? :

    text must be a string, otherwise a TypeError is raised. There is no
    space at the beginning or at the end of each printed line.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    line = ""
    for char in text:
        line += char
        if char in ".?:":
            print(line.strip(" "))
            print()
            line = ""
    print(line.strip(" "), end="")
