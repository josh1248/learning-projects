day_number = 21
import collections
def main():
    grid = [[c for c in line.strip()] for line in read_file()]
    height, width = len(grid), len(grid[0])
    start = [(r, c) for r in range(height) for c in range(width) if grid[r][c] == "S"][0]
    start_coord_parity = sum(start) % 2
    def even_steps_flag(coordinate): return sum(coordinate) % 2 == start_coord_parity #54 is even

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])
    def bfs():
        queue = collections.deque([(64, start)]) #O(1) pop left
        visited = set()
        while queue:
            steps_left, c = queue.popleft()
            if (not (0 <= c[0] < height and 0 <= c[1] < width and steps_left >= 0) or
                c in visited or 
                grid[c[0]][c[1]] == "#"):
                continue
            else:
                visited.add(c)
                queue.extend([(steps_left - 1, coord) for coord in list(map(lambda d: update_coords(c, d), directions))])
        return len(list(filter(even_steps_flag, visited)))

    print(bfs())


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()