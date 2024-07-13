#modified version that allows both humans and machines
#to understand actions to do.
#pole A = position 0, pole B = position 1, pole C = position 2

human_mode, machine_mode = 0, 1
#main wrapper function that kicks off the process, plus data validation
def hanoi(height, mode):
    if height < 1 or (mode != human_mode and mode != machine_mode):
        print("invalid")
    else:
        steps_list = hanoi_lst(height, 0, 2)
        if mode == human_mode:
            humanise(steps_list)
        else:
            mechanise(steps_list)


#returns the pole position that is not the position of the input positions
#assumes input positions are distinct integers that can be 0, 1, or 2
def other(a, b):
    return [i for i in range(3) if i != a and i != b][0]

'''returns list of triplets that describe movement of circles.
triplet contains:
start pole. which pole number to take the disc from.
end pole.  where to drop a taken disc.
size:   size of disc taken.
Assume that in a tower of n, discs have size 1 to n.
'''
def hanoi_lst(stacks, start, end):
    base = {"start": start, "end": end, "size": stacks}
    if stacks == 0:
        return []
    else:
        return  hanoi_lst(stacks - 1, start, other(start, end)) + \
                [base] + \
                hanoi_lst(stacks - 1, other(start, end), end)

#index position to pole letter converter    
pole_name = ["A", "B", "C"]



#prints list of triplets in human-readable fashion
def humanise(steps_list):
    def namify(triplet):
        return [pole_name[triplet["start"]], \
                pole_name[triplet["end"]], \
                triplet["size"]]
    namified_steps = map(namify, steps_list)

    for index, step in enumerate(namified_steps,start=1):
        [start, end, size] = step
        print(f"Step {index}: {start} -> {end} (size {size})")

#converts to instructions: PICK (size), DROP (size), LEFT, RIGHT
def mechanise(steps_list):
    #returns instructions for a step, with or without disc.
    def move(step, moveDisc):
        difference = step["start"] - step["end"]
        if difference < 0:
            movement = ["RIGHT"] * (0 - difference)
        else:
            movement = ["LEFT"] * difference

        if moveDisc == True:
            size = step["size"]
            return [f"PICK {size}"] + movement + [f"DROP {size}"]
        else:
            return movement


    #adjusts arm from position of previous step to next step
    def inter_step(step1, step2):
        fake_step = {"start": step1["end"], "end": step2["start"]}
        return fake_step
    
    instructions = []
    prev_step = []
    for step in steps_list:
        if prev_step != []:
            instructions += move(inter_step(prev_step, step), moveDisc=False)
    
        instructions += move(step, moveDisc=True)
        prev_step = step
    
    print(instructions)

   
print("Humanised form:")
hanoi(4, human_mode)
print("Mechanised form:")
hanoi(4, machine_mode)