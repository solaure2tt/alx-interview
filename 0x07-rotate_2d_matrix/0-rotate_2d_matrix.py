#!/usr/bin/python3
""" Given an n x n 2D matrix, rotate it 90 degrees clockwise."""
from math import sqrt


def rotate_2d_matrix(matrix):
    """rotate a nxn matrice 90 degrees clockwise
        Args:
           matrix: matrix to rotate
        Return:
           matrix rotated
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
    for i in range(n):
        for j in range(n//2):
            temp = matrix[i][j]
            matrix[i][j] = matrix[i][n - j - 1]
            matrix[i][n - j - 1] = temp
