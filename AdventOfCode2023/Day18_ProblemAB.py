#text input is "DayX_Input.txt"
day_number = 18
import sys
def main():
    input = [[x for x in l.strip().split()] for l in read_file()]
    unit_vector = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    pairings = dict(zip("0123", "RDLU"))
    p1_instructions = [[l[0], int(l[1])] for l in input]
    p2_instructions = [[pairings[l[-1][-2]], int(l[-1][2:7], 16)] for l in input]


    def next_coordinate(coord, d, length):
        displacement = (length * i for i in unit_vector[d])
        return tuple(a + b for a, b in zip(coord, displacement))
    
    def determinant(p1, p2): return p1[0] * p2[1] - p1[1] * p2[0]

    def get_area(instructions):
        shoelace_area, boundary_area = 0, 0
        prev_coord = (0, 0)
        for direction, length in instructions:
            next_coord = next_coordinate(prev_coord, direction, length)
            shoelace_area += determinant(prev_coord, next_coord)
            boundary_area += length
            prev_coord = next_coord
        shoelace_area = abs(shoelace_area) / 2

        exterior_area = boundary_area
        interior_area = shoelace_area - (boundary_area / 2) + 1
        return int(interior_area + exterior_area)

    print(f"Part 1: {get_area(p1_instructions)}")
    print(f"Part 2: {get_area(p2_instructions)}")


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()