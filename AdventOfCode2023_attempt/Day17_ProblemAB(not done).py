#text input is "DayX_Input.txt"
day_number = 17
import sys
from copy import deepcopy
sys.setrecursionlimit(9999999)
def main():
    maze = [[int(i) for i in line.strip()] for line in read_file()]
    width, height = len(maze[0]), len(maze)
    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])
    def clockwise(d): return (d[1], -d[0]) #multiply by -i in complex plane
    def counter_clockwise(d): return (-d[1], d[0]) #multiply by i in complex plane
    def get_next_directions(d, consecs): return [clockwise(d), counter_clockwise(d)] + [x for x in [d] if consecs <= 3]




    def simulate():
        def bfs(r, c, d, consecs, visited):
            print(visited)
            if r < 0 or c < 0 or r >= height or c >= width:
                return float('inf')
            elif r == height - 1 and c == width - 1:
                return maze[r][c]
            elif visited[r][c]:
                return float('inf')
            else:
                visited[r][c] = True
                shortest = maze[r][c] +  min(map(lambda dir: bfs(r + dir[0], c + dir[1], dir, 1 if dir != d else consecs + 1, visited),
                                                 get_next_directions(d, consecs)))
                #visited[r][c] = False
                return shortest
        return bfs(0, 0, E, 0, [[False] * width for i in range(height)])


    print(simulate())


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()