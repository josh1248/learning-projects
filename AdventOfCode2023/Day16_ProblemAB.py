#text input is "DayX_Input.txt"
day_number = 16
def main():
    maze = [[char for char in line.strip()] for line in read_file()]
    width, height = len(maze[0]), len(maze)
    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    sym_to_direction = {"|": {N: [N], S: [S], E: [N, S], W: [N, S]}, 
                        "-": {E: [E], W: [W], N: [E, W], S: [E, W]},
                        "\\": {N: [W], E: [S], S: [E], W: [N]},
                        "/": {N: [E], E: [N], S: [W], W: [S]},
                        ".": {N: [N], E: [E], S: [S], W: [W]}}
    
    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])
    def get_next_direction(c, d): return sym_to_direction[maze[c[0]][c[1]]][d]

    def simulate(args):
        coords, direction = args
        visited = [[{N: False, E: False, S: False, W: False} for i in range(len(maze[0]))] for _ in range(len(maze))]
        stack = [(coords, direction)]
        while stack:
            c, dir = stack.pop()
            if c[0] < 0 or c[1] < 0 or c[0] >= height or c[1] >= width:
                continue
            elif visited[c[0]][c[1]][dir] == True:
                continue
            visited[c[0]][c[1]][dir] = True
            stack += list(map(lambda d: (update_coords(c, d), d),
                              get_next_direction(c, dir)))

        total = 0
        for line in visited:
            for coord in line:
                if any(coord.values()): 
                    total += 1
        return total

    to_simulate = []
    for r in range(height):
        to_simulate.append([(r, 0), E])
        to_simulate.append([(r, width - 1), W])
    for c in range(width):
        to_simulate.append([(0, c), S])
        to_simulate.append([(height - 1, c), N])
    results = list(map(simulate, to_simulate))
    print(f"Part 1: {results[0]}")
    print(f"Part 2: {max(results)}")



def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()