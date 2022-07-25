#!/usr/bin/python3
"""solves the puzzle
Determines all possible solutions placing N
Example:
    $ ./101-nqueens.py N
N must be an integer grater than or equal to 4
Attributes:
    board (list): A list of lists rep the chess boad
    solutions (list): A list of lists having solutions
Solutions are rep in the format [[r, c], [r, c] [r, c]]
where r and c rep the row and column repsectively
queen must be placed on the chessboard
"""

import sys


def init_board(n):
    """initialize an `n`x`n` sized chessboard with 0's."""
    board = []
    [board.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in board]
    return (board)


def board_deepcopy(board):
    """rets a copy of the board."""
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return (board)


def get_solution(board):
    """ret the list of lists rep of solved chessboard"""
    solution = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                solution.append([r, c])
                break
    return (solution)


def xout(board, row, col):
    """X out spots on a chessboard.
    All spots where non-attacking queens can no longer be playes
    Args:
        board (list): The cur working chessboard
        row (int): The row where queen last played
        col (int): The col where a queen was last played.
    """

    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c == 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


    def recursive_solve(board, row, queens, solutions):
        """recursively solve the puzzle
        Args:
            board (list): The current working chessboard
            row (int): The current working row
            queens (int): the cur no of placed queens
            solutions (list): A list of lists of of solutions.
        Returns:
            solutions
        """
        if queens == len(board):
            solutions.append(get_solution(board))
            return (solutions)

        for c in range(len(board)):
            if board[row][c] == " ":
                tmp_board = board_deepcopy(board)
                tmp_board[row][c] = "Q"
                xout(tmp_board, row, c)
                solutions = recursive_solve(tmp_board, row + 1,
                                            queens + 1, solutions)
        return (solutions)


    if __name__ == "__main__":
        if len(sys.argv) != 2:
            print("Usage: nqueens N")
            sys.exit(1)
        if sys.argv[1].isdigit() is False:
            print("N must be a number")
            sys.exit(1)
        if int(sys.argv[1]) < 4:
            print("N must be atleast 4")
            sys.exit(1)

        board = init_board(int(sys.argv[1]))
        solutions = recursive_solve(board, 0, 0, [])
        for sol in solutions:
            print(sol)

