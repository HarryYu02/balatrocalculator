from enum import Enum
from collections import Counter
from deck import Card, Suit

class HandType(Enum):
    FLUSHFIVE = 11
    FLUSHHOUSE = 10
    FIVEOFAKIND = 9
    STRAIGHTFLUSH = 8
    FOUROFAKIND = 7
    FULLHOUSE = 6
    FLUSH = 5
    STRAIGHT = 4
    THREEOFAKIND = 3
    TWOPAIR = 2
    PAIR = 1
    HIGHCARD = 0

class Hand:
    cards: list[Card]
    suit_order = [Suit.SPADE, Suit.HEART, Suit.CLUB, Suit.DIAMOND]
    rank_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    rank_order_map = {
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'T': 10,
        'J': 11,
        'Q': 12,
        'K': 13,
        'A': 14
    }

    def __init__(self, cards):
        self.cards = cards

    def __len__(self):
        return len(self.cards)

    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.cards) + ']'

    def sort(self):
        def card_sort_key(card: Card):
            suit_index = self.suit_order.index(card.suit)
            rank_index = self.rank_order.index(card.rank.value)
            return (rank_index, suit_index)

        self.cards.sort(key=card_sort_key)

    def discard(self):
        pass

    def eval_hand(self):
        unique_rank_values = sorted({self.rank_order_map[card.rank.value] for card in self.cards})
        rank_counts = Counter(self.rank_order_map[card.rank.value] for card in self.cards)
        suit_counts = Counter(card.suit.value for card in self.cards)

        # print(unique_rank_values)
        # print(rank_counts)
        # print(suit_counts)

        def is_straight():
            # A, 2, 3, 4, 5
            if set([2, 3, 4, 5, 14]).issubset(unique_rank_values):
                return True

            for i in range(len(unique_rank_values) - 4):
                window = unique_rank_values[i:i+5]
                if all(window[j] - window[j-1] == 1 for j in range(1, 5)):
                    return True

            return False

        def is_fullhouse():
            counts = list(rank_counts.values())

            has_three = any(count >= 3 for count in counts)
            has_pair = any(count >= 2 for count in counts if count != 3 or counts.count(3) > 1)

            return has_three and has_pair

        def is_two_pair():
            counts = list(rank_counts.values())

            has_three = any(count >= 2 for count in counts)
            has_pair = any(count >= 2 for count in counts if count != 2 or counts.count(2) > 1)

            return has_three and has_pair

        if 4 in rank_counts.values():
            return HandType.FOUROFAKIND

        if is_fullhouse():
            return HandType.FULLHOUSE

        if any(count >= 5 for count in suit_counts.values()):
            return HandType.FLUSH

        if is_straight():
            return HandType.STRAIGHT

        if 3 in rank_counts.values():
            return HandType.THREEOFAKIND

        if is_two_pair():
            return HandType.TWOPAIR

        if 2 in rank_counts.values():
            return HandType.PAIR


        return HandType.HIGHCARD
