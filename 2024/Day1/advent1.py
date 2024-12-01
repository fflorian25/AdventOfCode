def read_file_columns(file_name):
    """
    Reads a text file containing two columns of numbers separated by a space
    and returns two lists, one for each column.

    :param file_name: The name of the text file to read.
    :return: Two lists containing the numbers from each column.
    """
    column1 = []
    column2 = []
    
    try:
        with open(file_name, 'r') as file:
            for line in file:
                # Strip unnecessary spaces and skip empty lines
                line = line.strip()
                if line:
                    # Split the line into two columns
                    values = line.split()
                    if len(values) == 2:  # Ensure the line has exactly two values
                        column1.append(float(values[0]))
                        column2.append(float(values[1]))
                    else:
                        print(f'Line skipped (not two columns): {line}')
    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return column1, column2

def compute_distance(column1, column2):
    """
    Compute the distance between two lists.

    :param column1: First set of numbers.
    :param column2: Second set of numbers.
    :return: Sum of distances between each corresponding element of the lists.
    """
    dist = 0

    if len(column1) != len(column2):
        raise ValueError("The two lists must have the same length.")

    for i in range(len(column1)):
        dist += abs(column1[i] - column2[i])  # Use absolute value 

    return int(dist)


#### Begin of MAIN
#extract the columns
col1, col2 = read_file_columns('input.txt')

#sort columns
col1.sort()
col2.sort()

#compute the diff
dist = compute_distance(col1, col2)

print(f'Total distances: {dist}')
