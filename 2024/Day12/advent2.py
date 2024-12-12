
import sys

def parse_file(filename):
    with open(filename) as f:
        map = {}
        for row, line in enumerate(f):
            for col, char in enumerate(line.rstrip()):
                map[(col, row)] = Plant(char, col, row)
    return map

class Plant:
    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y
        self.has_been_visited = False
        self.neighbour = []
        self.side = []
        self.perimeter = 0
        self.size = 1
        
    def __repr__(self):
        return f"Plant(type={self.type}, x={self.x}, y={self.y}, has_been_visited={self.has_been_visited}, neighbour={self.neighbour}, perimeter={self.perimeter}, size={self.size})"
def computeFence(plant, plants):
    # Mark the plant as visited
    plant.has_been_visited = True

    # Define the directions for adjacent plants
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Iterate over each direction
    for dx, dy in directions:
        # Calculate the coordinates of the adjacent plant
        adjacent_x = plant.x + dx
        adjacent_y = plant.y + dy

        # Check if the adjacent plant exists and is of the same type
        if (adjacent_x, adjacent_y) in plants and plants[(adjacent_x, adjacent_y)].type == plant.type:
            # If the adjacent plant has not been visited, recursively call computeFence
            if not plants[(adjacent_x, adjacent_y)].has_been_visited:
                computeFence(plants[(adjacent_x, adjacent_y)], plants)
                plant.size += plants[(adjacent_x, adjacent_y)].size  
            # If the adjacent plant has been visited,
            else:
                pass
        #store which plants has been wisited
        self.neighbour.append(dx, dy)
        # If the adjacent plant does not exist or is of a different type, add to the perimeter
        else:
            sel.perimeter += 1
            self.side.append((dx, dy))
    
    
    sides =      [(0, 1), (0, -1), (1, 0), (-1, 0)]
    # Iterate over each direction
    for dx, dy in directions:
        if (dx,dy) in self.neighbour:
            
    

if __name__ == "__main__":
    """
    Main function to execute the script
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    plants = parse_file(filename)
    res = 0

    for plant in plants.values():
        if not plant.has_been_visited:
            computeFence(plant, plants)
            print(plant)
            res += plant.perimeter * plant.size

    print(f"Result: {res}")
