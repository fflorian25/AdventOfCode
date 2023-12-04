
class Card:
    def __init__(self, index):
        self.index = index
        self.winning_numbers = []
        self.scratched_numbers = []
        self.winning_scratched_numbers = []
        self.number_of_instances = 1

    def add_winning_number(self, number):
        self.winning_numbers.append(number)

    def add_scratched_number(self, number):
        self.scratched_numbers.append(number)
        if number in self.winning_numbers:
            self.winning_scratched_numbers.append(number)

    @classmethod
    def from_file(cls, filename):
        cards = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                index, card_data = line.split(":")
                card = cls(index)
                parts = card_data.split("|")
                winning_numbers = [int(num) for num in parts[0].split() if num.isdigit()]
                scratched_numbers = [int(num) for num in parts[1].split() if num.isdigit()]
                for num in winning_numbers:
                    card.add_winning_number(num)
                for num in scratched_numbers:
                    card.add_scratched_number(num)
                cards.append(card)
        return cards

def update_instances(cards):
    for i in range(len(cards)):
        n = len(cards[i].winning_scratched_numbers)
        for j in range(i+1, min(i+n+1, len(cards))):
            cards[j].number_of_instances += cards[i].number_of_instances

# reading cards from file
cards = Card.from_file('input.txt')

# updating instances
update_instances(cards)

def print_cards_summary(cards):
    for i, card in enumerate(cards, start=1):
        print(f"Card {i}:")
        print(f"Winning Numbers: {card.winning_numbers}")
        print(f"Scratched Numbers: {card.scratched_numbers}")
        print(f"Winning Scratched Numbers: {card.winning_scratched_numbers}")
        print("-------------------------")

# printing cards summary
#print_cards_summary(cards)

# calculate total number of instances
total_instances = sum(card.number_of_instances for card in cards)

# print total number of instances
print(f"Total number of instances: {total_instances}")
