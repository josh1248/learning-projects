def getAllStates():
    states = []
    def helper(curr: list[int], remaining):
        if remaining == 0:
            states.append(curr[:])
            return
        
        for i in [-1, 0, 1]:
            curr.append(i)
            helper(curr, remaining - 1)
            curr.pop()

        

    helper([], 9)
    print(states)

getAllStates()