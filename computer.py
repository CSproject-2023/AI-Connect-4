import numpy as np
import math
import library as lib
COLUMN_INDEX= 0

def get_computer_decision(board_state:np.ndarray) -> np.int8:
    """
    We need to get the column which the computer choose
    return: column position
    """
    return maximize(board_state.copy())[COLUMN_INDEX]

def maximize(state:np.ndarray, level:int, alpha:float = None, beta:float= None) -> tuple:
    
    if lib.is_state_complete(state):
        return (-1, get_score(state)) #get_score needs to be identified (What does it return indeed)

    (max_pos, max_score)= (-1,-math.inf)
    
    state_children= get_children(state)
    
    for child in state_children:

        (pos, score)= minimize(child, level+1, alpha, beta)

        if score > max_score:
            max_score= score
            max_pos= pos
        
        if alpha is not None and beta is not None:
            
            if max_score >= beta:
                break
            if max_score > alpha:
                alpha= max_score

    return (max_pos,max_score) 


def minimize(state:np.ndarray, level:int, alpha:float = None, beta:float= None) -> tuple:
    
    if lib.is_state_complete(state):
        return (-1, get_score(state)) #get_score needs to be identified (What does it return indeed)

    (min_pos, min_score)= (-1,math.inf)
    
    state_children= get_children(state)
    
    for child in state_children:

        (pos, score)= maximize(child, level+1, alpha, beta)

        if score < min_score:
            min_score= score
            min_pos= pos
        
        if alpha is not None and beta is not None:
            
            if min_score <= alpha:
                break
            if min_score < beta:
                beta= min_score

    return (min_pos,min_score) 

