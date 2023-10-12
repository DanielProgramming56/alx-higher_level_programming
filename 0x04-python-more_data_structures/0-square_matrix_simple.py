#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    squ_matrix = []

    for row in matrix:
        new_row = []

        for element in row:
            new_row.append(element ** 2)

        squ_matrix.append(new_row)
    return squ_matrix
