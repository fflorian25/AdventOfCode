
import sys

# Class to represent a letter in the grid
class Letter:
    def __init__(self, value, col, row):
        self._value = value
        self._col = col
        self._row = row
        self._isXmas = self._value in ["X", "M", "A", "S"]

    # Getter for value
    @property
    def value(self):
        return self._value

    # Setter for value
    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._isXmas = self._value in ["X", "M", "A", "S"]

    # Getter for col
    @property
    def col(self):
        return self._col

    # Setter for col
    @col.setter
    def col(self, new_col):
        self._col = new_col

    # Getter for row
    @property
    def row(self):
        return self._row

    # Setter for row
    @row.setter
    def row(self, new_row):
        self._row = new_row

    # Getter for isXmas
    @property
    def isXmas(self):
        return self._isXmas


# Function to read the file and create a list of Letter objects
def read_file(filename):
    letters = []
    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                letters.append(Letter(char, col, row))
    return letters

# Function to search for adjacent letters in the specified direction
def search_adjacent(letter, letters, direction):
    adjacent_letters = []
    dx, dy = 0, 0
    if direction == "N":
        dx, dy = 0, 1
    elif direction == "S":
        dx, dy = 0, -1
    elif direction == "E":
        dx, dy = 1, 0
    elif direction == "W":
        dx, dy = -1, 0
    elif direction == "NE":
        dx, dy = 1, 1
    elif direction == "NW":
        dx, dy = -1, 1
    elif direction == "SE":
        dx, dy = 1, -1
    elif direction == "SW":
        dx, dy = -1, -1

    for l in letters:
        if l.row == letter.row + dy and l.col == letter.col + dx:
            adjacent_letters.append(l)
    return adjacent_letters

# Function to search for 'XMAS' chain in all directions
def search_xmas_chain(letter, letters):
    total=0
    adjacent_xmas =[]
    for direction in ["NE", "SW", "NW", "SE"]:
        adjacent = search_adjacent(letter, letters, direction)
        if adjacent:
            adjacent_xmas.append(adjacent[0].value)
    if len(adjacent_xmas) !=4 :
        return 0
    # Checking diagonals for 'M' and 'S'
    if (adjacent_xmas[0] == "M" and adjacent_xmas[1] == "S") or (adjacent_xmas[0] == "S" and adjacent_xmas[1] == "M"):
        if (adjacent_xmas[2] == "M" and adjacent_xmas[3] == "S") or (adjacent_xmas[2] == "S" and adjacent_xmas[3] == "M"):
            return 1
    return 0

if __name__ == "__main__":
    # Read the file and get the strings
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    letters = read_file(filename)
    # Use the search_adjacent function
    xmas_count = 0
    for letter in letters:
        if letter.value == "A":
            xmas_count += search_xmas_chain(letter, letters)
    print(f"Found {xmas_count} complete 'XMAS' sequences.")
