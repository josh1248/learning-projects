#pole A = position 0, pole B = position 1, pole C = position 2en

#returns the pole position that is not the position of the input positions
#assumes input positions are distinct integers that can be 0, 1, or 2
def other(a, b):
    poles = list(range(3))
    poles.remove(a)
    poles.remove(b)
    return poles[0]
    


#returns list of ordered pairs that describe movement of circles
def hanoi(stacks, start, end):
    if stacks == 1:
        return [(start, end)]
    else:
        return hanoi(stacks - 1, start, other(start, end)) + \
               [(start, end)] + \
               hanoi(stacks - 1, other(start, end), end) 
    
print(hanoi(4,0,2))