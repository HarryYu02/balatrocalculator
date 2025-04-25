from deck import Deck

def test_draw():
    deck = Deck()
    top = deck.draw()
    print(top)
    print(deck)
