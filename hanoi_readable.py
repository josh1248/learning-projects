#modified version to allow human readability
#pole A = position 0, pole B = position 1, pole C = position 2

#returns the pole position that is not the position of the input positions
#assumes input positions are distinct integers that can be 0, 1, or 2
def other(a, b):
    poles = [0, 1, 2]
    poles.remove(a)
    poles.remove(b)
    return poles[0]

'''returns list of triplets that describe movement of circles.
triplet contains, in this order:
start pole. which pole number to take the disc from.
end pole.  where to drop a taken disc.
size:   size of disc taken.
Assume that in a tower of n, discs have size 1 to n.
'''
def hanoi(stacks, start, end):
    base = (start, end, stacks)
    if stacks == 0:
        return []
    else:
        return  hanoi(stacks - 1, start, other(start, end)) + \
                [base] + \
                hanoi(stacks - 1, other(start, end), end)

#index position to pole letter converter    
pole_name = ["A", "B", "C"]
def namify(triplet):
    return [pole_name[triplet[0]], pole_name[triplet[1]],triplet[2]]

#prints list of triplets in human-readable fashion
def readable(steps_list):
    namified_steps = map(namify, steps_list)
    for index, step in enumerate(namified_steps,start=1):
        [start, end, size] = step
        print(f"Step {index}: {start} -> {end} (size {size})")

readable(hanoi(4,0,2))