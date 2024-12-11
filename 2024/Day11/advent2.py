import sys

# This function parses a given file and creates a list of integers.
# It reads the file line by line and converts each line into an integer.
# The integers are then added to a list which is returned at the end.
def parse_file(filename):
    """
    This function reads a file and creates a list of integers.

    Args:
    filename (str): The name of the file to read

    Returns:
    list: A list of all integers in the file

    Raises:
    ValueError: If the file contains non-integer values.
    """
    try:
        with open(filename) as f:
            stones = [int(stone) for stone in f.read().split()]
        return stones
    except ValueError:
        raise ValueError("File contains non-integer values.")
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {filename} was not found.")

already = {}

# This function performs the "blink" operation on a given number.
# The blink operation is defined as follows:
# - If the number is 0, it is replaced with the result of blinking 1.
# - If the number has an even number of digits, it is split into two parts,
#   and the blink operation is applied recursively to both parts.
# - If neither of the above conditions are met, the number is replaced with
#   its value multiplied by 2024, and the blink operation is applied recursively.
def do_blink(num, prof):
    """
    Function to perform "blink" operation on a number recursively.

    Args:
    num (int): The number to perform the operation on.
    prof (int): The remaining recursion depth.

    Returns:
    int: Result of the blink operation.
    """
    if (num, prof) in already:
        return already[(num, prof)]

    if prof == 0:
        res = 1
    elif num == 0:
        res = do_blink(1, prof - 1)
    elif len(str(num)) % 2 == 0:
        mid = len(str(num)) // 2
        left_part = int(str(num)[:mid])
        right_part = int(str(num)[mid:])
        res = do_blink(left_part, prof - 1) + do_blink(right_part, prof - 1)
    else:
        res = do_blink(num * 2024, prof - 1)

    already[(num, prof)] = res
    return res

# This is the main function that is executed when the script is run.
if __name__ == "__main__":
    """
    Main function to execute the script.
    Reads numbers from the input file, applies the blink operation, and prints the result.
    """
    try:
        filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
        stones = parse_file(filename)

        blinks = 75
        res = 0

        for stone in stones:
            res += do_blink(stone, blinks)

        print(f"Result: {res}")
    except Exception as e:
        print(f"Error: {e}")
