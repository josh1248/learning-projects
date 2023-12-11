# Sample array
my_array = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Modify a subslice
start_index = 2
end_index = 5
new_values = [10, 11, 12]

# Assign the new values to the subslice
my_array[start_index:end_index] = my_array[0:3] + 1

# Print the modified array
print(my_array)