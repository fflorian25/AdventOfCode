from enum import Enum
from functools import cmp_to_key
from functools import total_ordering

@total_ordering
class Type(Enum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7
    def __lt__(self, other):
        if self.__class__ is other.__class__:
            return self.value < other.value
        return NotImplemented

def is_card1_stronger(card1, card2):
    card_order = "AKQJT98765432"

    if card1 not in card_order or card2 not in card_order:
        raise ValueError("Invalid card value")

    rank1 = card_order.index(card1)
    rank2 = card_order.index(card2)

    if rank1 < rank2:
        return 1
    elif rank1 > rank2:
        return -1
    else:
        return 0    

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.type = Type.HIGH_CARD


    def identic_cards(self):
        char_count = {}
        for char in self.cards:
            char_count[char] = char_count.get(char, 0) + 1
        return char_count
    
    def compute_type(self):
        identicCards = self.identic_cards()
        maxIdenticCards = max(identicCards.values())
        minIdenticCards = min(identicCards.values())
        occurrences = sum(1 for value in identicCards.values() if value == maxIdenticCards)

        if maxIdenticCards == 5:
               self.type = Type.FIVE_OF_A_KIND
        elif maxIdenticCards == 4:
               self.type = Type.FOUR_OF_A_KIND
        elif maxIdenticCards == 3:
            if minIdenticCards == 2:
               self.type = Type.FULL_HOUSE
            else:
               self.type = Type.THREE_OF_A_KIND
        elif maxIdenticCards == 2:
            if occurrences == 2:
               self.type = Type.TWO_PAIR
            else:            
               self.type = Type.ONE_PAIR
        else:
            self.type = Type.HIGH_CARD
               

    def comparator(self, other):
        #>
        if self.type > other.type :
            return 1
        #<
        elif self.type < other.type :
            return -1
        #=
        else :
            for i in range(0,5):
                oneStronger =  is_card1_stronger(self.cards[i], other.cards[i])
                if oneStronger == 1: 
                    return 1 
                elif oneStronger == -1:
                    return -1
        return 0

    @classmethod
    def from_file(cls, filename):
        hands = []
        with open(filename, 'r') as f:
            lines = f.readlines()
            for line in lines:
                cards, bids = line.split(" ")
                hand = Hand(cards, bids)
                hands.append(hand)
        return hands


# reading cards from file
hands = Hand.from_file('2023/Day7/input.txt')

for hand in hands:
    hand.compute_type()

def print_cards_summary(hands):
    for i, hand in enumerate(hands, start=1):
        print(f"Hand {i}:")
        print(f"Cards: {hand.cards}")
        print(f"Bid: {hand.bid}")
        print(f"Type: {hand.type}")
        print("-------------------------")


# sort the hands
sorted_hands = sorted(hands, key=cmp_to_key(Hand.comparator))

# printing cards summary
print_cards_summary(sorted_hands)

# print total bids
tot=0
for i, hand in enumerate(sorted_hands):
    tot += (i+1)*hand.bid

print(f"Total price: {tot}")
