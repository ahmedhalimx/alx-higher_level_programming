#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for m_row in matrix:
        for m_column in m_row:
            print("{:d}".format(m_column), end=" " if m_column != m_row[-1] else "")
        print()
