#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for col_index, col_value in enumerate(row):
            if col_index != 0:
                print(" ", end="")
            print("{:d}".format(col_value), end="")
        print()
