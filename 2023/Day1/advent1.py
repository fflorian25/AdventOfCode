def extract_figures(file_path):
    total = 0
    with open(file_path, 'r') as file:
        for line in file:
            figures = [char for char in line if char.isdigit()]
            if figures:
                if len(figures) > 1:
                    total += int(figures[0] + figures[-1])  # concatenate first and last figure
                else:
                    total += int(figures[0] * 2)  # create a double digit number by repeating the figure
    print(f'Total sum of figures: {total}')

# usage
extract_figures('input.txt')
