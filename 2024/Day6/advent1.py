
import sys

# This function reads the file and appends each character to the letters list
def read_file(filename):
    """
    Reads a file and creates a list of Case objects representing each character in the file.

    Args:
    filename (str): The name of the file to read.

    Returns:
    list: A list of Case objects.
    """
    cases = []
    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                cases.append(Case(char, col, row))
    return cases

# This class represents a Letter with its value and position
class Case:
    """
    Represents a case with a value and a position.

    Attributes:
    _value (str): The value of the case.
    _col (int): The column of the case.
    _row (int): The row of the case.
    _isEmpty (bool): Whether the case is empty.
    _hasBeenVisited (bool): Whether the case has been visited.
    _isWall (bool): Whether the case is a wall.
    """
    def __init__(self, value, col, row):
        self._value = value
        self._col = col
        self._row = row
        self._isEmpty = self._value in ["."]
        self._hasBeenVisited = self._value in ["^"]
        self._isWall = self._value in ["#"]

    @property
    def value(self):
        """Gets the value of the case."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Sets the value of the case."""
        self._value = new_value
        self._isEmpty = self._value in ["."]
        self._isWall = self._value in ["#"]
        if self._hasBeenVisited == False:
            self._hasBeenVisited = self._value in ["^"]

    @property
    def col(self):
        """Gets the column of the case."""
        return self._col

    @col.setter
    def col(self, new_col):
        """Sets the column of the case."""
        self._col = new_col

    @property
    def row(self):
        """Gets the row of the case."""
        return self._row

    @row.setter
    def row(self, new_row):
        """Sets the row of the case."""
        self._row = new_row

    @property
    def isEmpty(self):
        """Gets whether the case is empty."""
        return self._isEmpty

    @isEmpty.setter
    def isEmpty(self, new_isEmpty):
        """Sets whether the case is empty."""
        self._isEmpty = new_isEmpty

    @property
    def hasBeenVisited(self):
        """Gets whether the case has been visited."""
        return self._hasBeenVisited

    @hasBeenVisited.setter
    def hasBeenVisited(self, new_hasBeenVisited):
        """Sets whether the case has been visited."""
        self._hasBeenVisited = new_hasBeenVisited

    @property
    def isWall(self):
        """Gets whether the case is a wall."""
        return self._isWall

    @isWall.setter
    def isWall(self, new_isWall):
        """Sets whether the case is a wall."""
        self._isWall = new_isWall

# This function looks for the guard in the cases list
def look_for_guard(cases):
    """
    Finds the guard in the list of cases.

    Args:
    cases (list): The list of cases to search.

    Returns:
    Case: The guard case, or None if no guard is found.
    """
    for case in cases:
        if case.value == "^":
            return case
    return None

def go(case, cases, direction):
    """
    Moves in the specified direction from the current case, or stays put if the next case is a wall.

    Args:
    case (Case): The current case.
    cases (list): The list of all cases.
    direction (str): The direction to move in ('U', 'D', 'L', or 'R').

    Returns:
    Case: The case after moving, or the current case if the next case is a wall.
    """
    if direction == 'U':
        next_case = [c for c in cases if c.row == case.row-1 and c.col == case.col]
    elif direction == 'D':
        next_case = [c for c in cases if c.row == case.row+1 and c.col == case.col]
    elif direction == 'L':
        next_case = [c for c in cases if c.row == case.row and c.col == case.col-1]
    elif direction == 'R':
        next_case = [c for c in cases if c.row == case.row and c.col == case.col+1]

    if next_case:
        if next_case[0].isWall:
            return case
        else:
            next_case[0].hasBeenVisited = True
            return go(next_case[0], cases, direction)
    else:
        return case

def count_visited_cases(cases):
    """
    Counts the number of visited cases in the list of cases.

    Args:
    cases (list): The list of cases.

    Returns:
    int: The number of visited cases.
    """
    return sum(case.hasBeenVisited for case in cases)

# Execution starts here
if __name__ == "__main__":
    """
    Main execution of the program. Reads the file, finds the guard, and moves in all directions until hitting a wall.
    Prints the number of visited cases.
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input_basic.txt'
    cases = read_file(filename)

    guard = look_for_guard(cases)

    direction ="U"

    max_col = max(case.col for case in cases)
    max_row = max(case.row for case in cases)
    directions = ["U", "R", "D", "L"]
    direction_index = 0

    while ((guard.col != 0) and (guard.col != max_col) and (guard.row != 0) and (guard.row != max_row)):
        guard = go(guard, cases, directions[direction_index])
        direction_index = (direction_index + 1) % len(directions) # This will cycle through the directions

    visited=count_visited_cases(cases)

    print(f"Found {visited} visited Case.")
