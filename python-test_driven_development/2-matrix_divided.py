#!/usr/bin/python3
"""Module 2-matrix_divided: defines a function that divides a matrix."""


def matrix_divided(matrix, div):
    """Divide all elements of a matrix by div, rounded to 2 decimal places.

    matrix must be a list of lists of integers or floats, and each row
    must have the same size. div must be a number and cannot be 0.
    Returns a new matrix.
    """
    msg = "matrix must be a matrix (list of lists) of integers/floats"
    if not isinstance(matrix, list) or matrix == []:
        raise TypeError(msg)
    for row in matrix:
        if not isinstance(row, list) or row == []:
            raise TypeError(msg)
        for n in row:
            if not isinstance(n, (int, float)):
                raise TypeError(msg)
    size = len(matrix[0])
    for row in matrix:
        if len(row) != size:
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
