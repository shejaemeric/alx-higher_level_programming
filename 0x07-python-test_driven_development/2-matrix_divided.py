#!/usr/bin/python3
"""
    module to divide a matrix
"""

from decimal import DivisionByZero


def matrix_divided(matrix, div):
    """
    matrix_divided by div

    Args:
        matrix (list[list[int/float]]): matrix
        div (int): divident
    """
    newRow = []
    newMatrix = []

    counter = len(matrix[1])
    same = True


    if type(div) not in (int, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise DivisionByZero("division by zero")

    for row in matrix:
        for item in row:
            if type (item) not in (int, float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if not counter == len(row):
            same = False
    
    if not same:
        raise TypeError("Each row of the matrix must have the same size")

    for row in matrix:
        newRow = []
        for item in row:
            item = item / div
            newRow.append(round(item, 2))
        newMatrix.append(newRow)
    
    return newMatrix
            