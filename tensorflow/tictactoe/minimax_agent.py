# one-time use to generate seed data
import random

victory_cons = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6],
]

def board_value(board_state: list[int]) -> tuple[bool, int]:
    '''
        Based on the board state, returns 2 items:
        - First item is a boolean, denoting if the board state is "terminal" - no more moves to be played.
        - Second item returns 1 if the board state is a victory for the first player, -1 if victory for the second player, 0 otherwise.
        
        Second item value should be ignored if the first value reads False.
    '''
    
    for (a, b, c) in victory_cons:
        if board_state[a] == board_state[b] == board_state[c] and board_state[a] != 0:
            return (True, board_state[a])

    return(sum([1 if square != 0 else 0 for square in board_state]) == 9, 0)
        
def minimax_agent(board_state) -> tuple[bool, int, int]:
    '''
        Based on the board state, returns 2 items:
        - First item is a boolean, denoting if the board state is "terminal" - no more moves to be played.
        - Second item returns the value of the board state.
            - 1 if a 1st player victory is secured
            - -1 if a 2nd player victory is secured
            - 0 otherwise 
        - Third item returns which empty slot to place in (0 to 8) if board state is non-terminal.
        
        Third item value should be ignored if the first value reads False.
    '''
    empty_squares = [i for i in range(len(board_state)) if board_state[i] == 0]
    player = 1 if len(empty_squares) % 2 == 1 else -1

    # ensure that current board still has decisions to make
    if len(empty_squares) == 0 or board_value(board_state)[1] != 0:
        return (True, board_value(board_state)[1], -1)
    
    # let moves[0] indicate moves that give board value 0,
    # moves[1] indicate moves that give board value 1,
    # and moves[-1] indicate moves that give board value -1.
    moves = [[], [], []]
    for i in empty_squares:
        curr = board_state[:]
        curr[i] = player
        _, value, _ = minimax_agent(curr)
        moves[value].append(i)

    # always pick the board state that is optimal for the current player
    if len(moves[player]) > 0:
        return (False, player, moves[player][random.randrange(0, len(moves[player]))])
    elif len(moves[0]) > 0:
        return (False, 0, moves[0][random.randrange(0, len(moves[0]))])
    else:
        return (False, -player, moves[-player][random.randrange(0, len(moves[-player]))])