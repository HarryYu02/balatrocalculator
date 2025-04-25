from enum import Enum
import random

class Suit(Enum):
    HEART = 'h'
    DIAMOND = 'd'
    CLUB = 'c'
    SPADE = 's'

class Rank(Enum):
    TWO = '2'
    THREE = '3'
    FOUR = '4'
    FIVE = '5'
    SIX = '6'
    SEVEN = '7'
    EIGHT = '8'
    NINE = '9'
    TEN = 'T'
    JACK = 'J'
    QUEEN = 'Q'
    KING = 'K'
    ACE = 'A'

class Card:
    rank: Rank
    suit: Suit
    is_wild: bool
    is_stone: bool

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.is_wild = False
        self.is_stone = False

    def __str__(self):
        return f'{self.suit.value}{self.rank.value}'

    def __eq__(self, other):
        return isinstance(other, Card) and \
            self.suit == other.suit and \
            self.rank == other.rank

class Deck:
    cards: list[Card]
    suit_order = [Suit.SPADE, Suit.HEART, Suit.CLUB, Suit.DIAMOND]
    rank_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']

    def __init__(self, deck=None):
        self.cards = deck if deck is not None else [Card(rank, suit) for suit in Suit for rank in Rank]

    def __str__(self):
        return '[' + ', '.join(str(card) for card in self.cards) + ']'

    def print_deck_by_suit(self):
        suit_to_cards = {suit: [] for suit in self.suit_order}

        for card in self.cards:
            suit_to_cards[card.suit].append(card)

        for suit in self.suit_order:
            cards = suit_to_cards[suit]
            line = " ".join(str(card) for card in cards)
            print(f"{suit.name}: {line}")

    def shuffle(self):
        random.shuffle(self.cards)

    def grab(self, card):
        self.cards.remove(card)
        return Card(rank=card.rank, suit=card.suit)

    def draw(self):
        drawn = self.cards[0]
        self.cards = self.cards[1:]
        return drawn

    def draw_many(self, n: int) -> list[Card]:
        drawn = []
        for _ in range(n):
            drawn.append(self.draw())
        return drawn

    def sort(self):
        def card_sort_key(card: Card):
            suit_index = self.suit_order.index(card.suit)
            rank_index = self.rank_order.index(card.rank.value)
            return (suit_index, rank_index)

        self.cards.sort(key=card_sort_key)
