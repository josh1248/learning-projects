#text input is "DayX_Input.txt"
day_number = 9
def main():
    input = read_file()
    sequences = [[int(i) for i in line.split()] for line in input]
    def extrapolate(seq):
        diffs = [seq[i + 1] - seq[i] for i in range(len(seq) - 1)]
        return seq[-1] + (extrapolate(diffs) if any(diffs) else 0)    
    
    print(sum(map(extrapolate, sequences)))
    print(sum(map(extrapolate, [seq[::-1] for seq in sequences])))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()