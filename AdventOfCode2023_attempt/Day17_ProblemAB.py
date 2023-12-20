#text input is "DayX_Input.txt"
day_number = 17
import heapq
def main():
    maze = [[int(i) for i in line.strip()] for line in read_file()]
    width, height = len(maze[0]), len(maze)
    N, E, S, W = (-1, 0), (0, 1), (1, 0), (0, -1)
    def update_coords(c, d): return (c[0] + d[0], c[1] + d[1])
    def clockwise(d): return (d[1], -d[0]) #multiply by -i in complex plane
    def counter_clockwise(d): return (-d[1], d[0]) #multiply by i in complex plane

    #a state is a 4-tuple: (weight to reach coordinate, coordinate, direction, consecutives in that direction)
    #probably more maintainable as a class, but wtv
    def get_next_states(state, min_consecs, max_consecs):
        def flag(s):
            w, c, d, consecs = s
            return 0 <= c[0] < height and 0 <= c[1] < width and consecs <= max_consecs

        w, c, d, consecs = state
        turn_left = (w, update_coords(c, c_clockwise_dir := counter_clockwise(d)), c_clockwise_dir, 1)
        straight = (w, update_coords(c, d), d, consecs + 1)
        turn_right = (w, update_coords(c, clockwise_dir := clockwise(d)), clockwise_dir, 1)
        if consecs >= min_consecs: #allow turning
            return list(map(update_weight, filter(flag, [turn_left, straight, turn_right])))
        else:
            return [update_weight(straight)] if flag(straight) else []

    def update_weight(s):
        return (s[0] + maze[s[1][0]][s[1][1]],) + s[1:]

    def dijkstra(min_consecs, max_consecs):
        distances = dict()
        priority_queue = get_next_states((0, (0, 0), E, 0), min_consecs, max_consecs)
        heapq.heapify(priority_queue)
        while priority_queue:
            current_state = heapq.heappop(priority_queue)
            weight, key = current_state[0], current_state[1:]
            if (key not in distances or weight < distances[key]):
                distances[key] = weight
                for next_state in get_next_states(current_state, min_consecs, max_consecs):
                    heapq.heappush(priority_queue, next_state)

        return min(v for k, v in distances.items() if k[0] == (height - 1, width - 1))

    print("Part 1:", dijkstra(0, 3))
    print("Part 2:", dijkstra(4, 10))
    '''
    Time taken with 'Measure-Command (time for Mac/Linux) {python AdventOfCode2023_attempt\Day17_ProblemAB.py}': 1s for A, 3s for B
    Possible optimisation: integrate get_next_state function within dijkstra, which would cut down duplicate calculations
    at the cost of some readability'''


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()