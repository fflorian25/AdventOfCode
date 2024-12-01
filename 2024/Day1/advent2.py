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

def compute_similarity(column1, column2):
    """
    Compute the similarity between two sorted lists.

    :param column1: First set of numbers (sorted).
    :param column2: Second set of numbers (sorted).
    :return: The similarity score, calculated by summing each number in column1 
             multiplied by its occurrences in column2.
    """
    total_sim = 0
    i, j = 0, 0  # Pointers for column1 and column2

    while i < len(column1) and j < len(column2):
        if column1[i] < column2[j]:
            # Current column1[i] does not match column2[j], move to next column1
            i += 1
        elif column1[i] > column2[j]:
            # Current column1[i] is greater, move to the next column2
            j += 1
        else:
            # column1[i] == column2[j], count occurrences of column1[i] in column2
            occurrences = 0
            while j < len(column2) and column2[j] == column1[i]:
                occurrences += 1
                j += 1
            # Add to total similarity
            total_sim += column1[i] * occurrences
            i += 1

    return int(total_sim)



#### Begin of MAIN
#extract the columns
col1, col2 = read_file_columns('input.txt')

#sort columns
col1.sort()
col2.sort()

#compute the diff
Total = compute_similarity(col1, col2)

print(f'Total similarities: {Total}')
