day_number = 22
X, Y, Z = 0, 1, 2 #axes
class Brick:
    def __init__(self, line):
        self.start, self.end = [[int(i) for i in coord.split(",")] for coord in line.strip().split("~")]
        #bricks have >1 length ("parallel") along a single axis only (or none). 
        self.axis = a[0] if (a := [axis for axis in [X, Y, Z] if self.start[axis] < self.end[axis]]) else Z
        self.supporting, self.supported_by = [], []
        self.can_remove = None
    
    def __str__(self):
        return f"{self.start}, {self.end}, {self.axis}, {self.supporting}, {self.supported_by}, {self.can_remove}"
    
    def check_2d_collision(self, other): #check if current brick will hit another brick right below it
        '''check by examining collision across x and y axis.
        if self.axis == x, for example, it would have [start, end] coordinates. 
        if the start x-coordinate of the other brick does not lie within the [start, end] interval, collision is impossible,
        Similar logic applies for the y axis, and if other.axis is x or y instead.
        for cases where both bricks are not parallel to e.g. the x axis, checking equality of the x axis start point will do.
        repeat if both bricks are not parallel to the z axis'''
        axes_to_check = {X, Y}
        if (s := self.axis) != Z:
            result1 = (self.start[s] <= other.start[s] <= self.end[s])
            axes_to_check.discard(s)
            if not result1: return False

        if (o := other.axis) != Z:
            result2 = (other.start[o] <= self.start[o] <= other.end[o])
            axes_to_check.discard(o)
            if not result2: return False

        return all(self.start[remaining_axis] == other.start[remaining_axis] for remaining_axis in axes_to_check)

    def make_brick_fall(self, fallen):
        if self.start[Z] <= 1:
            return False #brick can no longer fall
        elif any(map(lambda b: self.check_2d_collision(b),
                     fallen[self.start[Z] - 1])):
            return False
        else:
            self.start[Z] -= 1
            self.end[Z] -= 1
            return True
        
    def update_supports(self, fallen):
        self.supported_by = list(filter(lambda o: self.check_2d_collision(o),
                                        fallen[self.start[Z] - 1]))
        for b in self.supported_by:
            b.supporting.append(self)

    def safe_to_remove(self, fallen):
        if len(self.supporting) == 0: return True
        x = all(map(lambda o: len(o.supported_by) >= 1, self.supporting))
        return x
        
def main():
    bricks = sorted(list(Brick(line) for line in read_file()), key=lambda b: b.start[Z])
    fallen_bricks = [[] for _ in range(bricks[-1].end[Z] + 1)] #store bricks by highest z-axis
    for b in bricks:
        while b.make_brick_fall(fallen_bricks): pass
        fallen_bricks[b.end[Z]].append(b)
        b.update_supports(fallen_bricks)

    for b in bricks:
        b.safe_to_remove(fallen_bricks)
    print(len(list(filter(lambda b: b.safe_to_remove(fallen_bricks), bricks))))


def read_file():
    relative_directory = "AdventOfCode2023_attempt"
    full_directory = f"{relative_directory}/Day{day_number}_Input.txt"
    with open(full_directory, "r") as file:
        return file.readlines()

main()