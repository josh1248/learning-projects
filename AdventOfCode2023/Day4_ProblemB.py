#text input is "DayX_Input.txt"
day_number = 4
import functools

def main():
    input = read_file()
    ScratchCardsAt = {} #memoization holder

    #returns total scratch cards drawn if starting at card i
    def scratch_cards_at(index):
        val = ScratchCardsAt.get(index)
        if val is not None:
            return val
        
        row = input[index]
        start_pos, mid_pos = row.find(":"), row.find("|")
        winning_nums = row[start_pos + 1:mid_pos].split()
        nums_you_have = row[mid_pos + 1:].split()
        
        matches = len(set(winning_nums).intersection(nums_you_have))
        total_scratch_cards = 1
        for i in range(matches):
            total_scratch_cards += scratch_cards_at(index + i + 1)

        ScratchCardsAt[index] = total_scratch_cards
        return total_scratch_cards

    print(functools.reduce(lambda running_sum, pos: running_sum + scratch_cards_at(pos), range(len(input)), 0))

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()