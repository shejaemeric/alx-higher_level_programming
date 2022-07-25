#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


"""tests"""

print(matrix_divided([[1,2],[3,4]], 5))
print(matrix_divided([[1.3,2.5],[3.4,4.5]], 5))
print(matrix_divided([[1,2],[3,4]], 5.3))
print(matrix_divided([[1.3,2.5],[3.4,4.5]], 5.2))

print(matrix_divided([[4,5],[77,4]], '6'))