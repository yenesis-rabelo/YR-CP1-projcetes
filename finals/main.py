#Yenesis Rabelo Final Project Assignment

import random
import time

# Player's stats
player = {
    "health": 100,
    "attack": 10,
    "pieces_collected": 0,
    "items": [],
    "magic_rock": True  # Indicates the player has found the magic rock
}

# Enemy Class
class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

# Initial enemies for combat
initial_enemies = [
    Enemy("Goblin", 30, 5),
    Enemy("Orc", 30, 5),
    Enemy("Wolf", 30, 5)
]

# Enemies for doors
door_enemies = [
    Enemy("Troll", 30, 6),
    Enemy("Minotaur", 35, 7),
    Enemy("Giant Spider", 40, 8),
    Enemy("Dark Knight", 45, 8),
    Enemy("Ogre", 50, 9),
    Enemy("Dragonette", 55, 10)
]

# Final boss
final_boss = Enemy("Shadow Dragon", 100, 12)

def main_game():
    while True:  # Loop for restarting the game after a defeat
        reset_player()  # Reset player stats for each new game
        if not prepare_for_battle():  # Prepare for the battle
            continue  # Restart if the preparation phase fails

        if not battle_enemies(initial_enemies, random.randint(2, 3)):  # Battle enemies
            print("You were defeated! The game will restart...")
            continue  # Restart the game after defeat

        print("You defeated all the enemies!")
        find_elevator_pieces()  # Attempt to find pieces for the elevator

        if player['pieces_collected'] < 6:
            print("You failed to collect all pieces. Game will restart...")
            continue  # Restart if did not collect pieces

        print("You've collected all elevator pieces!")
        go_to_second_floor()  # Go to the second floor

        if not puzzles():  # Attempt to solve puzzles
            continue  # Restart after choosing the wrong door

        # If player successfully solves the puzzles
        print("Congratulations! You've completed the game!")
        break  # Exit the game loop once done

def reset_player():
    player['health'] = 100
    player['pieces_collected'] = 0
    player['items'] = []  # Reset collected items
    player['magic_rock'] = True  # Player starts with the magic rock

def prepare_for_battle():
    print("You are in a battle preparation room. Prepare yourself!")
    print("You have 5 seconds to prepare...")
    time.sleep(5)  # 5 seconds delay
    print("During your preparation, you found a magic rock that will heal you by 3 health points every time you attack or defend.")
    return True  # Successfully prepared

def battle_enemies(enemy_list, num_enemies):
    for _ in range(num_enemies):  # Loop through each enemy
        enemy = random.choice(enemy_list)
        if not combat(enemy):  # If combat returns False, player is defeated
            return False  # Player is defeated
    return True  # Player defeated all enemies

def combat(enemy):
    print(f"A wild {enemy.name} appears with {enemy.health} health!")
    while enemy.health > 0 and player["health"] > 0:
        action = input("Choose your action (attack, defend): ").lower()

        if action == "attack":  # Attack action
            enemy.health -= player["attack"]
            print(f"You attacked {enemy.name} for {player['attack']} damage.")

            # Heal from magic rock
            player["health"] += 3
            if player["health"] > 100:  # Cap health at 100
                player["health"] = 100
            print(f"Your magic rock healed you! Your health is now {player['health']}.")

            if enemy.health <= 0:  # If the enemy is defeated
                print(f"You defeated {enemy.name}!")
                return True

            # Enemy attacks back
            player["health"] -= enemy.attack
            print(f"{enemy.name} attacks you for {enemy.attack} damage. Your health is now {player['health']}.")

            # Heal from magic rock after enemy attack
            player["health"] += 3
            if player["health"] > 100:  # Cap health at 100
                player["health"] = 100
            print(f"Your magic rock healed you! Your health is now {player['health']}.")

        elif action == "defend":  # Defend action
            print("You defended against the attack. No damage taken this turn.")

            # Heal from magic rock on defend
            player["health"] += 3
            if player["health"] > 100:  # Cap health at 100
                player["health"] = 100
            print(f"Your magic rock healed you! Your health is now {player['health']}.")

        else:
            print("Invalid action! Please choose again.")

    return False  # Player is defeated if health <= 0

def find_elevator_pieces():
    while player['pieces_collected'] < 6:  # Loop until all pieces are collected
        print("You find an elevator that is missing some pieces.")
        door_choice = input("Choose a door (1-6): ")

        if door_choice in ["1", "2", "3", "4", "5", "6"]:
            door_number = int(door_choice) - 1
            if door_number in player['items']:
                print("You've already been through this door!")  # Checking if door was already opened
                continue
            # Each door holds a tougher enemy
            enemy = door_enemies[min(door_number, len(door_enemies) - 1)]
            if combat(enemy):  # If the player wins the combat
                player['pieces_collected'] += 1  # Collect piece
                player['items'].append(door_number)  # Store opened door
                print(f"You collected a piece from door {door_choice}.")
            else:
                print("You were defeated! The game will restart...")
                return  # Exit if defeated
        else:
            print("Invalid door choice. Please choose again.")

def go_to_second_floor():
    print("You insert the pieces into the elevator and ascend to the second floor...")
    time.sleep(2)  # Pause for effect

def puzzles():
    print("You have ascended to the second floor. There are two doors.")
    print("Only Door 2 leads to the correct puzzle. Door 1 leads to an instant defeat.")

    while True:
        door_choice = input("Choose a door to face the puzzle (1 or 2): ")

        if door_choice == "1":  # Door 1 leads to death
            print("You chose Door 1. You are defeated! The game will restart...")
            return False  # Restart if Door 1 is chosen
        elif door_choice == "2":  # Door 2 leads to riddle puzzle
            if not riddle_puzzle():
                print("You chose the wrong door! You will restart the game.")
                return False  # Restart if riddle is not solved
            return True  # Successfully solved
        else:
            print("Invalid door choice. Choose again.")

# Simulate a riddle puzzle
def riddle_puzzle():
    riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?"
    answer = "ECHO"  # Answer in capital letters
    print(riddle)

    user_answer = input("Your answer (type 'ECHO' in capitals to summon the boss): ").strip()
    
    if user_answer == answer:  # Correct answer but does not summon the boss
        print("Correct! The riddle is solved.")
        return True
    elif user_answer == "ECHO":  # Player summons the final boss
        print("The Final Boss appears!")
        if combat(final_boss):  # Engage in combat with the final boss
            print("You defeated the Shadow Dragon!")
            return True  # Boss defeated
        else:
            print("You were defeated by the Shadow Dragon! The game will restart...")
            return False  # Return false if the player is defeated
    else:
        print("Incorrect answer. You chose the wrong door...")
        return False  # Return false on incorrect answer

# Start the Game
if __name__ == "__main__":
    main_game()
    print("Thank you for playing!")
