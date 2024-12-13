import random
import time

# Player class to handle stats and actions
class Player:
    def __init__(self, strength, health, defense):
        self.strength = strength
        self.health = health
        self.defense = defense
        self.inventory = []
        self.explored_rooms = set()
    
    def increase_stat(self, stat):
        if stat == "strength":
            self.strength += 1
        elif stat == "health":
            self.health += 10
        elif stat == "defense":
            self.defense += 1
    
    def take_damage(self, amount):
        self.health -= max(amount - self.defense, 0)
    
    def heal(self, amount):
        self.health += amount

    def pick_up_item(self, item):
        self.inventory.append(item)
    
    def use_item(self, item):
        if item == "key":
            print("You used the key.")
            self.inventory.remove(item)

# Combat function
def combat(player, enemy):
    while player.health > 0 and enemy['health'] > 0:
        action = input(f"Your health: {player.health}, Enemy health: {enemy['health']}\nChoose an action: 'attack' or 'defend': ").lower()
        if action == 'attack':
            damage = random.randint(1, player.strength)
            enemy['health'] -= damage
            print(f"You attacked the enemy for {damage} damage!")
        elif action == 'defend':
            player.defense += 2  # Temporary defense boost
            print(f"You defend and increase your defense!")
        
        # Enemy attacks back
        if enemy['health'] > 0:
            enemy_damage = random.randint(1, enemy['strength'])
            player.take_damage(enemy_damage)
            print(f"The enemy attacked you for {enemy_damage} damage!")
        
        if player.health <= 0:
            print("You died. Game over!")
            return False
    
    print("You defeated the enemy!")
    return True

# Room functions
def room_1(player):
    # Room where player fights small enemies
    print("You are in room 1. Enemies approach!")
    enemies = [{'health': 30, 'strength': 5} for _ in range(20)]
    
    for enemy in enemies:
        if not combat(player, enemy):
            return False  # If player dies during combat, return False
    
    print("All enemies defeated!")
    return True

def room_2(player):
    # Room where player collects elevator pieces
    print("You are in room 2. There are 6 doors.")
    pieces = 0
    while pieces < 6:
        door_choice = input("Choose a door to explore (1-6): ")
        door_choice = int(door_choice) - 1
        if door_choice not in player.explored_rooms:
            player.explored_rooms.add(door_choice)
            enemy = {'health': 50, 'strength': 7}
            if not combat(player, enemy):
                return False
            pieces += 1
            print(f"You've found a piece! Total pieces: {pieces}")
        else:
            print("You've already explored this door.")
    print("You collected all elevator pieces!")
    return True

def puzzle_room(player):
    # Room with two puzzles
    print("You're at the puzzle room. Choose a door to proceed:")
    puzzle_choice = input("Enter '1' for maze, '2' for riddle: ")
    
    if puzzle_choice == '1':
        print("Solve the maze puzzle!")
        time_limit = time.time() + 10 * 60  # 10-minute timer
        while time.time() < time_limit:
            maze_solution = input("Solve the maze: [type 'exit' to give up]: ")
            if maze_solution.lower() == "exit":
                print("You gave up. Game over!")
                return False
            if maze_solution.lower() == "correct":  # Placeholder for correct answer
                print("You solved the maze!")
                return True
        print("Time's up!")
        return False
    
    elif puzzle_choice == '2':
        print("Solve the riddle!")
        riddle_answer = input("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I? ")
        if riddle_answer.lower() == "echo":
            print("Correct! You solved the riddle.")
            return True
        else:
            print("Wrong answer. Game over!")
            return False
    return False

# Game loop and logic
def start_game():
    player = Player(strength=5, health=100, defense=2)
    print("You have 10 seconds to prepare for battle...")
    time.sleep(10)  # Simulate preparation time
    
    if not room_1(player):  # Combat in room 1
        return  # If player dies, game ends
    
    if not room_2(player):  # Collecting elevator pieces
        return  # If player dies, game ends
    
    if not puzzle_room(player):  # Puzzle room
        return  # If player fails puzzle, game ends
    
    print("Congratulations! You've escaped!")
    
# Start the game
start_game()
