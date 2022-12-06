#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for x in matrix:
        i = ""
        for y in x:
            print("{:s}{:d}".format(i, y), end='')
            i = " "
        print()
