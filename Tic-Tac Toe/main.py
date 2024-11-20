#Yenesis Rabelo Tic-Tac-Toe ProficienyTest
with nested loop

import random

# function to print the board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# function to check for a winner
def check_winner(board, player):
    # checking rows, columns and diagonals
    for i in range(3):
        # check rows
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
        # check columns
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True
    # checking diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# function to check if the board is full 
def is_board_full(board):
    for row in board:
        if " " in row:
            return False
    return True

# function to get the user's move
def user_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            row, col = divmod(move, 3)
            if board[row][col] == " ":
                board[row][col] = "X"
                break
            else:
                print("That spot is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter a number between 1 and 9.")

# function to make the computer move
def computer_move(board):
    while True:
        move = random.randint(0, 8)
        row, col = divmod(move, 3)
        if board[row][col] == " ":
            board[row][col] = "O"
            break

# the main game loop
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]  #tic-tac-toe board 3x3
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the computer is O.")
    print("Instructions: Enter a number between 1 and 9 to place your X in the corresponding position on the board.")

    print_board(board)

    while True:
        # users turn
        user_move(board)
        print_board(board)
        if check_winner(board, "X"):
            print("You win!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

        # computers turn
        computer_move(board)
        print_board(board)
        if check_winner(board, "O"):
            print("Computer wins!")
            break
        if is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
