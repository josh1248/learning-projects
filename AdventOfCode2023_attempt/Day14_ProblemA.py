#text input is "DayX_Input.txt"
import numpy as np
day_number = 14
def main():
    input = np.array([list(line.strip()) for line in read_file()])
    def weight_on_north(grid):
        grid = np.transpose(grid)
        total_weight = 0
        for row in grid:
            row = row[::-1]
            rounded_rocks = 0
            for index, char in enumerate(row, 1): #1-indexed
                if char == "O":
                    rounded_rocks += 1
                elif char == "#":
                    total_weight += sum(range(index - rounded_rocks, index))
                    rounded_rocks = 0
            total_weight += sum(range(len(row) - rounded_rocks + 1, len(row) + 1))
        return total_weight
    print(weight_on_north(input))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()