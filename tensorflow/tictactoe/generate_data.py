from .minimax_agent import minimax_agent

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
    return states

def generateTrainingData() -> tuple[list, list]:
    inputs = []
    outputs = []
    for state in getAllStates():
        terminal, value, play = minimax_agent(state)
        if not terminal:
            inputs.append(state)
            outputs.append(play)
    
    return inputs, outputs