#text input is "DayX_Input.txt"
day_number = 14
def main():
    input = [line.strip().split() for line in read_file()]


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()