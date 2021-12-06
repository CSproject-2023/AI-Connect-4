"""
Here we will have the common functions among several files
"""
import numpy as np
# The add to board.
# Calculating score.


#is_board_completed
def is_state_complete(board:np.ndarray):
    return  True if  len(board[board==0]) == 0 else False

def get_score(state,player_no,width = 8,length = 8):
    score = 0
    for i in range(width):
        for j in range(length):
            if i + 3 < width: score = __update_score(score,state,player_no,i,j,1,0)
            if i + 3 < width and j + 3 < length:  score = __update_score(score,state,player_no,i,j,1,1)
            if i + 3 < width and j - 3 >= 0:  score = __update_score(score,state,player_no,i,j,1,-1)
            if j + 3 < length:  score = __update_score(score,state,player_no,i,j,0,1)
    return score

def __update_score(score,state,player_no,i,j,x,y):
    connect4 = True
    for z in range(4):
        if state[i + z * x][j + z * y] != player_no:
            connect4 = False
    return score+1 if connect4 else score


