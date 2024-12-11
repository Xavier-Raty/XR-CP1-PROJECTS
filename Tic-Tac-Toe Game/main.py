# Xavier Raty Tic-Tac-Toe Game

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*5)

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != " ":
            return board[i][0]
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] != " ":
            return board[0][i]
        
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
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    print("Welcome to the Tic-Tac-Toe game")
    print("You're X, Computer is O")
    print("To select a space, choose (0, 1, or 2)")
    print("E.x: '00' is the top-left corner.")

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
          print("Yay, you won!")
          break
            
         if is_board_full(board):
            print_board(board)
            print("It's a draw...")
            break
        
         print("Computer's turn:")
         row, col = computer_move(board)
         board[row][col] = "O"
        
         if check_winner(board) == "O":
            print_board(board)
            print("You just got beat by a computer")
            break

         if is_board_full(board):
            print_board(board)
            print("It's a ties")
            break


         if check_winner(board) == "X":
            print_board(board)
            print("Yay, you win!")
            break

tic_tac_toe()
