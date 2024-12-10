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
                row, col = (move, 3)
                if [board][col] == " ":
                     return row, col
                else:
                     print("That spot is already taken, try another place")
            except:
                     print("You can't do that number, try another one")

def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

def computer_move(board):
     empty_space = [(x, y) for x in range(3) for y in range(3) if board[x][y] == " "]
     return random.choice(empty_space)

def tic_tac_toe():
    # Initialize the board
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("Welcome to the Tic-Tac-Toe game")
    print("You're X, Computer is O")
    print("To select a space, choose (0, 1, or 2)")
    print("E.x: '0 0' is the top-left corner.")

    while True: 
         print_board(board)
         try:
            row, col = map(int, input("Enter your move (row and column): "))
            if board[row][col] != " ":
                 print("This spot is already taken, try another place")
                 continue
         except:
              print("You can't do that number, try another one")
              continue
         
         board[row][col] = "X"

         if check_winner(board) == "X":
            print_board(board)
            print("Yay, you win!")
            break