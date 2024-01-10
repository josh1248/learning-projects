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
    def traverse_loop(coords, incoming_direction):
        while True:
            visited.add(coords)
            if coords == start_coords:
                break
            else:
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
                    traverse_loop(update_coords(start_coords, direction), flip_direction(direction))
                    traversed_main_loop = True
        except IndexError:
            continue

    for key, value in pipe_to_direction.items():
        if value == valid_directions:
            write(maze, start_coords, key)

    #"E" denotes non-loop tiles in the original maze, "X" denotes non-loop, non-original tiles
    new_maze = [[0] * 2 * width for _ in range(2 * height)]
    for r, line in enumerate(maze):
        for c, char in enumerate(line):
            expanded = [["E", "X"], ["X", "X"]]
            if (r, c) in visited:
                expanded[0][0] = "B" #B denotes main loop boundaries
                if S in pipe_to_direction[char]:
                    expanded[1][0] = "B"
                if E in pipe_to_direction[char]:
                    expanded[0][1] = "B"
            new_maze[2 * r][2 * c: 2 * c + 2] = expanded[0]
            new_maze[2 * r + 1][2 * c: 2 * c + 2] = expanded[1]

    def flood_fill(coords):
        stack = [coords]
        contiguous_block = set()
        boundary_flag = False
        while stack:
            current = stack.pop()
            if read(new_maze, current) == "B":
                continue
            elif current[0] in [0, 2 * height - 1] or current[1] in [0, 2 * width - 1]:
                boundary_flag = True

            contiguous_block.add(current)
            for direction in [N,E,S,W]:
                new_coords = update_coords(current, direction)
                if ((new_coords not in contiguous_block) and 
                  (0 <= new_coords[0] <= 2 * height - 1) and
                  (0 <= new_coords[1] <= 2 * width - 1)):
                    stack.append(new_coords) 
        
        if boundary_flag:
            for coords in contiguous_block:
                write(new_maze, coords, "O")
            return 0
        else:
            E_count = 0
            for coords in contiguous_block:
                if read(new_maze, coords) == "E":
                    E_count += 1
                write(new_maze, coords, "I")
            return E_count

    total = 0
    for r in range(2 * height - 1):
        for c in range(2 * width - 1):
            if new_maze[r][c] in ["E", "X"]:
                total += flood_fill((r, c))
    print(total)
    


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()