import random

# Constants
GRID_SIZE = 10
SHIP_SIZES = [3, 2]  # Small ship sizes for demo (can add more)

# Initialize empty grid
def create_grid():
    return [['~' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Convert input like 'B4' to (row, col)
def parse_input(coord):
    row = ord(coord[0].upper()) - ord('A')
    col = int(coord[1:]) - 1
    return row, col

# Print grid for player
def print_grid(grid, hide_ships=False):
    print("  " + " ".join([str(i+1).rjust(2) for i in range(GRID_SIZE)]))
    for i, row in enumerate(grid):
        row_label = chr(ord('A') + i)
        display = []
        for cell in row:
            if hide_ships and cell == 'S':
                display.append('~')
            else:
                display.append(cell)
        print(f"{row_label} " + " ".join(display))

# Place ship randomly for AI
def place_ship_randomly(grid, size):
    while True:
        vertical = random.choice([True, False])
        if vertical:
            row = random.randint(0, GRID_SIZE - size)
            col = random.randint(0, GRID_SIZE - 1)
            if all(grid[row + i][col] == '~' for i in range(size)):
                for i in range(size):
                    grid[row + i][col] = 'S'
                break
        else:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - size)
            if all(grid[row][col + i] == '~' for i in range(size)):
                for i in range(size):
                    grid[row][col + i] = 'S'
                break

# Check if all ships are sunk
def all_ships_sunk(grid):
    for row in grid:
        if 'S' in row:
            return False
    return True

# AI targeting strategy
class AI:
    def __init__(self):
        self.hits = []
        self.possible_targets = []

    def choose_target(self, player_grid):
        if self.possible_targets:
            return self.possible_targets.pop()
        while True:
            row = random.randint(0, GRID_SIZE - 1)
            col = random.randint(0, GRID_SIZE - 1)
            if player_grid[row][col] in ('~', 'S'):
                return row, col

    def update_strategy(self, row, col, result):
        if result == "Hit":
            self.hits.append((row, col))
            for dr, dc in [(-1,0), (1,0), (0,-1), (0,1)]:
                r, c = row + dr, col + dc
                if 0 <= r < GRID_SIZE and 0 <= c < GRID_SIZE:
                    self.possible_targets.append((r, c))

# Main game loop
print("Welcome to Battleship!")
player_grid = create_grid()
ai_grid = create_grid()

# AI ship placement
for size in SHIP_SIZES:
    place_ship_randomly(ai_grid, size)

ai = AI()

while True:
    print("\nYour Board:")
    print_grid(player_grid)

    # Player turn
    while True:
        try:
            move = input("Enter your attack (e.g., A5): ")
            row, col = parse_input(move)
            if ai_grid[row][col] in ('X', 'O'):
                print("Already targeted. Try again.")
            else:
                break
        except:
            print("Invalid input. Try again.")

    if ai_grid[row][col] == 'S':
        ai_grid[row][col] = 'X'
        print(f"Player attacks: {move.upper()} → Hit!")
    else:
        ai_grid[row][col] = 'O'
        print(f"Player attacks: {move.upper()} → Miss")

    if all_ships_sunk(ai_grid):
        print("Congratulations! You sank all AI ships. You win!")
        break

    # AI turn
    row, col = ai.choose_target(player_grid)
    if player_grid[row][col] == 'S':
        player_grid[row][col] = 'X'
        print(f"AI attacks: {chr(ord('A')+row)}{col+1} → Hit!")
        ai.update_strategy(row, col, "Hit")
    elif player_grid[row][col] == '~':
        player_grid[row][col] = 'O'
        print(f"AI attacks: {chr(ord('A')+row)}{col+1} → Miss")

    if all_ships_sunk(player_grid):
        print("AI has sunk all your ships. You lose!")
        break

