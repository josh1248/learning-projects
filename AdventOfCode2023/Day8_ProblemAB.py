#text input is "DayX_Input.txt"
day_number = 8
from math import lcm

def main():
    input = read_file()
    instruction_unit = input[0].strip()
    def instructions(): #infinite generator list of instructions
        while True:
            for instruction in instruction_unit:
                yield instruction
    graph = {line[0:3]: {"L": line[7:10], "R": line[12:15]} for line in input[2:]}

    def steps_from(start, flag):
        steps, vertex = 0, start
        for instruction in instructions():
            if flag(vertex): return steps
            steps += 1
            vertex = graph[vertex][instruction]

    print(str(steps_from("AAA", lambda v: v == "ZZZ")))
    start_vertices = [v for v in graph if v[-1] == "A"]
    #only works because of zero-offset cycles to reach z, which the input satisfies.
    #if offset is present, Chinese Remainder Theorem must be used instead.
    print(lcm(*map(lambda vertex: steps_from(vertex, lambda v: v[-1] == "Z"), start_vertices)))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()