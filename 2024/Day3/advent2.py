
# Import the regular expression module
import re

# Define a function to read a file and extract required strings
def read_file(filename):
    '''
    This function reads a file and extracts strings that start with 'do()' and end with 'don't()'.

    Args:
    filename (str): The name of the file to be read

    Returns:
    list: A list of strings that start with 'do()' and end with 'don't()'
    '''
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the file content and replace newline characters with empty string
        data = "do()" + file.read().replace('\n', '') + "don't()"
    # Use regular expression to find all strings that begin with 'do()' and end with 'dont()'
    strings = re.findall(r'do\(\)(.*?)don\'t\(\)', data)
    return strings

# Define a function to extract pairs of numbers from the strings
def extract_pairs(strings):
    '''
    This function extracts pairs of numbers from the strings that are enclosed in 'mul(number1,number2)' pattern.

    Args:
    strings (list): A list of strings from which pairs of numbers are to be extracted

    Returns:
    list: A list of tuples where each tuple contains a pair of numbers
    '''
    # Initialize an empty list to store pairs of numbers
    pairs = []
    # For each string
    for string in strings:
        # Use regular expression to find all pairs of numbers enclosed in 'mul(number1,number2)' pattern
        pair = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', string)
        # If pairs are found, append them to the list
        if pair:
            pairs.extend(pair)
    # Return the found pairs
    return pairs

# Main section of the code
if __name__ == "__main__":
    '''
    This is the main section of the code that calls the functions to read the file, extract strings,
    extract pairs of numbers from the strings, and calculate the sum of multiplication of each pair of numbers.
    '''
    # Read the file and get the strings
    strings = read_file('input.txt')
    # Extract the pairs of numbers from the strings
    pairs = extract_pairs(strings)
    # Calculate the sum of multiplication of each pair of numbers
    total = sum(int(pair[0]) * int(pair[1]) for pair in pairs)
    # Print the total sum
    print(f'The Total number is', {total})
