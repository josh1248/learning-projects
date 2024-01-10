day_number = 19
import re
import math
def main():
    letter_to_axis = dict(zip("xmas", (0, 1, 2, 3)))
    input = read_file().split("\n\n")
    
    def str_to_workflow(s):
        name, tmp = s.split("{")
        decisions = tmp[:-1].split(",")
        return (name, decisions)
    workflows = dict(str_to_workflow(s) for s in input[0].split("\n"))

    p2_start = [(1, 4000)] * 4
    def get_accepted_parts(i_s, workflow_name, decision_index):
        if not all(i_s) or workflow_name == "R":
            return 0
        elif workflow_name == "A":
            return math.prod(i[1] - i[0] + 1 for i in i_s)
        decision = workflows[workflow_name][decision_index]
        colon_index = decision.find(":")
        if colon_index == -1: #last decision
            return get_accepted_parts(i_s, decision, 0)
        
        #non-terminal decision point
        inequality, redirect = decision.split(":")
        i_s_consequent, i_s_alternative = split_4d_interval(i_s, inequality)
        return (get_accepted_parts(i_s_consequent, redirect, 0) + 
                get_accepted_parts(i_s_alternative, workflow_name, decision_index + 1))

            
    def split_4d_interval(i_s, inequality):
        axis, sign, boundary = letter_to_axis[inequality[0]], inequality[1], int(inequality[2:])
        return list(map(lambda bound: [interval if index != axis else bound for index, interval in enumerate(i_s)],
                        split_individual_interval(i_s[axis], sign, boundary)))

    def split_individual_interval(i, sign, boundary):
        if sign == "<":
            if i[1] < boundary: return (i, None)
            elif i[0] >= boundary: return (None, i)
            else: return ((i[0], boundary - 1), (boundary, i[1]))
        elif sign == ">":
            if i[1] <= boundary: return (None, i)
            elif i[0] > boundary: return (i, None)
            else: return ((boundary + 1, i[1]), (i[0], boundary))
    
    print(f"Part 2: {get_accepted_parts(p2_start, 'in', 0):,}")

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.read()

main()