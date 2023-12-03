
# Importing required library
import re

# Defining a class DiceSet to hold the number of each color dice
class DiceSet:
    # Initializing the DiceSet with the number of each color dice
    def __init__(self, blue=0, red=0, green=0):
        self.blue = blue
        self.red = red
        self.green = green

# Defining a class Game to hold the sets of dice and compute the max number of each color
class Game:
    # Initializing the Game with the sets of dice and computing the max number of each color
    def __init__(self, *sets):
        self.sets = sets
        self.max_blue = max(set.blue for set in sets)
        self.max_red = max(set.red for set in sets)
        self.max_green = max(set.green for set in sets)

# Function to read the games from a file
def read_games(file_name):
    # List to hold the games
    games = []

    # Opening the file
    with open(file_name, 'r') as file:
        # Reading all lines
        lines = file.readlines()
        # Processing each line
        for line in lines:
            # List to hold the sets of a game
            sets = []
            # Splitting the line into sets
            split_line = re.split(":|;", line)
            raw_sets = split_line[1:]
            # Processing each set
            for raw_set in raw_sets:
                # Initializing the number of each color dice to 0
                blue = 0
                red = 0
                green = 0
                # Splitting the set into individual dice
                dices = raw_set.split(',')
                # Processing each dice
                for dice in dices:
                    # Extracting the number and color of the dice
                    match = re.search(r'([0-9]+) ([a-z]+)', dice.strip())
                    if match:
                        number = int(match.group(1))
                        color = match.group(2)
                        if color == 'blue':
                            blue += number
                        elif color == 'red':
                            red += number
                        elif color == 'green':
                            green += number
                # Adding the set to the list of sets
                sets.append(DiceSet(blue, red, green))
            # Adding the game to the list of games
            games.append(Game(*sets))
    # Returning the list of games
    return games

# Function to print the games
def print_games(games):
    # Processing each game
    for i, game in enumerate(games, start=1):
        # Printing the game number
        print(f"Game {i}:")
        # Processing each set in the game
        for j, set in enumerate(game.sets, start=1):
            # Printing the set number and the number of each color dice
            print(f" Set {j}: {set.blue} blue, {set.red} red, {set.green} green")

# Calling the read_games function to read the games from a file
games = read_games("input.txt")

# Calling the print_games function to print the games, for debug
print_games(games)

# Initializing a counter for the sum of indices
index_sum=0

# Processing each game
for i, game in enumerate(games, start=1):
    # Checking if the game satisfies the given conditions
    if game.max_blue <= 14 and game.max_red <= 12 and game.max_green <= 13:
        # Adding the index of the game to the counter
        index_sum += i

# Printing the sum of indices
print(f"The sum of indices for games with less than or equal to 14 blue dice, 12 red dice, and 13 green dice is: {index_sum}")
