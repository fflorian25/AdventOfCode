
import sys

# This function parses a given file and creates a list of integers.
# It reads the file line by line and converts each line into an integer.
# The integers are then added to a list which is returned at the end.
def parse_file(filename):
    """
    This function reads a file and creates a list each int.
    It also identifies the maximum row and column indices.

    Args:
    filename (str): The name of the file to read

    Returns:
    stones (list) : list of all numbers
    """
    with open(filename) as f:
        stones = [int(stone) for stone in f.read().split()]
    return stones

# This function performs the "blink" operation on a given list of integers.
# The blink operation is defined as follows:
# - If the integer is 0, it is replaced with 1.
# - If the integer has an even number of digits, it is split into two integers,
#   each containing half of the digits of the original integer.
# - If neither of the above conditions are met, the integer is replaced with
#   its value multiplied by 2024.
# The function returns the modified list.
def do_blink(array):
    """
    Function to perform "blink" operation on the array

    Args:
    array (list): list of numbers

    Returns:
    array (list) : modified list after performing "blink" operation
    """
    i = 0
    while i < len(array):
        if array[i] == 0:
            array[i] = 1
            i += 1
        elif len(str(array[i])) % 2 == 0:
            mid = len(str(array[i])) // 2
            array[i:i+1] = [int(str(array[i])[:mid]), int(str(array[i])[mid:])]
            i += 2
        else:
            array[i] = array[i] * 2024
            i += 1
    return array


# This is the main function that is executed when the script is run.
# It first checks if a filename is provided as a command line argument.
# If not, it defaults to 'input.txt'.
# It then calls the parse_file function to read the file and create a list of integers.
# The blink operation is then performed on the list 75 times.
# The length of the final list is printed as the result.
if __name__ == "__main__":
    """
    Main function to execute the script
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    stones = parse_file(filename)

    blinks=25
    for i in range(0,blinks):
        print(f"Progress: {i/blinks*100:.2f}%")
        stones = do_blink(stones)

    res = len(stones)
    print(f"Result: {res}")
