#text input is "DayX_Input.txt"
day_number = 5
from functools import reduce

def main():
    input = read_file()
    seed_ranges = [int(i) for i in input[0].split()[1:]] #exclude header
    seeds = []
    for i in range(0, len(seed_ranges), 2):
        seeds.append(range(seed_ranges[i], seed_ranges[i] + seed_ranges[i + 1]))

    category_boundaries = []
    for rownum in range(1, len(input)):
        if input[rownum].endswith(":\n"):
            category_boundaries.append(rownum)
    category_boundaries.append(len(input))
    
    list_of_maps_sorted = []
    for i in range(len(category_boundaries) - 1):
        category_map = input[category_boundaries[i] + 1:category_boundaries[i + 1] - 1]
        category_map_split = list(map(lambda mapping: mapping.split(), category_map))
        sorted_category_map = sorted(category_map_split, key = lambda indiv_map: indiv_map[1])
        list_of_maps_sorted.append(sorted_category_map)

    def get_range_of_locations(seed_range, mapping):
        def apply_map(mapping, start_num):
            for individual_map in mapping:
                dest_start, source_start, value_range = map(int, individual_map)
                if source_start <= start_num and start_num < source_start + value_range:
                    return start_num + dest_start - source_start
            return start_num #no mappings found
        
        return reduce(lambda source_num, mapping: apply_map(mapping, source_num), list_of_maps, seed)
    '''
    print("done!")
    mins = []
    for seed_range in seeds:
        mins.append(min(map(get_location, seed_range)))
        print("done!")
    print(min(mins))'''
def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()