import random

# Function to handle combat with enemies
def combat(enemy):
    combat_options = ["Attack", "Defend", "Use Item"]
    print(f"A wild {enemy} appears!")
    while True:
        print("Choose an action: ")
        for i, option in enumerate(combat_options):
            print(f"{i + 1}. {option}")
        try:
            choice = int(input("Enter your choice (1-3): ")) - 1
            if choice == 0:  # Attack
                print(f"You attack the {enemy}!")
                print(f"You defeated the {enemy}!")
                return True  
            elif choice == 1:  # Defend
                print(f"You defend against the {enemy}!")
                print(f"You successfully defended the {enemy}'s attack!")
                continue  # Let the player defend again
            elif choice == 2:  # Use Item
                print("You use a health potion!")
                print("You restored some health!")
                continue
            else:
                print("Invalid option. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3.")

# Function to explore doors and collect puzzle pieces
def explore_doors():
    doors = ["Room 1", "Room 2", "Room 3", "Room 4", "Room 5", "Room 6"]
    puzzle_pieces = []
    for door in doors:
        print(f"Opening {door}...")
        enemy = f"Enemy in {door}"
        combat(enemy)  # 
        puzzle_pieces.append(f"Piece from {door}")
        print(f"You collected a puzzle piece from {door}!")
        if len(puzzle_pieces) == 6:  # Collecting all pieces
            print("You collected all the puzzle pieces!")
            break  # Exit after collecting all pieces
    return puzzle_pieces

# Function for the puzzles on the second floor
def solve_puzzles():
    print("You're on the second floor! Choose a puzzle to solve:")
    puzzles = ["Maze", "Riddle"]
    while True:
        choice = input(f"Pick a puzzle: {puzzles[0]} or {puzzles[1]}: ").lower()
        if choice == "maze":
            print("You are navigating through the maze!")
            print("You solved the maze and collected the key!")
            return True
        elif choice == "riddle":
            print("You are solving the riddle!")
            print("You solved the riddle and collected the key!")
            return True
        else:
            print("Invalid choice. Please choose again.")

# Main function to run the game
def game():
    print("Welcome to the adventure game!")
    
    # Combat section (2 enemies)
    for i in range(1, 3):
        print(f"\nBattle {i}:")
        combat(f"Enemy {i}")  
        print(f"Enemy {i} defeated!")
    
    # After defeating the 2 enemies, explore doors
    print("\nYou defeated all enemies! Now, explore the doors.")
    puzzle_pieces = explore_doors()
    
    # If all puzzle pieces are collected, solve puzzles on the second floor
    if len(puzzle_pieces) == 6:
        print("\nYou collected all the puzzle pieces! The elevator is now open.")
        if solve_puzzles():
            print("You escaped successfully!")
        else:
            print("Game over. Try again!")

# Start the game
game()
