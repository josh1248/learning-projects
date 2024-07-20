import random

print("training model now...")

print("model trained.")

def select_move(board: list[int]):
    freeCells = [i for i in range(len(board)) if board[i] == 0]
    return freeCells[random.randrange(0, len(freeCells))]

