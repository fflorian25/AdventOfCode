
import sys

# This function reads the file and appends each character to the letters list
def read_file(filename):
    letters = []
    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                letters.append(Letter(char, col, row))
    return letters

# This function searches for adjacent letters based on the given direction
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

# This function searches for the next XMAS letter in the adjacent letters
def search_adjacent_xmas(letter, letters, direction):
    next_xmas = letter.next_xmas_letter()
    if next_xmas:
        adjacent_letters = search_adjacent(letter, letters, direction)
        return [l for l in adjacent_letters if l.value == next_xmas]
    return []

# This function searches for the complete XMAS chain in the given direction
def search_xmas_chain(letter, letters, direction, count=0):
    total=0
    if letter.value == "S" and count == 3:
        return 1
    else:
        adjacent_xmas = search_adjacent_xmas(letter, letters, direction)
        for l in adjacent_xmas:
            total += search_xmas_chain(l, letters, direction, count + 1)
        return total

# This class represents a Letter with its value and position
class Letter:
    def __init__(self, value, col, row):
        self._value = value
        self._col = col
        self._row = row
        self._isXmas = self._value in ["X", "M", "A", "S"]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._isXmas = self._value in ["X", "M", "A", "S"]

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, new_col):
        self._col = new_col

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, new_row):
        self._row = new_row

    @property
    def isXmas(self):
        return self._isXmas

    # This function returns the next letter in the XMAS chain
    def next_xmas_letter(self):
        xmas_order = ["X", "M", "A", "S"]
        if self._value in xmas_order:
            current_index = xmas_order.index(self._value)
            if current_index < len(xmas_order) - 1:
                return xmas_order[current_index + 1]
        return None

# Execution starts here
if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    letters = read_file(filename)
    xmas_count = 0
    for letter in letters:
        if letter.value == "X":
            for direction in ["N", "S", "E", "W", "NE", "NW", "SE", "SW"]:
                xmas_count += search_xmas_chain(letter, letters, direction)
    print(f"Found {xmas_count} complete 'XMAS' sequences.")
