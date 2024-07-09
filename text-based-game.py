class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.inventory = []

    def move(self, direction):
        print(f"{self.name} moves {direction}")

    def pick_up_item(self, item):
        print(f"{self.name} picks up {item}")

    def use_item(self, item):
        print(f"{self.name} uses {item}")

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, player):
        print(f"{self.name} attacks {player.name} for {self.damage} damage")
        player.health -= self.damage
        if player.health <= 0:
            print(f"{player.name} has been defeated!")

class Item:
    def __init__(self, name):
        self.name = name

# Game initialization
def initialize_game():
    # Create player
    player_name = input("Enter your name: ")
    player = Player(player_name)
    
    # Initialize game world, enemies, items, etc.
    print("\n=== Welcome to the Adventure Game ===\n")
    print(f"{player.name}, you find yourself in a mysterious land.")
    print("Your objective is to survive and explore!\n")

    # Start game loop
    game_loop(player)

# Game loop
def game_loop(player):
    while player.health > 0:
        print("\n----------------------------------")
        print(f"Current Health: {player.health}\n")

        action = input("What would you like to do? (move, pick up, quit): ").lower().strip()

        if action == "quit":
            break
        elif action == "move":
            direction = input("Which direction would you like to move? (north, south, east, west): ").lower().strip()
            player.move(direction)
        elif action == "pick up":
            item = input("What item would you like to pick up? ").strip()
            player.pick_up_item(item)
        else:
            print("Invalid action. Try again.")

        # Simulate enemy encounter
        enemy = Enemy("Goblin", 20, 5)
        enemy.attack(player)

    print("\n----------------------------------")
    print("Game Over!")
    print(f"{player.name}, thanks for playing!")

# Start the game
if __name__ == "__main__":
    initialize_game()
