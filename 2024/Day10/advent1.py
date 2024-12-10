
import sys

# Function to parse the file and create a double entry map
def parse_file(filename):
    """
    This function reads a file and creates a double entry map with each character.
    It also identifies the maximum row and column indices.

    Args:
    filename (str): The name of the file to read

    Returns:
    map_dict (dict): A dictionary with keys as (column, row) and value as the character read
    max_row (int): The maximum row index
    max_col (int): The maximum column index
    """
    map_dict = {}
    max_col = 0
    max_row = 0
    with open(filename, 'r') as file:
        for y, line in enumerate(file):
            max_row = y
            for x, char in enumerate(line.strip()):
                max_col = max(max_col, x)
                if char.isdigit():
                    map_dict[(x, y)] = int(char)
                else:
                    map_dict[(x, y)] = 10 # for the examples where "." exists
    return map_dict, max_row, max_col

# Function to get nines from zero
def get_nines_from_zero(x, y, array, max_row, max_col):
    """
    This function calculates the sum of values in the array starting from zero.

    Args:
    x (int): The x-coordinate of the starting point
    y (int): The y-coordinate of the starting point
    array (dict): The array to search
    max_row (int): The maximum row index
    max_col (int): The maximum column index

    Returns:
    res (int): The sum of values in the array starting from zero
    """
    directions =[(0,1),(1,0),(0,-1),(-1,0)]

    alreadyFound = []
    res = 0

    parents = [(x, y)]
    while len(parents) > 0:
        x, y = parents.pop(0)
        for dx, dy in directions:
            posx = x + dx
            posy = y + dy
            if posx < 0 or posx > max_col or posy < 0 or posy > max_row:
                continue
            else:
                newpos = (posx, posy)
                if newpos in array:
                    if array[newpos] == 9 and array[(x, y)] == 8 and newpos not in alreadyFound:
                        alreadyFound.append(newpos)
                        res += 1
                    elif array[newpos] == array[(x, y)] + 1:
                        parents.append((posx, posy))

    return res

# Function to look for zero in the array
def look_for_zero(array):
    """
    This function searches for all instances of zero in the array.

    Args:
    array (dict): The array to search

    Returns:
    list_of_zero (list): A list of positions where zero is found
    """
    list_of_zero = []
    for pos, value in array.items():
        if value == 0:
            list_of_zero.append(pos)
    return list_of_zero

if __name__ == "__main__":
    # If a filename is provided as a command line argument, use it. Otherwise, use 'input.txt'.
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    array, max_row, max_col = parse_file(filename)

    list_of_zero = look_for_zero(array)

    res = 0
    for x,y in list_of_zero:
        res += get_nines_from_zero(x, y, array, max_row, max_col)

    print(f"Result: {res}")
