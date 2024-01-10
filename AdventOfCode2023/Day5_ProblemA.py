#text input is "DayX_Input.txt"
day_number = 5
from functools import reduce

def main():
    input = read_file()
    seeds = [int(i) for i in input[0].split()[1:]] #exclude header
    
    category_boundaries = []
    for rownum in range(1, len(input)):
        if input[rownum].endswith(":\n"):
            category_boundaries.append(rownum)
    category_boundaries.append(len(input))
    
    list_of_maps = []
    for i in range(len(category_boundaries) - 1):
        category_map = input[category_boundaries[i] + 1:category_boundaries[i + 1] - 1]
        list_of_maps.append(list(map(lambda mapping: mapping.split(), category_map)))

    def get_location(seed):
        def apply_map(mapping, start_num):
            for individual_map in mapping:
                dest_start, source_start, value_range = map(int, individual_map)
                if source_start <= start_num and start_num < source_start + value_range:
                    return start_num + dest_start - source_start
            return start_num #no mappings found
        
        return reduce(lambda source_num, mapping: apply_map(mapping, source_num), list_of_maps, seed)
    
    print(min(map(get_location, seeds)))

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()