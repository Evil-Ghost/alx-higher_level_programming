#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if matrix is None or matrix == [[]]:
        print()
        return

    for x in range(len(matrix)):
        for y in range(len(matrix[x])):
            if y != len(matrix[x]) - 1:
                print("{:d}".format(matrix[x][y]), end=' ')
            else:
                print("{:d}".format(matrix[x][y]))