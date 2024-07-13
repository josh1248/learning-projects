function naive_implementation(number) {
    //n log n implementation, palindrome check is a log n operation run n times
    let count = 0;
    for (let i = 1; i <= number; i = i + 1) {
        if (is_palindrome(i)) {
            count = count + 1;
        }
    }
    return count;
}

function fast_implementation(number) {
    //log n implementation.
    let digits_in_num = 0;
    let lead_digit = "something";
    for (let x = number; x > 0; x = math_floor(x / 10)) {
        digits_in_num = digits_in_num + 1;
        lead_digit = x;
    }

    //idea: we know the number of palindromes with n digits in total. so, we 
    //can precalculate palindromes with less digits than our current number.
    function palindromes_up_to_power(power) {
        //palindromes from 1 to 10^power - 1
        return power < 1 
               ? 0
               : 9 * math_pow(10, math_floor((power - 1) / 2))
                 + palindromes_up_to_power(power - 1);
    }
    let less_digit_palindromes = palindromes_up_to_power(digits_in_num - 1);

    //idea: generate palindromes by producing the number
    //left of the midline. For example, midline of 5225 will be between the 2's
    //and 919 will have midline right at the 1
    //Therefore, the number of palindromes with 5 digits of 527xx, for example,
    //will be the number of integers from 100 to 526. for 527, check xx and ensure
    //that 52725 <= 527xx, i.e. 7xx >= left to mid digits, reversed (725).
    const split_digits_len = math_ceil(digits_in_num / 2);
    let left_to_mid_digits = math_floor(number / math_pow(10, digits_in_num - split_digits_len));
    let mid_to_right_digits = number % math_pow(10, split_digits_len);
    
    let reversed_left_to_mid = num_reverse(left_to_mid_digits);
    
    let equal_digit_palindromes = left_to_mid_digits - 
                                  math_pow(10, split_digits_len - 1) +
                                  (mid_to_right_digits >= reversed_left_to_mid ? 1 : 0);
    return equal_digit_palindromes + less_digit_palindromes;
}

function num_reverse(number) {
    let reversed = "";
    while (number > 0) {
        reversed = reversed + stringify(number % 10);
        number = math_floor(number / 10);
    }
    return parse_int(reversed, 10);
}
fast_implementation(999);

function is_palindrome(number) {
    let stringified = stringify(number);
    let length = 0;
    for (let i = 0; char_at(stringified, i) !== undefined; i = i + 1) {
        length = length + 1;
    }
    
    let mid_index = (length - 1) / 2;
    for (let i = 0; i <= mid_index; i = i + 1) {
        if (char_at(stringified, i) !== char_at(stringified, length - i - 1)) {
            return false;
        }
    }
    return true;
}

function checker(num) {
    display("Palindromic numbers from 1 to " + stringify(num) + ": ");
    const start_time_f = get_time();
    const f_answer = fast_implementation(num);
    const end_time_f = get_time();
    display("Fast: " + stringify(f_answer) +
            " (Time: " + stringify(end_time_f - start_time_f) + "ms)");
    
    const start_time_n = get_time();
    const n_answer = naive_implementation(num);
    const end_time_n = get_time();
    display("Naive: " + stringify(n_answer) +
            " (Time: " + stringify(end_time_n - start_time_n) + "ms)");
    
}

function check_serial(lst) {
    if (is_null(lst)) {
        return "finished";
    } else {
        checker(head(lst));
        check_serial(tail(lst));
    }
}

check_serial(list(1, 10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000));