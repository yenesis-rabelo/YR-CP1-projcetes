#Yenesis Rabelo Tic-Tac-Toe ProficienyTest

import random

#initialize the board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

#print the board using a nested for loop
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 5)

#check forthe winner
def check_winner(board, player):
    #check the rows, columns, and diagonals
    for i in range(3):
        if all([board[i][j] == player for j in range(3)]):  #check row
            return True
        if all([board[j][i] == player for j in range(3)]):  #check column
            return True

    #check the diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False

#check if the board is full
def board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

#function to let the user make a move
def user_move(board):
    while True:
        try:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))
            if board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input! Please enter numbers between 0 and 2.")

#function to let the computer make a move
def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == ' ':
            board[row][col] = 'O'
            print(f"Computer plays O at ({row}, {col})")
            break

#the main game loop
def play_game():
    board = initialize_board()
    current_player = 'X'  #user starts the game

    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    print("To play, enter a row and column number (0-2) when prompted.")
    print("The game will end when one player wins or the board is full.")

    while True:
        print_board(board)

        if current_player == 'X':
            print("Your turn!")
            user_move(board)
            if check_winner(board, 'X'):
                print_board(board)
                print("Congratulations! You win!")
                break
            current_player = 'O'
        else:
            print("Computer's turn!")
            computer_move(board)
            if check_winner(board, 'O'):
                print_board(board)
                print("Computer wins! Better luck next time.")
                break
            current_player = 'X'

        if board_full(board):
            print_board(board)
            print("It's a draw!")
            break

#start the game
play_game()
