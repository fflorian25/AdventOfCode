
import sys
import math

class Case:
    """
    Represents a case with a value and a position.

    Attributes:
    _value (str): The value of the case.
    _col (int): The column of the case.
    _row (int): The row of the case.
    _isWall (bool): True if the case is a wall ('#'), False otherwise.
    _isBox (bool): True if the case is a box ('O'), False otherwise.
    """

    def __init__(self, value: str, col: int, row: int):
        """
        Initializes a Case object.

        Args:
        value (str): The value of the case.
        col (int): The column of the case.
        row (int): The row of the case.
        """
        self._value = value
        self._col = col
        self._row = row
        self._isWall = self._value == "#"
        self._isBox = self._value == "O"

    def fill_box(self):
        self._value = value = "O"
        self._isBox = True

    def empty_box(self):
        self._value = value = "."
        self._isBox = False

    def get_value(self) -> str:
        """Returns the value of the case."""
        return self._value

    def get_position(self) -> tuple[int, int]:
        """Returns the position of the case as (col, row)."""
        return self._col, self._row

    def get_col(self) -> int:
        """Returns the column of the case."""
        return self._col

    def get_row(self) -> int:
        """Returns the row of the case."""
        return self._row

    def __repr__(self) -> str:
        """Returns a string representation of the Case."""
        return (f"Case(value={self._value}, col={self._col}, row={self._row}, "
                f"isWall={self._isWall}, isBox={self._isBox})")

def read_file(file_path: str):
    """
    Reads the file and processes its contents to create a map of Case objects, a start point, and a path list.

    Args:
    file_path (str): The path to the input file.

    Returns:
    tuple[dict[tuple[int, int], Case], tuple[int, int], list[tuple[int, int]]]:
        - A dictionary representing the map with keys as (x, y) coordinates and values as Case objects.
        - A tuple representing the start point as (x, y).
        - A list of tuples representing the path with directions as (dx, dy).
    """
    map_cases = {}  # Dictionary to store the map as {(x, y): Case}
    path = []       # List to store the path directions
    start_point = None  # Start point coordinates

    with open(file_path, 'r') as file:
        lines = file.readlines()

    # Process the map section to create Case objects
    path_start_index = 0  # Default value in case no empty line is found
    for y, line in enumerate(lines):
        line = line.strip()
        if not line:  # Stop processing map when encountering an empty line
            path_start_index = y + 1  # Start reading the path from the next line
            break

        for x, char in enumerate(line):
            map_cases[(x, y)] = Case(value=char, col=x, row=y)
            if char == "@":
                start_point = (x, y)

    # Ensure start_point was found
    if start_point is None:
        raise ValueError("No start point '@' found in the map.")

    # Process the path directions
    direction_map = {
        '<': (-1, 0),
        '>': (1, 0),
        '^': (0, -1),
        'v': (0, 1)
    }

    for path_line in lines[path_start_index:]:
        path_line = path_line.strip()
        for char in path_line:
            if char in direction_map:
                path.append(direction_map[char])

    return map_cases, start_point, path

def pretty_print(cases):
    """
    Prints the map in a formatted way based on the given cases.

    Args:
    cases (dict[tuple[int, int], Case]): The map of cases with coordinates as keys.
    """
    if not isinstance(cases, dict):
        raise TypeError("cases must be a dictionary with (col, row) tuples as keys.")

    if not cases:
        return

    # Determine the bounds of the map dynamically
    max_row = max(pos[1] for pos in cases)
    max_col = max(pos[0] for pos in cases)

    for row in range(max_row + 1):
        for col in range(max_col + 1):
            case = cases.get((col, row))  # Access the case directly using (col, row) as key
            if case:
                if case.get_value() != ".":
                    print(case.get_value(), end='')
                elif getattr(case, 'is_antinode', lambda: False)():  # Check if is_antinode exists and call it
                    print("#", end='')
                else:
                    print(".", end='')
            else:
                print(" ", end='')
        print()

def do_move(robot, direction, cases):
    """
    Moves the robot in the specified direction if possible.

    Args:
    robot (tuple[int, int]): The current position of the robot as (x, y).
    direction (tuple[int, int]): The direction to move as (dx, dy).
    cases (dict[tuple[int, int], Case]): The map of cases with coordinates as keys.

    Returns:
    tuple[int, int]: The new position of the robot after the move.
    """
    new_case = (robot[0] + direction[0], robot[1] + direction[1])

    # Look for the first case that is not a box in the alignment
    end_case = new_case
    while cases[end_case]._isBox:
        end_case = (end_case[0] + direction[0], end_case[1] + direction[1])

    # Check if the end case is a wall
    if cases[end_case]._isWall:
        return robot

    else:  # The end case is empty; move the box
        cases[end_case].fill_box()
        cases[new_case].empty_box()
        cases[new_case]._value = "@"
        cases[robot]._value = "."
        return new_case



# Execution starts here
if __name__ == "__main__":
    """
    Prints the number of antinide cases.
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    cases, robot, paths = read_file(filename)
    #pretty_print(cases)

    for direction in paths:
        #print(direction)

        robot = do_move(robot, direction, cases)     


    pretty_print(cases)
    res = 0
    for case in cases.values():
        if case._isBox:
            xy = case.get_position()
            #print(case)
            res += xy[0] + 100*xy[1]
    print(f"Found Res :{res}.")
