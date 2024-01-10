day_number = 22
X, Y, Z = 0, 1, 2 #axes
def check_interval_intersect(i1, i2): return i1[0] <= i2[0] <= i1[1] or i2[0] <= i1[0] <= i2[1]
class Brick:
    def __init__(self, line):
        self.start, self.end = [[int(i) for i in coord.split(",")] for coord in line.strip().split("~")]
        self.supporting, self.supported_by = set(), set()
    
    def __str__(self):
        return f"{self.start}, {self.end}, {self.supporting}, {self.supported_by}"
    
    def check_2d_collision(self, other): #check if current brick will hit another brick right below it
        return (check_interval_intersect((self.start[X], self.end[X]), (other.start[X], other.end[X])) and
                check_interval_intersect((self.start[Y], self.end[Y]), (other.start[Y], other.end[Y])))

    def make_brick_fall(self, fallen):
        while self.start[Z] > 1:
            if any(map(lambda b: self.check_2d_collision(b),
                        fallen[self.start[Z] - 1])):
                break
            else:
                self.start[Z] -= 1
                self.end[Z] -= 1
        
    def update_supports(self, fallen):
        self.supported_by = list(filter(lambda o: self.check_2d_collision(o),
                                        fallen[self.start[Z] - 1]))
        for b in self.supported_by:
            b.supporting.add(self)

    def safe_to_remove(self):
        return all(len(o.supported_by) >= 2 for o in self.supporting)
    
    def chain_reaction_falls(self):
        def helper(brick, removed_set):
            removed_set.add(brick)
            for b in brick.supporting:
                if set(b.supported_by).issubset(removed_set):
                    removed_set.union(helper(b, removed_set))
            return removed_set
        return len(helper(self, set())) - 1

        
def main():
    bricks = sorted([Brick(line) for line in read_file()], key=lambda b: b.start[Z])
    fallen_bricks = [[] for _ in range(bricks[-1].end[Z] + 1)] #store bricks by highest z-axis
    for b in bricks:
        b.make_brick_fall(fallen_bricks)
        fallen_bricks[b.end[Z]].append(b)
        b.update_supports(fallen_bricks)

    print("Part 1:", len([b for b in bricks if b.safe_to_remove()]))
    print("Part 2:", sum([b.chain_reaction_falls() for b in bricks]))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()