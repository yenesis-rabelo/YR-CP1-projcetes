#Yenesis Rabelo Tic-Tac-Toe ProficienyTest

import random
#function to initialize the board
def initialize_board():
    return [[" " for _ in range(3)] for _ in range(3)]

#function to print the board
"""Print the current state of the board using a nested loop."""
print("Current Board:")
for row in board:
    for cell in row:
        print(cell, end="|")
        print() #move to the next kine after a row
        print("-" * 5)
        
#function to check for a winner
def check_winner(board):
    #check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]  #return X or O winner
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]  #5eturn X or O winner
    
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]  #return X or O winner
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]  #return X or O winner
    
    #check if the board is full 
    for row in board:
        if " " in row:
            return None  #game is still ongoing
    
    return "Draw"  #no winner and no empty spaces it's a draw

#function to handle the users move
def player_move(board):
    while True:
        try:
            row, col = map(int, input("Enter your move (row and column) as two numbers from 0-2 separated by a space: ").split())
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That space is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter numbers between 0 and 2 for both row and column.")

#function to handle the computers move
def computer_move(board):
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

#main game function
def play_game():
    board = initialize_board()
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'X' and the computer is 'O'.")
    
    while True:
        print_board(board)
        
        #players turn
        player_move(board)
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "X":
                print("Congratulations! You win!")
            elif winner == "O":
                print("Sorry, the computer wins!")
            else:
                print("It's a draw!")
            break
        
        #computers turn
        print("Computer's turn...")
        computer_move(board)
        winner = check_winner(board)
        if winner:
            print_board(board)
            if winner == "X":
                print("Congratulations! You win!")
            elif winner == "O":
                print("Sorry, the computer wins!")
            else:
                print("It's a draw!")
            break
