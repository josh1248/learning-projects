#text input is "DayX_Input.txt"
day_number = 4

def main():
    input = read_file()
    total_points = 0

    for row in input:
        single_spaces_only = row.replace("  ", " ")
        start_pos, mid_pos = single_spaces_only.find(":"), single_spaces_only.find("|")
        winning_nums = single_spaces_only[(start_pos + 2):(mid_pos - 1)].split(" ")
        nums_you_have = single_spaces_only[(mid_pos + 2):-1].split(" ")
        
        matches = len(set(winning_nums).intersection(nums_you_have))
        if matches: #not zero evals to true
            total_points += 2 ** (matches - 1)

    print(total_points)

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()