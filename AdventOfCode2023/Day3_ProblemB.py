#text input is "DayX_Input.txt"
day_number = 3
import re

def main():
    input = read_file()
    input_rows = len(input)

    #gear "*" is allowed if adjacent, incl. diagonals, to exactly 2 numbers
    allowed_gears_sum = 0

    rows_of_numbers = []
    #first, generate number coordinates of
    #numbers[i] represents all numbers in row i of input
    #each number is represented with a dict which contains the number (as a string),
    #and start and end of column coordinates
    for line in input:
        matches = re.finditer(r'[0-9]+', line)
        rows_of_numbers.append([{"num_string": num.group(), 
                                 "start_col" : num.span()[0],
                                 "end_col": num.span()[1] - 1} for num in matches])

    for row_index, line in enumerate(input):
        #get allowed "*"" in the form of "item", a match object:
        #.span() of match object returns column coordinates (start_col, end_col + 1)
        #.group() of match object returns the matching string of the item
        for item in re.finditer(r'[*]', line):
            allowed_gears_sum += get_gear_ratio(item, row_index, input_rows, rows_of_numbers)
    
    print(allowed_gears_sum)

def get_gear_ratio(item, row_index, input_rows, numbers):
    col_index = item.span()[0]
    surrounding_numbers = []
    #check if range of numbers touches another range of numbers
    #iterate over row on top, row on same line as "*", and row below to find surrounding numbers respectively
    for row_offset in [-1, 0, 1]:
        if row_index + row_offset < 0 or row_index + row_offset >= input_rows:
            continue

        for number_dict in numbers[row_index + row_offset]:
            if number_dict["start_col"] > col_index + 1 or number_dict["end_col"] < col_index - 1:
                continue
            else:
                surrounding_numbers.append(int(number_dict["num_string"]))

    if len(surrounding_numbers) != 2:
        return 0
    else:
        return surrounding_numbers[0] * surrounding_numbers[1]


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()
#text input is "DayX_Input.txt"
day_number = 3
import re

def main():
    input = read_file()
    input_rows = len(input)

    #gear "*" is allowed if adjacent, incl. diagonals, to exactly 2 numbers
    allowed_gears_sum = 0

    rows_of_numbers = []
    for line in input:
        matches = re.finditer(r'[0-9]+', line)
        rows_of_numbers.append([{"num_string": num.group(), 
                                 "start_col" : num.span()[0],
                                 "end_col": num.span()[1] - 1} for num in matches])

    for row_index, line in enumerate(input):
        for item in re.finditer(r'[*]', line):
            allowed_gears_sum += get_gear_ratio(item, row_index, input_rows, rows_of_numbers)
    
    print(allowed_gears_sum)

def get_gear_ratio(item, row_index, input_rows, numbers):
    col_index = item.span()[0]
    surrounding_numbers = []
    #check if range of numbers touches another range of numbers
    #iterate over row on top, row on same line as "*", and row below to find surrounding numbers respectively
    for row_offset in [-1, 0, 1]:
        if row_index + row_offset < 0 or row_index + row_offset >= input_rows:
            continue

        for number_dict in numbers[row_index + row_offset]:
            if number_dict["start_col"] > col_index + 1 or number_dict["end_col"] < col_index - 1:
                continue
            else:
                surrounding_numbers.append(int(number_dict["num_string"]))

    if len(surrounding_numbers) != 2:
        return 0
    else:
        return surrounding_numbers[0] * surrounding_numbers[1]


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()