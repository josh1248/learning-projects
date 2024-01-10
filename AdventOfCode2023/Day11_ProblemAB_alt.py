#text input is "DayX_Input.txt"
#memoized implementation.
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

    empty_rows_smaller_than, empty_cols_smaller_than = np.array([0] * len(image)), np.array([0] * len(image[0]))
    for num in empty_rows:
        if num < (len(image) - 1):
            empty_rows_smaller_than[num + 1:] += 1 #only works in numpy.

    for num in empty_cols:
        if num < (len(image[0]) - 1):
            empty_cols_smaller_than[num + 1:] += 1
    
    def empty_lines_between(b1, b2, arr):
        return abs(arr[b2] - arr[b1])
        
    def expanded_between(bound1, bound2): #returns number of empty rows and columns between 2 coordinates
        return (empty_lines_between(bound1[0], bound2[0], empty_rows_smaller_than) + 
                empty_lines_between(bound1[1], bound2[1], empty_cols_smaller_than))
    
    def empty_space_scaled_by(scale):
        distances = np.int64(0) #prevent int32 overflow since result is larger than 4 billion
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