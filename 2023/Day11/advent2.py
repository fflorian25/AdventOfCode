
class Galaxy:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.distance = []
        self.tot_distance = 0
    def calculate_distances(self, galaxies):
        for galaxy in galaxies:
            if galaxy is not self:
                distance = abs(galaxy.row - self.row) + abs(galaxy.column - self.column)
                self.distance.append(distance)
                self.tot_distance += distance

def read_file_and_create_galaxies(filename):
    galaxies = []
    with open(filename, 'r') as file:
        for row, line in enumerate(file):
            for column, char in enumerate(line):
                if char == '#':
                    galaxies.append(Galaxy(row, column))
    return galaxies

galaxies = read_file_and_create_galaxies("input.txt")

def pretty_print_galaxies(galaxies):
    for galaxy in galaxies:
        print(f"Galaxy at row {galaxy.row} and column {galaxy.column}")

#pretty_print_galaxies(galaxies)
def find_empty_columns(galaxies):
    columns_with_galaxies = set(galaxy.column for galaxy in galaxies)
    all_columns = set(range(max(columns_with_galaxies) + 1))
    empty_columns = all_columns - columns_with_galaxies
    return empty_columns

empty_columns = find_empty_columns(galaxies)

def find_empty_rows(galaxies):
    rows_with_galaxies = set(galaxy.row for galaxy in galaxies)
    all_rows = set(range(max(rows_with_galaxies) + 1))
    empty_rows = all_rows - rows_with_galaxies
    return empty_rows

empty_rows = find_empty_rows(galaxies)

def expand_galaxy(galaxies, empty_columns, empty_rows):
    for galaxy in galaxies:
        for empty_column in sorted(empty_columns, reverse=True):
            if galaxy.column > empty_column:
                galaxy.column += 1000000-1
        for empty_row in sorted(empty_rows, reverse=True):
            if galaxy.row > empty_row:
                galaxy.row += 1000000-1

expand_galaxy(galaxies, empty_columns, empty_rows)

#pretty_print_galaxies(galaxies)

for galaxy in galaxies:
    galaxy.calculate_distances(galaxies)

#for galaxy in galaxies:
#    print(f"Distances for galaxy at row {galaxy.row} and column {galaxy.column}: {galaxy.distance}")

# Divide the total distance by two in order to compute each pair only once
total_distance = sum(galaxy.tot_distance for galaxy in galaxies) / 2
print(f"The sum of all total distances is: {total_distance}")
