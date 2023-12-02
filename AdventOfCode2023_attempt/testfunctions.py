digits = {'one': '1', 'two': '2', 'three': '3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
d_keys = list(digits.keys())

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
            #out of bounds check
            if (start_i + digit_len) > length:
                continue
            elif string[start_i: start_i + digit_len].lower() == digit_spelling:
                output_array.append(digits[digit_spelling])
            else:
                continue
    return output_array

print(d_keys)
print(input_line_to_nums("fiveight2oneneqew"))