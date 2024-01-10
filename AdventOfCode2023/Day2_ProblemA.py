#text input is "DayX_Input.txt"
day_number = 2
import re

color_requirements = {"red" : 12, "green": 13, "blue": 14}
colors = color_requirements.keys()
def main():
    input = read_file()

    ID_sums = 0
    for line in input:
        possible_draw = True
        for color in colors:
            color_draws = re.findall(fr'([0-9]+) {color}', line)
            color_draws_int = map(int, color_draws)
            if max(color_draws_int) > color_requirements[color]:
                #impossible draw
                possible_draw = False
                break
        
        if possible_draw:
            ID = re.findall(r'Game ([0-9]+):', line)
            ID_sums += int(ID[0])
    
    print(ID_sums)


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()