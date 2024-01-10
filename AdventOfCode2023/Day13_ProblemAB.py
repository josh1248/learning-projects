#text input is "DayX_Input.txt"
day_number = 13
import numpy as np
def main():
    input = [np.array([list(line) for line in grid.split("\n")]) for grid in read_file().split("\n\n")]
        
    def row_wise_symmetry(grid, smudges):
        height, width = grid.shape
        #each bucket i shows equal rows along mirror below row i (0-indexed)
        row_symmetries = [[] for _ in range(height - 1)]
        smudge_candidates = []
        #reflect between rows only -> their row numbers add up to an odd number
        for i, j in [(i, j) for i in range(height) for j in range(i + 1, height, 2)]:
            row = (i + j - 1) // 2
            result = sum(grid[i] == grid[j]) #check how many elements match
            if result == width:
                row_symmetries[row].append((i, j))
            if result == width - smudges:
                smudge_candidates.append(row)

        total = 0
        for rownum, row in enumerate(row_symmetries):
            #for a grid with h rows, a mirror exists below row i iff there are exactly min(i + 1, h - i - 1) row symmetries
            if (len(row) == (min(rownum + 1, height - rownum - 1) - smudges) and
                rownum in smudge_candidates):
                total += rownum + 1
        return total

    
    def get_symmetries(grid, smudges):
        result = row_wise_symmetry(grid, smudges)
        if result: return 100 * result
        else: return row_wise_symmetry(np.transpose(grid), smudges)

    print(f"Part 1: {sum(map(lambda grid: get_symmetries(grid, smudges=0), input))}")
    print(f"Part 2: {sum(map(lambda grid: get_symmetries(grid, smudges=1), input))}")
    print(f"I like chaos: {sum(map(lambda grid: get_symmetries(grid, smudges=5), input))}")


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.read()

main()