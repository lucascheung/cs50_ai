"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x = 0
    o = 0
    for row in board:
        for m in row:
            if m == "X":
                x += 1
            if m == "O":
                o += 1
    return "O" if x > o else "X"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                result.add((i,j))
    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    new_board = copy.deepcopy(board)
    if board[i][j]:
        raise ValueError
    else:
        new_board[i][j] = player(board)
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    
    for m in ["XXX", "OOO"]:
        # horizontal
        for row in range(3):
            if board[row][0] == board[row][1] == board[row][2]:
                return board[row][0]
        # vertical
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col]:
                return board[0][col]
        # diagonal
        if board[0][0] == board[1][1] == board[2][2]:
            return board[1][1]
        if board[0][2] == board[1][1] == board[2][0]:
            return board[1][1]
    return None
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                return False
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    win = winner(board)
    if win == "X":
        return 1
    elif win == "O":
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    p = player(board)
    if p == "X":
        v, a = max_value(board)
        return a
    if p == "O":
        v, a = min_value(board)
        return a


def max_value(board):
    if terminal(board):
        return utility(board), None
    v = -2
    a = float('-inf')
    for action in actions(board):
        m, ac = min_value(result(board, action))
        if m > v:
            v = m
            a = action
            if v == 1:
                return v, a
    return v, a

def min_value(board):
    if terminal(board):
        return utility(board), None
    v = float('inf')
    a = None
    for action in actions(board):
        m, ac = max_value(result(board, action))
        if m < v:
            v = m
            a = action
            if v == -1:
                return v, a
    return v, a