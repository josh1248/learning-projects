day_number = 23
import copy
def main():
    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    arrows = {"^": N, ">": E, "v": S, "<": W}
    maze = [[c for c in line.strip()] for line in read_file()]
    height, width = len(maze), len(maze[0])

    def maze_at(coord): return maze[coord[0]][coord[1]]

    def flip_direction(direction): return tuple(-i for i in direction)

    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])

    def get_next_moves(coord, visited):
        if (s := maze_at(coord)) in arrows:
            return [update_coords(coord, arrows[s])]
        
        def valid(c):
            return (0 <= c[0] < height and 0 <= c[1] < width and
                    c not in visited and
                    (sym := maze_at(c)) != "#" and
                    (sym not in arrows or update_coords(c, arrows[sym]) != coord))

        i, j = coord
        return [c for c in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)] if valid(c)]
    
    def dfs(coord, visited):
        steps = 0
        while coord != (height - 1, width - 2):
            #print(coord)
            visited.add(coord)
            steps += 1
            next_moves = get_next_moves(coord, visited)
            if len(next_moves) == 1:
                coord = next_moves[0]
            elif len(next_moves) == 0:
                return -99999
            else:
                return (steps + 
                       max(map(lambda c: dfs(c, copy.deepcopy(visited)), next_moves)))
        return steps

    
    print("Part 1:", dfs((0, 1), set()))

        

def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()