#text input is "DayX_Input.txt"
day_number = 15
def main():
    input = read_file()[0].strip().split(",")
    def get_hash(s):
        val = 0
        for char in s:
            val = (val + ord(char)) * 17 % 256
        return val
    print(f"Part 1: {sum(map(get_hash, input))}")

    boxes = [[] for _ in range(256)]
    def apply_lens(s):
        if "=" not in s:
            hash_value = get_hash(s[:-1])
            boxes[hash_value] = [x for x in boxes[hash_value] if x[0] != s[:-1]]
        else:
            lens, focus = s.split("=")
            hash_value = get_hash(lens)
            for i in boxes[hash_value]:
                if i[0] == lens:
                    i[1] = focus
                    break
            else:
                #only runs if not broken previously
                boxes[hash_value].append([lens, focus])

    for s in input:
        apply_lens(s)

    total = 0
    for box_num, box in enumerate(boxes, 1):
        for slot_num, slot in enumerate(box, 1):
            total += box_num * slot_num * int(slot[1])

    print(f"Part 2: {total}")


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()