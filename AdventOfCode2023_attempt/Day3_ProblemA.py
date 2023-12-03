#text input is "DayX_Input.txt"
day_number = 3
import re

def main():
    input = read_file()
    input_rows = len(input)
    #minus one here to exclude new line character at the end
    input_cols = len(input[0]) - 1

    #number is allowed if adjacent, incl. diagonals, to symbols excluding "."
    allowed_numbers_sum = 0

    for row_index, line in enumerate(input):
        #get allowed numbers in the form of "item", a match object:
        #.span() of match object returns column coordinates (start_col, end_col + 1)
        #.group() of match object returns the matching string of the item
        for item in re.finditer(r'[0-9]+', line):
            if is_allowed_number(item, row_index, input, input_rows, input_cols):
                allowed_numbers_sum += int(item.group())
    
    print(allowed_numbers_sum)

def is_allowed_number(item, row_index, input, input_rows, input_cols):
    (start_col, end_col_plus_one) = item.span()
    surrounding_chars = ""
    #get left, right, top, and bottom surrounding characters repsectively
    if start_col > 0:
        surrounding_chars += input[row_index][start_col - 1]
    if end_col_plus_one < input_cols:
        surrounding_chars += input[row_index][end_col_plus_one]
    if row_index > 0:
        surrounding_chars += input[row_index - 1][max(0, start_col -1):min(input_cols, end_col_plus_one + 1)]
    if row_index < input_rows - 1:
        surrounding_chars += input[row_index + 1][max(0, start_col -1):min(input_cols, end_col_plus_one + 1)]
    #Python magic: empty lists are False, non-empty lists are True
    return bool(re.search(r'[^A-Za-z0-9.]', surrounding_chars))

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()