
import sys

def concat(num1, num2):
    return int(str(num1) + str(num2))

class Equation:
    """
    Class representing an Equation with an equation string and a list of numbers.
    """
    def __init__(self, equation, numbers=None):
        """
        Constructor for the Equation class.
        :param equation: The equation string.
        :param numbers: List of numbers involved in the equation.
        """
        self.equation = int(equation)
        self.numbers = numbers if numbers else []

    def add_number(self, number):
        """
        Method to add a number to the list of numbers.
        :param number: The number to add.
        """
        self.numbers.append(number)

    def pretty_print(self):
        """
        Method to print the equation and the list of numbers.
        """
        print(f"Equation: {self.equation}")
        print(f"Numbers: {', '.join(str(num) for num in self.numbers)}")
        print("-"*20)
        
    def is_possible(self):
        """
        Method to check if the equation can be solved with the given numbers.
        :return: True if the equation can be solved, False otherwise.
        """
        from itertools import product
    
        # Create a list of all possible variations of "*" and "+"
        variations = list(product(["*", "+", "||"], repeat=len(self.numbers)-1))
    
        # Iterate over all variations
        for variation in variations:
            numbers_copy = self.numbers[:]
                    
            #print(numbers_copy)
            # Start with the first number
            res = numbers_copy[0]
            # Iterate over the rest of the numbers
            for i in range(1, len(numbers_copy)):
                # Apply the operation from the variation to the result and the next number
                #print(variation)
                if variation[i-1] == "*":
                    res = res * numbers_copy[i]
                elif variation[i-1] == "+":
                    res = res + numbers_copy[i]
                elif variation[i-1] == "||":
                    res = concat(res, numbers_copy[i])
                else:
                    print("ERROR")
            # Check if the result matches the equation
            #print(res)
            if res == self.equation:
                return True
    
        # If no variation solved the equation, return False
        return False
        

def parse_file(filename):
    """
    Function to parse a file and create a list of Equation objects.
    :param filename: The name of the file to parse.
    :return: List of Equation objects.
    """
    equations = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line == '':
                continue
            equation, num = line.split(':')
            numbers = list(map(int, num.split()))
            equations.append(Equation(equation, numbers))

    return equations

if __name__ == "__main__":
    """
    Main function to parse the file, create pages and updates, and print the total count of pages.
    """
    filename = sys.argv[1] if len(sys.argv) > 1 else 'input.txt'
    equations = parse_file(filename)
    res = 0
    
    #for eq in [equations[3]]:
    for eq in equations:
        eq.pretty_print()
        if eq.is_possible():
            res += eq.equation

    print(f"Resultat of possible equation: {res}")
