#!/usr/bin/python3
"""program that solves the N queens problem"""
import sys


def Backtracking(start, n, colones, pos, inv, board):
    """
    backtracking function to solve Nqueens problem
    """
    if start == n:
        result = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == 1:
                    result.append([i, j])
        print(result)
        return

    for k in range(n):
        if k in colones or (start + k) in pos or (start - k) in inv:
            continue

        colones.add(k)
        pos.add(start + k)
        inv.add(start - k)
        board[start][k] = 1
        Backtracking(start+1, n, colones, pos, inv, board)
        colones.remove(k)
        pos.remove(start + k)
        inv.remove(start - k)
        board[start][k] = 0


def nqueens(n):
    """
    resolution to nqueens problem
    Args:
        n (int): number of queens. Must be >= 4
    Return:
        List of lists every possible solution to the problem
    """
    colones = set()
    position_diagonal = set()
    inv_diag = set()
    board = [[0] * n for i in range(n)]

    Backtracking(0, n, colones, position_diagonal, inv_diag, board)


if __name__ == "__main__":
    args = sys.argv
    if len(args) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(args[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
