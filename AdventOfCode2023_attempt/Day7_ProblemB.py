#text input is "DayX_Input.txt"
day_number = 7

def main():
    input = read_file()
    hand_and_bids = [line.split() for line in input]
    def type_strength(hand):
        #high card: strength 1, ..., five of a kind: strength 7
        uniques = list(set(hand))
        if len(uniques) == 1: return 7
        elif len(uniques) == 2:
            if hand.count(uniques[0]) in [1, 4]: return 6
            else: return 5
        elif len(uniques) == 3:
            counts = map(hand.count, uniques)
            if 3 in counts: return 4
            else: return 3
        elif len(uniques) == 4: return 2
        else: return 1
    
    def type_strength_with_joker(hand):
        if "J" not in hand:
            return type_strength(hand)
        else:
            uniques = list(set(hand))
            return max([type_strength(hand.replace("J", letter)) for letter in uniques])

    letters = ["J"] + [str(i) for i in range(2, 10)] + ["T", "Q", "K", "A"]
    strengths = {letter: strength for strength, letter in enumerate(letters, 1)}
    
    def hand_strength(hand):
        return [type_strength_with_joker(hand)] + list(map(lambda char: strengths[char], hand))
    
    #Python's sorted function automatically sorts arrays based on index 0, then index 1 if drawn, etc.
    sorted_hands = sorted(hand_and_bids, key=lambda hand_bid: hand_strength(hand_bid[0]))

    score_tallies = [rank * int(hand_bid[1]) for rank, hand_bid in enumerate(sorted_hands, 1)]
    print(sum(score_tallies))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()