from deck import Deck, Card

class Calculator():
    hand = list[Card]
    deck = Deck

    def __init__(self, hand, deck):
        self.hand = hand
        self.deck = deck

    def calculate(self, target):
        pass
