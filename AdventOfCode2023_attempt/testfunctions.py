def make_inf(string):
    while True:
        for char in string:
            yield char

# Example usage
inf_gen = make_inf("abcx")

# Loop to print the generated string
for _ in range(60):  # Print the first 20 characters for demonstration
    print(next(inf_gen), end='')