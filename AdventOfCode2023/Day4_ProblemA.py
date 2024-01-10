#text input is "DayX_Input.txt"
day_number = 4

def main():
    input = read_file()
    total_points = 0

    for row in input:
        start_pos, mid_pos = row.find(":"), row.find("|")
        winning_nums = row[start_pos + 1:mid_pos].split()
        nums_you_have = row[mid_pos + 1:].split()
        
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