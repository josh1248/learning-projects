day_number = 21
import collections
import math
import numpy as np
def main():
    grid = [[c for c in line.strip()] for line in read_file()]
    height, width = len(grid), len(grid[0])
    start = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == "S"][0]
    start_coord_parity = sum(start) % 2
    def even_steps_flag(x):
        slice_coord, c = x
        return (slice_coord[0] * (height % 2) + slice_coord[1] * (width % 2) + sum(c)) % 2 == start_coord_parity

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])
    def update_slice(s, c): 
        new_slice = (s[0] + math.floor(c[0] / height), (s[1] + math.floor(c[1] / width)))
        new_coord = (c[0] % height, c[1] % width)
        return new_slice, new_coord
    
    def bfs(i):
        queue = collections.deque([((0, 0), i, start)])
        visited = set()
        while queue:
            slice_coords, steps_left, c = queue.popleft()
            if steps_left < 0:
                continue
            slice_coords, c = update_slice(slice_coords, c)

            if (slice_coords, c) in visited or grid[c[0]][c[1]] == "#":
                continue
            else:
                visited.add((slice_coords, c))
                queue.extend([(slice_coords, steps_left - 1, coord) for coord in list(map(lambda d: update_coords(c, d), directions))])
        flag = lambda x: even_steps_flag(x) if i % 2 == 0 else not even_steps_flag(x)
        return len(list(filter(flag, visited)))


    def get_quadratic(x1, y1, x2, y2, x3, y3):
        A = np.vander([x1, x2, x3], 3)
        B = np.array([y1, y2, y3])

        a, b, c = np.linalg.solve(A, B)

        return lambda x: round(a * (x ** 2) + b * x + c)
    #26501365 = 202300 * 131 + 65
    print("Part 1:", bfs(64))
    print("Part 2:", get_quadratic(p1 := 65, bfs(p1), p2 := p1 + 131, bfs(p2), p3 := p2 + 131, bfs(p3))(26501365))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()