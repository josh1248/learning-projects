import random

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

def generateTrainingData(training_data_proportion: float) -> tuple[list, list, list, list]:
    states = getAllStates()
    chosen = set(random.sample([i for i in range(len(states))], round(len(states) * training_data_proportion)))
    
    train_inputs = []
    train_outputs = []
    test_inputs = []
    test_outputs = []
    for i in range(len(states)):
        terminal, _, play, _ = minimax_agent(states[i])
        if i in chosen:
            if not terminal:
                train_inputs.append(states[i])
                train_outputs.append(play)
        else:
            if not terminal:
                test_inputs.append(states[i])
                test_outputs.append(play)
    
    return train_inputs, train_outputs, test_inputs, test_outputs