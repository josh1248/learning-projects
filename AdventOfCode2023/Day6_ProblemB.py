#text input is "DayX_Input.txt"
day_number = 6
from math import floor, ceil
def main():
    input = read_file()
    time = int(''.join(input[0].replace(" ","").split(":")[1]))
    distance = int(''.join(input[1].replace(" ","").split(":")[1]))

    print(ways_to_beat_record((time, distance)))
    
#O(1) formula for ways_to_beat_record
def solve_real_quadratic(a, b, c):
    return (-b + (b**2 - 4*a*c) ** 0.5) / (2*a), (-b - (b**2 - 4*a*c) ** 0.5) / (2*a)

def ways_to_beat_record(race):
    maxtime, record_distance = race
    #do math. fudge factor of +0.5 so that charge times that match record exactly dont count
    min_charge_time, max_charge_time = solve_real_quadratic(-1, maxtime, -record_distance - 0.5)
    return floor(max_charge_time) - ceil(min_charge_time) + 1

#O(n) first implementation that still practically works
'''
def ways_to_beat_record(race):
    maxtime = race[0]
    record_distance = race[1]
    totalways = 0
    for preptime in range(1, maxtime):
        distance = (maxtime - preptime) * (preptime * 1)
        if distance > record_distance:
            totalways += 1
    return totalways
'''

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()