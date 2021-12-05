"""
Here we will have the common functions among several files
"""
import numpy as np
# The add to board.
# Calculating score.


#is_board_completed
def is_state_complete(board:np.ndarray):
    return  True if  len(board[board==0]) == 0 else False


