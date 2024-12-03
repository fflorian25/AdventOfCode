
# Import the regular expression module
import re

# Define a function to read a file and extract pairs of numbers
def read_file(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read the file content and replace newline characters with empty string
        data = file.read().replace('\n', '')
    # Use regular expression to find all pairs of numbers enclosed in 'mul(number1,number2)' pattern
    pairs = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', data)
    # Return the found pairs
    return pairs

# Main section of the code
if __name__ == "__main__":
    # Read the file and get the pairs of numbers
    pairs = read_file('input.txt')
    # Calculate the sum of multiplication of each pair of numbers
    total = sum(int(pair[0]) * int(pair[1]) for pair in pairs)
    # Print the total sum
    print(f'The Total number is', {total})
