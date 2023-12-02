#Assume: text input is "DayX_problemX_Input.txt"
day_number = 2
problem_set = "A"

from functools import reduce
def main():
    input = read_file()
    no_digits = map(lambda input_line: 
                            filter(lambda char: char >= "0" and char <= "9",
                                   input_line),
                    input)
    sum = 0
    for item in no_digits:
        arr = list(item)
        if len(arr) != 0:
            sum += int(arr[0]) * 10 + int(arr[-1])
    print(sum)
    print("".join(list(no_digits)))

    
    

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    file_lines = []
    #looped instead of fully read with .readlines() to remove new line character at the back
    with open(f"{relative_directory}/Day{day_number}_Problem{problem_set}_Input.txt", "r") as file:
        for line in file:
            file_lines.append(line[:-1])
    return file_lines


main()