
class Card:
    def __init__(self):
        self.winning_numbers = []
        self.scratched_numbers = []
        self.winning_scratched_numbers = []

    def add_winning_number(self, number):
        self.winning_numbers.append(number)

    def add_scratched_number(self, number):
        self.scratched_numbers.append(number)
        if number in self.winning_numbers:
            self.winning_scratched_numbers.append(number)

    def calculate_points(self):
        num_of_winning_scratched = len(self.winning_scratched_numbers)
        if num_of_winning_scratched > 0:
            return 2 ** (num_of_winning_scratched - 1)
        else:
            return 0

    @classmethod
    def from_file(cls, filename):
        cards = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                index, card_data = line.split(":")
                card = cls()
                parts = card_data.split("|")
                winning_numbers = [int(num) for num in parts[0].split() if num.isdigit()]
                scratched_numbers = [int(num) for num in parts[1].split() if num.isdigit()]
                for num in winning_numbers:
                    card.add_winning_number(num)
                for num in scratched_numbers:
                    card.add_scratched_number(num)
                cards.append(card)
        return cards

# reading cards from file
cards = Card.from_file('input.txt')

def print_cards_summary(cards):
    for i, card in enumerate(cards, start=1):
        print(f"Card {i}:")
        print(f"Winning Numbers: {card.winning_numbers}")
        print(f"Scratched Numbers: {card.scratched_numbers}")
        print(f"Winning Scratched Numbers: {card.winning_scratched_numbers}")
        print("-------------------------")

# printing cards summary
#print_cards_summary(cards)

# computing the sum of all card points
total_points = sum(card.calculate_points() for card in cards)

# printing the total points
print(f"Total Points: {total_points}")
