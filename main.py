from deck import Deck, Card, Rank, Suit
from utils import card_from_str, all_discard_combinations
from multiprocessing import Pool, cpu_count
from hand import Hand, HandType
from simulator import Simulator

def main():
    deck = Deck()
    deck.shuffle()
    drawn = deck.draw_many(8)
    hand = Hand(drawn)
    hand.sort()
    sim = Simulator(hand, deck)
    print(hand)

    discard_combo = all_discard_combinations()
    job_args = [(discard_indices) for discard_indices in discard_combo]
    with Pool(processes=cpu_count()) as pool:
        results = pool.map(sim.monte_carlo_fix_discard_by_idx, job_args)

    # print(results)
    ranked = [(discard_combo[i], results[i].get(HandType.STRAIGHT.name, 0)) for i in range(len(results))]
    ranked.sort(key=lambda x: x[1], reverse=True)

    for discard in ranked[:10]:
        print(discard)

if __name__ == "__main__":
    main()
