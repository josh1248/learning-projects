#text input is "DayX_Input.txt"
day_number = 1

from functools import reduce
def main():
    input = read_file()
    only_digits = map(lambda input_line: 
                            filter(lambda char: char >= "0" and char <= "9",
                                   input_line),
                      input)
    
    sum = 0
    for item in only_digits:
        arr = list(item)
        if len(arr) != 0:
            sum += int(arr[0]) * 10 + int(arr[-1])
    print(sum)
    

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()