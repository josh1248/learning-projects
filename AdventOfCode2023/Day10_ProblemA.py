#text input is "DayX_Input.txt"
day_number = 10
def main():
    maze = []
    for r, line in enumerate(read_file()):
        maze.append(line.strip())
        start_check = line.find("S")
        if start_check != -1:
            start_coords = (r, start_check)

    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    pipe_to_direction = {"|": [N, S], "-": [E, W], "L": [N, E], "J": [N, W],
                         "7": [S, W], "F": [E, S], ".": []} #in order of N,E,S,W for later checks
     
    def symbol_at(m, coords): return m[coords[0]][coords[1]]
    def get_next_direction(coords, incoming_direction):
        for d in pipe_to_direction[symbol_at(maze, coords)]:
            if d != incoming_direction:
                return d
    
    def flip_direction(d): return tuple(-i for i in d)
    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])

    def steps_in_loop(coords, incoming_direction):
        steps = 1 #one step away from start point
        while coords != start_coords:
            steps += 1
            next_direction = get_next_direction(coords, incoming_direction)
            coords = update_coords(coords, next_direction)
            incoming_direction = flip_direction(next_direction)
        return steps
        
    for direction in [N, E, S, W]:
        try:
            next_symbol = symbol_at(maze, update_coords(start_coords, direction))
            if flip_direction(direction) in pipe_to_direction[next_symbol]:
                loop_size = steps_in_loop(update_coords(start_coords, direction), flip_direction(direction))
                print(loop_size // 2 + (loop_size % 2 > 0)) #round up fn
                break #only need 1 valid path to consider
        except IndexError:
            continue


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()