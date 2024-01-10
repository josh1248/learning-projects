#text input is "DayX_Input.txt"
import numpy as np
day_number = 11
def main():
    image = np.array([[char for char in line.strip()] for line in read_file() ])
    empty_rows, empty_cols, galaxies = [], [], []
    for r_index, row in enumerate(image):
        galaxy_matches = list((r_index, pos) for pos, char in enumerate(row) if char == "#")
        if galaxy_matches:
            galaxies += galaxy_matches
        else:
            empty_rows.append(r_index) 

    for c_index in range(len(image[0])):
        if sum(image[:, c_index] == "#") == 0:
            empty_cols.append(c_index)

    def expanded_between(bound1, bound2): #returns number of empty rows and columns between 2 coordinates
        row_bounds = (bound1[0], bound2[0]) #already in order
        col_bounds = (bound1[1], bound2[1]) if bound1[1] < bound2[1] else (bound2[1], bound1[1])
        return (len([r for r in empty_rows if row_bounds[0] < r < row_bounds[1]]) + 
                len([c for c in empty_cols if col_bounds[0] < c < col_bounds[1]]))
    
    def empty_space_scaled_by(scale):
        distances = 0
        #pairwise combination
        for i in range(len(galaxies)):
            for j in range(i, len(galaxies)):
                start, end = galaxies[i], galaxies[j]
                distances += (abs(start[0] - end[0]) + abs(start[1] - end[1]) + 
                              (scale - 1) * expanded_between(start, end))
        return distances
    print(f"Part 1: {empty_space_scaled_by(2)}")
    print(f"Part 2: {empty_space_scaled_by(1000000)}")


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()