
import re

class Number:
    def __init__(self, line_number, begin_index, end_index, num_str):
        self.line_number = line_number
        self.begin_index = begin_index
        self.end_index = end_index - 1  # store the index of the character in the line
        self.num_str = num_str  # store the integer corresponding to the number
        self.num_int = int(num_str)
        self.min_distance = None  # store the minimal distance

class Symbol:
    def __init__(self, line_number, index, symbol_str):
        self.line_number = line_number
        self.index = index
        self.symbol_str = symbol_str  # store the string corresponding to the symbol

class Line:
    def __init__(self, line_index, numbers=None, symbols=None):
        self.line_index = line_index
        self.numbers = numbers if numbers else []
        self.symbols = symbols if symbols else []

def read_file(file_name):
    lines = []
    with open(file_name, 'r') as file:
        for line_index, line in enumerate(file, start=1):
            numbers = []
            symbols = []
            for match in re.finditer(r"\d+", line):
                num_str = match.group()  # get the string corresponding to the number
                numbers.append(Number(line_index, match.start(), match.end(), num_str))
            for match in re.finditer(r"[^\d\.\n]", line):  # exclude end of line from symbols
                symbol_str = match.group()  # get the string corresponding to the symbol
                symbols.append(Symbol(line_index, match.start(), symbol_str))
            lines.append(Line(line_index, numbers, symbols))
    return lines

# Call the function on the specified file
lines = read_file("input.txt")

def print_summary(lines):
    for line in lines:
        print(f"Line {line.line_index}: {len(line.numbers)} numbers, {len(line.symbols)} symbols")
        for number in line.numbers:
            print(f"Number: {number.num_str}")  # print the string of each number
        for symbol in line.symbols:
            print(f"Symbol: {symbol.symbol_str}")  # print the string of each symbol

# Call the function to print the summary of all lines
# print_summary(lines)

# Define a function to compute the distance between a symbol and the closest digit of a number
def compute_distance(symbol, number):
    # Compute the distance between the symbol index and the number begin and end index
    distance_to_begin = abs(symbol.index - number.begin_index)
    distance_to_end = abs(symbol.index - number.end_index)

    # Return the smallest distance
    return min(distance_to_begin, distance_to_end)

# Iterate over all lines
for i, line in enumerate(lines):
    # Iterate over all numbers in the line
    for number in line.numbers:
        # If the line is not the first one, compute the distance with the symbols of the previous line
        if i > 0:
            prev_line = lines[i - 1]
            for symbol in prev_line.symbols:
                distance = compute_distance(symbol, number)
                if number.min_distance is None or distance < number.min_distance:
                    number.min_distance = distance

        # Compute the distance with the symbols of the current line
        for symbol in line.symbols:
            distance = compute_distance(symbol, number)
            if number.min_distance is None or distance < number.min_distance:
                number.min_distance = distance

        # If the line is not the last one, compute the distance with the symbols of the next line
        if i < len(lines) - 1:
            next_line = lines[i + 1]
            for symbol in next_line.symbols:
                distance = compute_distance(symbol, number)
                if number.min_distance is None or distance < number.min_distance:
                    number.min_distance = distance

# Define a function to print the line number, number, and minimum distance for each number
def print_number_details(lines):
    for line in lines:
        for number in line.numbers:
            print(f"Line {number.line_number}: Number {number.num_str} with minimum distance {number.min_distance}")

# Call the function to print the details for each number
print_number_details(lines)

# Initialize the total integer
total = 0

# Iterate over all lines
for line in lines:
    # Iterate over all numbers in the line
    for number in line.numbers:
        # If the minimal distance is less than or equal to one, add the integer of the number to the total
        if number.min_distance <= 1:
            total += number.num_int

# Print the total with context
print(f"The total sum of numbers with minimal distance equal to one is: {total}")
