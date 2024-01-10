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

    visited = []
    def steps_in_loop(coords, incoming_direction):
        steps = 1 #one step away from start point
        while True:
            visited.append(coords)
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

    #shoelace method: https://en.wikipedia.org/wiki/Shoelace_formula
    def get_determinant(c1, c2):
        a, c = c1
        b, d = c2
        return a * d - b * c
    
    x = sum((get_determinant(visited[i], visited[i + 1]) for i in range(len(visited) - 1)))
    x += get_determinant(visited[-1], visited[0])
    print((abs(x) - len(visited)) / 2 + 1)



def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()