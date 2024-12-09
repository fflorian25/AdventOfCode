
import sys

class Index:
    def __init__(self, isEmpty, place=None):
        self.isEmpty = isEmpty
        self.place = place
    
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

def swap_memory(index_objects):
    """
    Swaps the last Not-Empty Index object with the first isEmpty Index object in the list.
    """
    first_empty_idx = None
    last_not_empty_idx = None

    # Find the first isEmpty index
    for i, obj in enumerate(index_objects):
        if obj.isEmpty:
            first_empty_idx = i
            break
    
    # Find the last Not-Empty index
    for i in range(len(index_objects) - 1, -1, -1):
        if not index_objects[i].isEmpty:
            last_not_empty_idx = i
            break
    
    # Swap if both indices are found
    if first_empty_idx is not None and last_not_empty_idx is not None and first_empty_idx < last_not_empty_idx:
        index_objects[first_empty_idx], index_objects[last_not_empty_idx] = (
            index_objects[last_not_empty_idx],
            index_objects[first_empty_idx],
        )
        return True  # Indicates that a swap occurred
    return False  # No swap occurred


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
        else:
            break

    print(f"Sum: {int(sum)}")
