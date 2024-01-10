#text input is "DayX_Input.txt"
day_number = 2
import re

color_requirements = {"red" : 12, "green": 13, "blue": 14}
colors = color_requirements.keys()
def main():
    input = read_file()

    power_sums = 0
    for line in input:
        power = 1
        for color in colors:
            color_draws = re.findall(fr'([0-9]+) {color}', line)
            color_draws_int = map(int, color_draws)
            power *= max(color_draws_int)

        power_sums += power
    
    print(power_sums)


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()