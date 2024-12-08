
import sys
import math

class Case:
    """
    Represents a case with a value and a position.

    Attributes:
    _value (str): The value of the case.
    _col (int): The column of the case.
    _row (int): The row of the case.
    _isAntiNode (bool): Whether the case has been visited.
    _isAntinodeOf (list): List of antennas that it is an antinode of.
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
        self._isAntiNode = False
        self._isAntinodeOf = []

    def add_antinode_of(self, antenna):
        """
        Adds an antenna that this case is an antinode of.

        Args:
        antenna: The antenna to add.
        """
        self._isAntiNode = True
        self._isAntinodeOf.append(antenna)

    def get_value(self):
        """Returns the value of the case as ."""
        return self._value

    def get_position(self):
        """Returns the position of the case as (col, row)."""
        return self._col, self._row
    
    def get_col(self):
        """Returns the column of the case."""
        return self._col

    def get_row(self):
        """Returns the row of the case."""
        return self._row

    def is_antinode(self):
        """Returns the antinode of the case as ."""
        return self._isAntiNode
    
    def __repr__(self):
        """Returns a string representation of the Case."""
        return (f"Case(value={self._value}, col={self._col}, row={self._row}, "
                f"isAntiNode={self._isAntiNode}, isAntinodeOf={self._isAntinodeOf})")


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

def pretty_print(cases, max_row, max_col):
    for row in range(max_row+1):
        for col in range(max_col+1):
            case = [c for c in cases if c.get_row() == row and c.get_col() == col]
            if case:
                if case[0].get_value() != ".":
                    print(case[0].get_value(), end='')
                elif case[0].is_antinode():
                    print("#", end='')
                else:
                    print(".", end='')
            else:
                print(" ", end='')
        print()

def group_cases_by_value(cases):
    """
    Groups a list of Case objects into a dictionary based on their value.

    Args:
    cases (list of Case): The list of Case objects.

    Returns:
    dict: A dictionary where keys are case values, and values are lists of Case objects.
    """
    case_dict = {}
    for case in cases:
        value = case._value
        if value == ".":
            continue
        elif value not in case_dict:
            case_dict[value] = []
        case_dict[value].append(case)
    return case_dict

def computeDistance(antenna1, antenna2):
    """
    Computes the difference in column and row positions between two antennas.

    Args:
    antenna1: The first antenna object with get_col() and get_row() methods.
    antenna2: The second antenna object with get_col() and get_row() methods.

    Returns:
    tuple: A tuple containing:
        - The difference in column positions (col_diff)
        - The difference in row positions (row_diff)
    """
    # Calculate the difference in column positions between antenna2 and antenna1
    col_diff = antenna2.get_col() - antenna1.get_col()
    
    # Calculate the difference in row positions between antenna2 and antenna1
    row_diff = antenna2.get_row() - antenna1.get_row()
    
    # Return the differences as a tuple
    return (col_diff, row_diff)

def lookForValueSymmetry(antenna, x, y, max_x, max_y):
    """
    Finds all positions that are multiples of the given x and y offsets,
    starting from the antenna's position, and until reaching max_x or max_y.

    Args:
    antenna (Case): The reference antenna object.
    x (int): The horizontal offset (column difference).
    y (int): The vertical offset (row difference).
    max_x (int): The maximum column value.
    max_y (int): The maximum row value.

    Returns:
    list of tuples: A list of positions (col, row) that are multiples of x and y.
    """
    # Get the position of the reference antenna
    col, row = antenna.get_col(), antenna.get_row()

    positions = []  # Initialize an empty list to store valid positions

    # Iterate for multiples of x and y at the same time
    # We will use a step to add multiples of x to col and multiples of y to row
    i = 1
    while True:
        new_col = col + (x * i)
        new_row = row + (y * i)
        
        # Check if the new position is within the bounds
        if new_col < max_x + 1 and new_row < max_y +1 and new_col>-1 and new_row > -1:
            positions.append((new_col, new_row))
        else:
            break  # Exit the loop if the position goes beyond the bounds
        
        i += 1  # Move to the next multiple of x and y simultaneously
    
    return positions

def reduce(x,y):  
    gcd = math.gcd(x, y)  
    return(x/gcd, y/gcd)

def lookForPos(cases, col, row):
    """
    Looks for a Case object at a specific position (col, row) in the list of cases.

    Args:
    cases (list of Case): The list of Case objects.
    col (int): The column index to search for.
    row (int): The row index to search for.

    Returns:
    Case: The Case object at the specified position, or None if not found.
    """
    # Iterate over the list of cases to find the case at the given position
    for case in cases:
        if case.get_col() == col and case.get_row() == row:
            return case  # Return the found case
    
    # If no case is found, return None (or you could raise an error here if needed)
    return None


def count_antinode(cases):
    """
    Counts the number of cases where isAntiNode is True.

    Args:
    cases (list of Case): The list of Case objects.

    Returns:
    int: The number of cases where isAntiNode is True.
    """
    return sum(case.is_antinode() for case in cases)


# Execution starts here
if __name__ == "__main__":
    """
    Prints the number of antinide cases.
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    cases = read_file(filename)

    max_col = max(case.get_col() for case in cases)
    max_row = max(case.get_row() for case in cases)
    #pretty_print(cases, max_row, max_col)

    antennas_dict = group_cases_by_value(cases)
    #print(antennas_dict)

    for val, antennas in antennas_dict.items():  # Iterate over the dictionary's key-value pairs
        antinodePosCol = []  # Initialize an empty list to store antinode positions
        for antenna in antennas:  # Loop through each antenna in the list
            for other_antenna in antennas:  # Compare with every other antenna in the list
                if antenna != other_antenna:  # Avoid computing distance with itself
                    (x, y) = computeDistance(antenna, other_antenna)  # Compute distance between antennas
                    (newX, newY) = reduce(x,y)
                    antinodeLists = lookForValueSymmetry(antenna, newX, newY, max_col, max_row)# Check for symmetry or perform a related operation
                    for elem in antinodeLists:
                        antinodePosCol.append(elem)  
        #print(val)
        #print(antinodePosCol)
        for antinode in antinodePosCol :
            if antinode[0] <= max_col and antinode[0] > -1 and antinode[1] <= max_row and antinode[1] > -1:
                anti = lookForPos(cases, antinode[0], antinode[1]).add_antinode_of(val)


    pretty_print(cases, max_row, max_col)


    nbAntiNode = count_antinode(cases)

    print(f"Found {nbAntiNode} nbAntiNode.")
