#text input is "DayX_Input.txt"
day_number = 13
import numpy as np
def main():
    input = [np.array([list(line) for line in grid.split("\n")]) for grid in read_file().split("\n\n")]
        
    def get_vertical_symmetry(grid):
        height = grid.shape[0]
        '''each bucket i shows if mirror along row (i / 2) is still possible.
        since mirror can only lie between rows, not on top of rows, we only need to consider
        odd cases of i. We also only need to consider combinations of rows that reflect between
        rows only, i.e. their row numbers add up to an odd number'''
        valid_symmetries = set(range(1, 2 * height - 2, 2))
        for i, j in [(i, j) for i in range(height) for j in range(i + 1, height, 2)]:
            if not np.array_equal(grid[i], grid[j]):
                valid_symmetries.discard(i + j)

        if valid_symmetries: return (sum(valid_symmetries) + 1) / 2
        else: return None
    
    def get_symmetries(grid):
        result = get_vertical_symmetry(grid)
        if result: return 100 * result
        else: return get_vertical_symmetry(np.transpose(grid))

    print(sum(map(get_symmetries, input)))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.read()

main()