#Assume: text input is "DayX_problemX_Input.txt"
day_number = 1
problem_set = "A"

def main():
    input = read_file()

def read_file():
    relative_directory = "personal-projects/AdventOfCode2023_attempt"
    file_lines = []
    with open(f"{relative_directory}/Day{day_number}_Problem{problem_set}_Input.txt", "r") as file:
        for line in file:
            #exclude new line character at the back
            file_lines.append(line[:-2])
    return file_lines

main()