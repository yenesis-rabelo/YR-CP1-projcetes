#Yenesis Rabelo Rock, Paper, Scissors ProficienyTest 

import random

# function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "win"
    else:
        return "lose"

# function to display the game result and update scores
def play_game():
    # initialize the scores
    user_score = 0
    computer_score = 0
    ties = 0
    
    # main game loop
    while True:
        # display current score
        print(f"Score - You: {user_score} | Computer: {computer_score} | Ties: {ties}")
        
        # get user input
        user_choice = input("Enter 'rock', 'paper', or 'scissors' (or 'exit' to quit): ").lower()

        # check for exit condition
        if user_choice == "exit":
            print("Thanks for playing!")
            break

        # validate user input
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid input! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        # randomly selecting the computer's choice
        computer_choice = random.choice(["rock", "paper", "scissors"])

        # determine the result
        result = determine_winner(user_choice, computer_choice)
        
        # display choices and result
        print(f"You chose {user_choice}, and the computer chose {computer_choice}.")
        
        if result == "win":
            print("You win this round!")
            user_score += 1
        elif result == "lose":
            print("You lose this round!")
            computer_score += 1
        else:
            print("It's a tie!")
            ties += 1
        
        print()

# run the game
if __name__ == "__main__":
    play_game()