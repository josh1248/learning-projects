#text input is "DayX_Input.txt"
day_number = 10
def main():
    maze = []
    for r, line in enumerate(read_file()):
        maze.append(list(line.strip()))
        start_check = line.find("S")
        if start_check != -1:
            start_coords = (r, start_check)

    width, height = len(maze[0]), len(maze)
    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    pipe_to_direction = {"|": [N, S], "-": [E, W], "L": [N, E], "J": [N, W],
                         "7": [S, W], "F": [E, S], ".": []} #in order of N,E,S,W for later checks
     
    def read(m, coords): return m[coords[0]][coords[1]]
    def write(m, coords, sym): m[coords[0]][coords[1]] = sym
    def get_next_direction(coords, incoming_direction):
        for d in pipe_to_direction[read(maze, coords)]:
            if d != incoming_direction:
                return d
    
    def flip_direction(d): return tuple(-i for i in d)
    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])

    visited = set()
    def steps_in_loop(coords, incoming_direction):
        steps = 1 #one step away from start point
        while True:
            visited.add(coords)
            if coords == start_coords:
                return steps
            else:
                steps += 1
                next_direction = get_next_direction(coords, incoming_direction)
                coords = update_coords(coords, next_direction)
                incoming_direction = flip_direction(next_direction)
        
    valid_directions = []
    traversed_main_loop = False
    for direction in [N, E, S, W]:
        try:
            next_symbol = read(maze, update_coords(start_coords, direction))
            if flip_direction(direction) in pipe_to_direction[next_symbol]:
                valid_directions.append(direction)
                if not traversed_main_loop:
                    loop_size = steps_in_loop(update_coords(start_coords, direction), flip_direction(direction))
                    print(f"Part 1: {loop_size // 2 + (loop_size % 2 > 0)}")
                    traversed_main_loop = True
        except IndexError:
            continue

    for symbol, directions in pipe_to_direction.items():
        if directions == valid_directions:
            write(maze, start_coords, symbol)

    #Point in polygon method, inspired by PiP implementation in https://github.com/yimqiy/AOC23/blob/main/aoc10.py
    ins = 0
    for r in range(height):
        intersections = 0
        directions = []
        for c in range(width):
            if (r, c) in visited:
                directions += [d for d in [N,S] if d in pipe_to_direction[read(maze, (r, c))]]
                if directions in [[N, S],[S, N]]: #winding number algorithm
                    intersections += 1
                    directions = []
                elif directions in [[N, N], [S, S]]:
                    directions = [] #does not wind both up and down
            elif intersections % 2 == 1:
                ins += 1
    print(f"Part 2: {ins}")


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()