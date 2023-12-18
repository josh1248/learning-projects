#text input is "DayX_Input.txt"
day_number = 18
import sys
def main():
    grid = [[x for x in l.strip().split()[-1]] for l in read_file()]
    unit_vector = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    pairings = {0: "R", 1: "D", 2: "L", 3: "U"}
    coordinates = [(0, 0)]
    boundary = 0
    for hexa in grid:
        print(hexa)
        direction = pairings[int(hexa[-2])]
        length = int(''.join(hexa[2:-2]), 16)
        boundary += int(length)
        displacement = (int(length) * u for u in unit_vector[direction])
        coordinates.append(tuple(a + b for a, b in zip(displacement, coordinates[-1])))

    #shoelace formula
    area = 0
    for i in range(len(coordinates) - 1):
        a, c = coordinates[i]
        b, d = coordinates[i + 1]
        area += a * d - b * c

    print(grid)
    print(coordinates)
    print("Interior: ", (abs(area) - boundary) / 2 + 1)
    print("Exterior: ", boundary)
    print("Total: ", (abs(area) + boundary) / 2 + 1)


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()