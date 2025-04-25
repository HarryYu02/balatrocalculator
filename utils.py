from deck import Card, Rank, Suit
from itertools import combinations

def all_discard_combinations(hand_size=8, max_discards=5):
    indices = list(range(hand_size))
    all_combos = []
    for r in range(0, max_discards + 1):
        all_combos.extend(combinations(indices, r))
    return all_combos

def card_from_str(card_str: str) -> Card:
    if len(card_str) != 2:
        raise ValueError("Card input must be exactly 2 characters (e.g. 'sA')")

    try:
        rank = next(r for r in Rank if r.value == card_str[1].upper())
        suit = next(s for s in Suit if s.value == card_str[0].lower())
    except StopIteration:
        raise ValueError("Invalid card input. Use format like 'sA', 'h2', 'dK'.")

    return Card(suit=suit, rank=rank)
