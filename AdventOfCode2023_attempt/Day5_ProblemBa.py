#text input is "DayX_Input.txt"
day_number = 5
from functools import reduce

def main():
    input = read_file()
    seed_nums = [int(i) for i in input[0].split()[1:]] #exclude header
    seed_ranges = []
    for i in range(0, len(seed_nums), 2):
        seed_ranges.append([seed_nums[i], seed_nums[i] + seed_nums[i + 1] - 1]) #denote start and end boundary of sequential seeds

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
        list_of_maps_sorted.append([list(map(int, i)) for i in sorted_category_map])

    def interval_intersection(i1, i2):
        result =  [max(i1[0], i2[0]), min(i1[1], i2[1])]
        return (result if result[0] <= result[1] else None)

    #get only the interval(s) in interval i1
    def interval_difference(i1, i2):
        i2 = interval_intersection(i1, i2)
        if i2 == None:
            return [i1]
        elif i2 == i1:
            return None
        else:
            result = [[i1[0], i2[0] - 1], [i2[1] + 1, i1[1]]]
            return [interval for interval in result if interval[0] <= interval[1]]

    #apply list of mappings to a single interval, get list of output intervals from mappings
    def apply_mapping(mappings, interval):
        output_intervals = []
        mapping_range = [mappings[0][1], mappings[0][1] + mappings[0][2] - 1]
        offset = mappings[0][0] - mappings[0][1]
        result = interval_intersection(interval, mapping_range)
        if result: #non-zero intersection
            output_intervals.append([i + offset for i in result])
            
        unmapped = interval_difference(interval, mapping_range)
        if unmapped == None:
            pass #nothing left to map
        elif len(unmapped) == 1:
            if len(mappings) > 1: #maps are sorted
                output_intervals += apply_mapping(mappings[1:], unmapped[0])
            else:
                output_intervals.append(unmapped[0])
        elif len(unmapped) == 2:
            #maps are sorted in increasing order, so interval smaller than current map will never be mapped again
            output_intervals.append(unmapped[0])
            if len(mappings) > 1:
                output_intervals += apply_mapping(mappings[1:], unmapped[1])
            else:
                output_intervals.append(unmapped[1])

        return output_intervals

    def apply_multiple_intervals(mappings, intervals):
        output_intervals = []
        for interval in intervals:
            output_intervals += apply_mapping(mappings, interval)
        
        return output_intervals
    
    source_range = seed_ranges
    for category in list_of_maps_sorted:
        source_range = apply_multiple_intervals(category, source_range)
    print(min([interval[0] for interval in source_range]))

    
def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()