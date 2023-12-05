mapping = [(52, 50, 48), (50, 98, 2)]
start_ranges = [[0, 70], [80, 90]]
from functools import reduce

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
        if len(mappings) > 1 and mappings[0][1] > mapping_range[1]: #maps are sorted
            output_intervals += apply_mapping(mappings[1:], unmapped[1])
        else:
            output_intervals.append(unmapped[0])
    elif len(unmapped) == 2:
        #maps are sorted in increasing order, so interval smaller than current map will never be mapped again
        output_intervals.append(unmapped[0])
        if len(mappings) > 1 and mappings[1][1] > mapping_range[1]: #maps are sorted
            output_intervals += apply_mapping(mappings[1:], unmapped[1])
        else:
            output_intervals.append(unmapped[1])
    return output_intervals

def apply_multiple_intervals(mappings, intervals):
    output_intervals = []
    for interval in intervals:
        output_intervals += apply_mapping(mappings, interval)
    
    return output_intervals

print(apply_multiple_intervals(mapping, apply_multiple_intervals(mapping, start_ranges)))