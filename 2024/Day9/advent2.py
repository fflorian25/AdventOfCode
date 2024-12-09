
import sys

class Index:
    def __init__(self, isEmpty, place=None):
        self.isEmpty = isEmpty
        self.place = place
        self.alreadySwaped = False
    
    def __repr__(self):
        return (f"Index(isEmpty={self.isEmpty}, place={self.place})")


def read_file(file_path):
    index_list = []
    
    try:
        with open(file_path, 'r') as file:
            data = file.read()
        
        for i, char in enumerate(data):
            if char.isdigit():  # Ensure the character is a number
                value = int(char)
                if i % 2 == 0:  # Even number
                    index_list.extend([Index(isEmpty=False, place=i/2) for _ in range(value)])
                else:  # Odd number
                    index_list.extend([Index(isEmpty=True) for _ in range(value)])
                    
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except ValueError as e:
        print(f"Error processing file: {e}")
    
    return index_list

def find_first_n_consecutive_is_empty(index_objects, n):
    """
    Finds the index of the first occurrence of N consecutive isEmpty=True objects.
    
    :param index_objects: List of Index objects.
    :param n: Number of consecutive isEmpty=True objects to find.
    :return: The starting index of the first N consecutive isEmpty=True objects, or -1 if not found.
    """
    count = 0  # Counter for consecutive isEmpty=True
    for i, obj in enumerate(index_objects):
        if obj.isEmpty:
            count += 1
            if count == n:  # Found N consecutive isEmpty=True
                return i - n + 1  # Return the starting index
        else:
            count = 0  # Reset counter if a non-isEmpty object is encountered
    return -1  # Return -1 if no such sequence is found

def swap_memory(index_objects):
    """
    Swaps the last Not-Empty Index group with the first isEmpty Index group
    of the same size in the list.
    """
    first_empty_idx = None
    last_not_empty_idx_begin = None
    last_not_empty_idx_end = None
    
    # Find the end of the last Not-Empty group
    for i in range(len(index_objects) - 1, -1, -1):
        if not index_objects[i].isEmpty and not index_objects[i].alreadySwaped:
            last_not_empty_idx_end = i
            break

    if last_not_empty_idx_end is None:
        return False  # No Not-Empty block found    

    # Find the beginning of the last Not-Empty group
    for i in range(last_not_empty_idx_end - 1, -1, -1):
        if index_objects[i].place != index_objects[last_not_empty_idx_end].place or index_objects[i].isEmpty:
            last_not_empty_idx_begin = i + 1
            break
    if last_not_empty_idx_begin is None:
        last_not_empty_idx_begin = 0  # Default to the start of the list

    # Calculate the size of the Not-Empty group
    group_size = last_not_empty_idx_end - last_not_empty_idx_begin + 1

    # Find the first occurrence of an empty block of the same size
    first_empty_idx = find_first_n_consecutive_is_empty(index_objects, group_size)

    if first_empty_idx != -1 and first_empty_idx < last_not_empty_idx_begin :
        # Mark the swapped Not-Empty block to prevent future swaps
        for i in range(last_not_empty_idx_begin, last_not_empty_idx_end + 1):
            index_objects[i].alreadySwaped = True
        # Perform the swap
        for i in range(group_size):
            index_objects[first_empty_idx + i], index_objects[last_not_empty_idx_begin + i] = (
                index_objects[last_not_empty_idx_begin + i],
                index_objects[first_empty_idx + i],
            )            
    else :
        # Mark the swapped Not-Empty block to prevent future swaps
        for i in range(last_not_empty_idx_begin, last_not_empty_idx_end + 1):
            index_objects[i].alreadySwaped = True
            
    return True  # Swap was performed
   

def sort_indices(index_objects):
    """
    Repeatedly applies swap_memory until all isEmpty=True objects are at the end of the list.
    """
    while swap_memory(index_objects):
        pass  # Continue swapping until no more swaps are possible


def pretty_print(index_objects):
    """
    Prints the Index objects in a readable table format.
    """
    print(f"{'Index':<10} {'isEmpty':<10} {'Place':<10}")
    print("=" * 30)
    for i, obj in enumerate(index_objects):
        place_str = str(obj.place) if obj.place is not None else "N/A"
        print(f"{i:<10} {str(obj.isEmpty):<10} {place_str:<10}")

# Execution starts here
if __name__ == "__main__":
    """
    Prints the number of antinide cases.
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    indexes = read_file(filename)
    
    #pretty_print(indexes)
    sort_indices(indexes)
    #pretty_print(indexes)

    sum = 0
    for i, index in enumerate(indexes):
        if not index.isEmpty:
            sum += i*index.place

    print(f"Sum: {int(sum)}")
