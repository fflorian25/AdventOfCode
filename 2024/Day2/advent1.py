
def read_file(filename):
    # Open the file in read mode
    with open(filename, 'r') as file:
        # Read all lines
        lines = file.readlines()
    data = []
    # Process each line
    for line in lines:
        # Convert each number in the line to int and add to an array
        numbers = [int(num) for num in line.split()]
        # Add the array to the list
        data.append(numbers)
    # Return the list of arrays
    return data

def is_safe(array):
    # Check if all elements are in increasing order or in decreasing order
    if all(array[i] <= array[i + 1] for i in range(len(array) - 1)) or all(array[i] >= array[i + 1] for i in range(len(array) - 1)):
        # Check if the difference between each pair of elements is at least 1 and at most 3
        if all(1 <= abs(array[i + 1] - array[i]) <= 3 for i in range(len(array) - 1)):
            # If all conditions are met, return True
            return True
    # If any condition is not met, return False
    return False

#### Begin of MAIN
# Read the file and get the data
reports = read_file('input.txt')

# Initialize the count of safe arrays
safe_count = 0
# Process each array
for report in reports:
    # If the array is safe, increment the count
    if is_safe(report):
        safe_count += 1

# Print the count of safe arrays
print(f'The Total number is', {safe_count})
