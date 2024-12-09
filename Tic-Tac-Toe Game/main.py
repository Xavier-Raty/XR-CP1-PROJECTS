# Xavier Raty Tic-Tac-Toe Game

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1] == board[2] and board[0] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return board[0][2]
    
    return None

def player_move(board):
     while True:
         try:
                move = int(input("Type 1-9 for your move: ")) - 1
                row, col = divmod(move, 3)
                if [board][col] == " ":
                     return row, col
                else:
                     print("That spot is already take, so try another place.")
                     print("You can't do that number, try another one.")

def 