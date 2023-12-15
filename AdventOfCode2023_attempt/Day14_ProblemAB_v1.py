#text input is "DayX_Input.txt"
import numpy as np
import copy
day_number = 14
def main():
    input = np.array([list(line.strip()) for line in read_file()])
    def weight_on_north(grid):
        total = 0
        for i in range(1, len(grid) + 1):
            total += (grid[-i] == "O").sum() * i #eq of .count()
        return total

    def tilt_platform(grid, direction):
        if direction == "North":
            return np.transpose(tilt_platform(np.transpose(grid), "West"))
        elif direction == "South":
            return np.transpose(tilt_platform(np.transpose(grid), "East"))
        elif direction == "West":
            return np.fliplr(tilt_platform(np.fliplr(grid), "East"))

        for r, row in enumerate(grid):
            rounded_rocks, last_cube_rock = 0, -1
            for c, char in enumerate(row):
                if char == "O":
                    rounded_rocks += 1
                elif char == "#":
                    grid[r, (c - rounded_rocks):c] = "O"
                    grid[r, (last_cube_rock + 1):(c - rounded_rocks)] = "."
                    last_cube_rock = c
                    rounded_rocks = 0
            if rounded_rocks:
                grid[r, -rounded_rocks:] = "O"
                grid[r, (last_cube_rock + 1):-rounded_rocks] = "."

        return grid

    def spin_cycle(grid):
        for direction in ["North", "West", "South", "East"]:
            grid = tilt_platform(grid, direction)
        return grid
    
    print(f"Part 1: {weight_on_north(tilt_platform(input, 'North'))}")
    results = []
    for i in range(100000):
        input = spin_cycle(input)
        matches = [(i, m) for i, m in enumerate(results) if np.array_equal(m, input)]
        if not matches:
            results.append(copy.deepcopy(input))
        else:
            offset = matches[0][0]
            cycle = len(results) - offset
            break

    print(f"Part 2: {weight_on_north(results[(1_000_000_000 - offset - 1) % cycle + offset])}")

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()