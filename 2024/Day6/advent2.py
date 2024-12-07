
import sys

# This function reads the file and appends each character to the letters list
def read_file(filename):
    cases = []
    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            for col, char in enumerate(line.strip()):
                cases.append(Case(char, col, row))
    return cases

# This class represents a Letter with its value and position
class Case:
    def __init__(self, value, col, row):
        self._value = value
        self._col = col
        self._row = row
        self._isEmpty = self._value in ["."]
        self._hasBeenVisited = self._value in ["^"]
        self._isWall = self._value in ["#"]
        self._visitedInDirection = []
        
    def check_duplicate_direction(self):
        #print(self._visitedInDirection)
        return len(self._visitedInDirection) != len(set(self._visitedInDirection))
    
    def pretty_print(self):
        print(f"Row: {self._row}, Col: {self._col}")
        
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        self._value = new_value
        self._isEmpty = self._value in ["."]
        self._isWall = self._value in ["#"]
        if self._hasBeenVisited == False:
            self._hasBeenVisited = self._value in ["^"]

    @property
    def col(self):
        return self._col

    @col.setter
    def col(self, new_col):
        self._col = new_col

    @property
    def row(self):
        return self._row

    @row.setter
    def row(self, new_row):
        self._row = new_row

    @property
    def isEmpty(self):
        return self._isEmpty

    @isEmpty.setter
    def isEmpty(self, new_isEmpty):
        self._isEmpty = new_isEmpty

    @property
    def hasBeenVisited(self):
        return self._hasBeenVisited

    @hasBeenVisited.setter
    def hasBeenVisited(self, new_hasBeenVisited):
        self._hasBeenVisited = new_hasBeenVisited     
        
    @property
    def visitedInDirection(self):
        return self._visitedInDirection

    @visitedInDirection.setter
    def visitedInDirection(self, new_visitedInDirection):
        self._visitedInDirection.append(new_visitedInDirection)

    @property
    def isWall(self):
        return self._isWall

    @isWall.setter
    def isWall(self, new_isWall):
        self._isWall = new_isWall

def pretty_print(cases, max_row, max_col):
    for row in range(max_row+1):
        for col in range(max_col+1):
            case = [c for c in cases if c.row == row and c.col == col]
            if case:
                if case[0].isWall:
                    print("#", end='')
                elif case[0].hasBeenVisited:
                    print("+", end='')
                else:
                    print(".", end='')
            else:
                print(" ", end='')
        print()

# This function looks for the guard in the cases list
def look_for_guard(cases):
    for case in cases:
        if case.value == "^":
            return case
    return None

def go(case, cases, direction):
    if direction == 'U':
        next_case = [c for c in cases if c.row == case.row-1 and c.col == case.col]
    elif direction == 'D':
        next_case = [c for c in cases if c.row == case.row+1 and c.col == case.col]
    elif direction == 'L':
        next_case = [c for c in cases if c.row == case.row and c.col == case.col-1]
    elif direction == 'R':
        next_case = [c for c in cases if c.row == case.row and c.col == case.col+1]

    if next_case:
        if next_case[0].isWall:
            return case
        else:
            next_case[0].hasBeenVisited = True
            return go(next_case[0], cases, direction)
    else:
        return case

def count_visited_cases(cases):
    return sum(case.hasBeenVisited for case in cases)

def extract_all_visited(cases, starting_point):
    visited_cases = [case for case in cases if case.hasBeenVisited and case != starting_point]
    return visited_cases

def reinit_all_visited(visited, cases):
    for case in cases:
        for visit_case in visited:
            if (case.col == visit_case.col) and (case.row == visit_case.row):
                case.isWall = False
                case._visitedInDirection = []
        case.hasBeenVisited = False
        
def reinit_all(cases):
    for case in cases:            
        case._visitedInDirection = []
        case.hasBeenVisited = False        

# Execution starts here
if __name__ == "__main__":
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    cases = read_file(filename)

    starting_guard=look_for_guard(cases)
    guard = look_for_guard(cases)

    direction ="U"

    max_col = max(case.col for case in cases)
    max_row = max(case.row for case in cases)
    directions = ["U", "R", "D", "L"]
    direction_index = 0

    # Create a dictionary for faster lookup
    cases_dict = {(case.row, case.col): case for case in cases}

    while ((guard.col != 0) and (guard.col != max_col) and (guard.row != 0) and (guard.row != max_row)):
        guard = go(guard, cases, directions[direction_index])
        direction_index = (direction_index + 1) % len(directions) # This will cycle through the directions

    visited=count_visited_cases(cases)

    #extract all the cases visited :
    visited_cases = extract_all_visited(cases, starting_guard)

    loop_number = 0
    counter=0
    #for visit_case in [visited_cases[12]]:
    for visit_case in visited_cases:
        print(f"Progress: {counter/len(visited_cases)*100:.2f}%")
        counter+=1
        reinit_all(cases)

        # Use the dictionary for faster lookup
        case = cases_dict.get((visit_case.row, visit_case.col))
        if case:
            case.isWall = True
        guard = starting_guard

        direction_index = 0
        while ((guard.col != 0) and (guard.col != max_col) and (guard.row != 0) and (guard.row != max_row)):
            guard = go(guard, cases, directions[direction_index])
            guard.visitedInDirection.append(directions[direction_index])
            direction_index = (direction_index + 1) % len(directions) # This will cycle through the directions
            if guard.check_duplicate_direction():
                loop_number += 1
                break

        # Use the dictionary for faster lookup
        case = cases_dict.get((visit_case.row, visit_case.col))
        if case:
            case.isWall = False

    print(f"Found {loop_number} loops possible.")
