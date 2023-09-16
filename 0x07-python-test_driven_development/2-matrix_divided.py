#!/usr/bin/python3
# 2-matrix_divided.py

"""Defines a function of matrix division."""


def matrix_divided(matrix, div):
    """
    Divide all elements of a matrix by a number and round to 2 decimal places.

    Args:
        matrix (list of lists of int or float): The matrix to be divided.
        div (int or float): The number to divide the matrix elements by.

    Returns:
        list of lists of float: A new matrix with elements divided and rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats, or if div is not a number (int or float).
        TypeError: If each row of the matrix doesn't have the same size.
        ZeroDivisionError: If div is equal to 0.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(isinstance(num, (int, float)) for row in matrix for num in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number (integer or float)")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    row_sizes = [len(row) for row in matrix]
    if len(set(row_sizes)) != 1:
        raise TypeError("Each row of the matrix must have the same size")

    new_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return (new_matrix)
