day_number = 19
import re
def main():
    input = read_file().split("\n\n")
    def str_to_part(s):
        return dict(zip("xmas", [int(i) for i in re.findall(r'\d+', s)]))
    parts = [str_to_part(s) for s in input[1].split("\n")]

    def str_to_workflow(s):
        dict_start = s.find("{")
        workflow_name = s[:dict_start]
        workflows = s[dict_start + 1:-1].split(",")
        def workflow(part):
            for str_rep in workflows[:-1]:
                inequality, redirect = str_rep.split(":")
                if eval(inequality, {inequality[0]: part[inequality[0]]}):
                    return redirect
            return workflows[-1]
        return (workflow_name, workflow)
    workflows = dict(str_to_workflow(s) for s in input[0].split("\n"))

    total = 0
    for part in parts:
        result = "in"
        while True:
            result = workflows[result](part)
            if result == "A":
                total += sum(part.values())
                break
            elif result == "R":
                break
    
    print(f"Part 1: {total:,}")


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.read()

main()