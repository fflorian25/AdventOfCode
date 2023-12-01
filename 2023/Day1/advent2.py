
def extract_figures(file_path):
    total = 0
    numbers_in_words = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0}
    with open(file_path, 'r') as file:
        for line in file:
            figures = []
            index = 0
            while index < len(line):
                if line[index].isdigit():  # check if the digit is in the line
                    figures.append(int(line[index]))
                    index += 1
                else:
                    for word, digit in numbers_in_words.items():
                        if line[index:].startswith(word):
                            figures.append(digit)
                            index += 1  # increment index by one
                            break
                    else:  # increment index by one if no digit or word is found at a place
                        index += 1
            print(figures)
            if figures:
                if len(figures) > 1:
                    total += int(str(figures[0]) + str(figures[-1]))  # concatenate first and last figure
                    print(str(figures[0]) + str(figures[-1]))
                else:
                    total += int(str(figures[0]) * 2)  # create a double digit number by repeating
                    print(str(figures[0]) * 2)
    print(f'Total sum of figures: {total}')

# usage
extract_figures('input.txt')
