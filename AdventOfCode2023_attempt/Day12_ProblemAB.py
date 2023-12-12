#text input is "DayX_Input.txt"
day_number = 12
def main():
    input = [line.strip().split() for line in read_file()]
    input = list(map(lambda line: [line[0], tuple(int(i) for i in line[1].split(","))], input))

    memo = {}
    def get_possibilities(line, sequence):
        def helper(substr, substr_len, subseq, min_len):
            #base cases
            if min_len > substr_len:
                return 0
            elif substr and not subseq:
                return 0 if [c for c in substr if c == "#"] else 1
            elif not substr:
                return 1
            elif (substr, subseq) in memo:
                return memo[(substr, subseq)]
        
            total = 0
            #consider . at first position if viable
            if substr[0] != "#":
                total += helper(substr[1:], substr_len - 1, subseq, min_len)

            #consider sequence of # starting from first position
            #if not the last seq, sequence of # must be followed by a .
            if (substr[0:subseq[0]].count(".") == 0): 
                if len(subseq) == 1:
                    total += helper(substr[subseq[0]:], substr_len - subseq[0], [], -1)
                elif substr[subseq[0]] != "#":
                    total += helper(substr[subseq[0] + 1:],
                                    substr_len - subseq[0] - 1,
                                    subseq[1:],
                                    min_len - subseq[0] - 1) #i love Python OOB slicing
                    
            memo[(substr, subseq)] = total
            return total
        return helper(line, len(line), sequence, sum(sequence) + len(sequence) - 1)
    
    print(f"Part 1: {sum(map(lambda row: get_possibilities(row[0], row[1]), input)):,}")
    print(f"Part 2: {sum(map(lambda row: get_possibilities('?'.join([row[0]] * 5), row[1] * 5), input)):,}")
    print(f"Memo size: {len(memo):,} entries, {len(str(memo.items())):,} chars")


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()