#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        count = len(row)
        index = 1
        for item in row:
            if index == count:
                print("{:d}".format(item), end="")
            else:
                print("{:d}".format(item), end=" ")
            index += 1
        print("")
