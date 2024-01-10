#text input is "DayX_Input.txt"
day_number = 1

digits = {'one': '1', 'two': '2', 'three': '3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
d_keys = digits.keys()
def main():
    input = read_file()
    only_digits = map(input_line_to_nums, input)

    sum = 0
    for item in only_digits:
        arr = list(item)
        if len(arr) != 0:
            sum += int(arr[0]) * 10 + int(arr[-1])
    print(sum)


def input_line_to_nums(string):
    length = len(string)
    output_array = []
    for start_i in range(length):
        #corresponds to a digit
        if string[start_i] >= "0" and string[start_i] <= "9":
            output_array.append(string[start_i])
            continue
        
        #check relevant substring if it spells out a digit
        for digit_spelling in d_keys:
            digit_len = len(digit_spelling)
            if (start_i + digit_len) > length:
                continue
            elif string[start_i: start_i + digit_len].lower() == digit_spelling:
                output_array.append(digits[digit_spelling])
            else:
                continue
    return output_array


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()