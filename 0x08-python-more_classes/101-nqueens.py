#!/usr/bin/python3
import sys


def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check if it's safe to place a queen in this position
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def solve(board, col, solutions):
        # Base case: If all queens are placed, add the solution to the list
        if col >= n:
            solutions.append(board[:])
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                solve(board, col + 1, solutions)

    board = [-1] * n  # Initialize the board as a list of length n with -1s
    solutions = []

    solve(board, 0, solutions)

    # Print all solutions
    ls = []
    for solution in solutions:
        for row in solution:
            ls.append([row, solution.index(row)])
        print(ls)
        ls.clear()


# Example usage for solving the 8-Queens puzzle
def main():
    """driver function to run the program"""
    if len(sys.argv) != 2:
        print("Usage: nqueens N\n")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)
    else:
        n = int(sys.argv[1])
        solve_n_queens(n)


main()
