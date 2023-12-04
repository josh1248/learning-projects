#text input is "DayX_Input.txt"
day_number = 4
import re

def main():
    input = read_file()
    total_points = 0

    for row in input:
        start_pos, mid_pos = row.find(":"), row.find("|")
        winning_nums, nums_you_have = line[start_pos:mid_pos + 1].split(" "), line[mid_pos + 1:].split(" ")
        print(winning_nums)

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()