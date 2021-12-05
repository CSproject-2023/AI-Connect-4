import numpy as np
import math
import library as lib
from tree import TreeNode,draw_tree
from heuristic import heuristic


PLAYER_VALUE=1
COMPUTER_VALUE= 2

COLUMN_INDEX= 0
SCORE_INDEX=1
MAX_LEVEL= 1
h = heuristic(8, 8, [0, 1, 3, 6, 10])

tree_list= None



def get_computer_decision(board_state:np.ndarray) -> np.int8:
    global tree_list
    """
    We need to get the column which the computer choose
    return: column position
    """
    tree_list= [[] for i in range(MAX_LEVEL+1)]
    pos=maximize(board_state.copy(),0,None, COMPUTER_VALUE)[COLUMN_INDEX]
    draw_tree(tree_list)
    return  pos


def get_children(state,value) :
    answer =[]
    temp=True
    for  i in range(8):
        child=np.copy(state)
        for  j in reversed(range(8)):
            if child[j][i]==0 :
                child[j][i]= value
                temp=False
                break
        if temp==True :
            answer.append(None) 
        else :
            answer.append(child)
        temp=True  
            
    return answer

def maximize(state:np.ndarray, level:int,parent_node:TreeNode,value ,alpha:float = None, beta:float= None) -> tuple:
    global tree_list
    node= TreeNode(-1,parent_node)
    # print(level)
    tree_list[level].append(node)

    if level == MAX_LEVEL:
        score= h.solve(state) #Calculating Objective Function
        node.score=score
        return (-1,score) 
    
    if lib.is_state_complete(state):
        score=get_score(state) #get_score needs to be identified (What does it return indeed)
        node.score=score
        return (-1,score)

    (max_pos, max_score)= (-1,-math.inf)
    
    state_children= get_children(state,value)
    
    for i in range (len(state_children)):
        if state_children[i] is None:
            continue

        score= minimize(state_children[i], level+1, node,PLAYER_VALUE if value ==COMPUTER_VALUE else COMPUTER_VALUE,alpha, beta)[SCORE_INDEX]

        if score > max_score:
            max_score= score
            node.score= score
            max_pos= i
        
        if alpha is not None and beta is not None:
            if max_score >= beta:
                break
            if max_score > alpha:
                alpha= max_score

    return (max_pos,max_score) 


def minimize(state:np.ndarray, level:int,parent_node:TreeNode, value,alpha:float = None, beta:float= None) -> tuple:
    global tree_list
    node= TreeNode(-1,parent_node)
    # print(level)
    tree_list[level].append(node)

    if level == MAX_LEVEL:
        score= h.solve(state)
        node.score=score
        return (-1,score) 
    
    if lib.is_state_complete(state):
        score=get_score(state) #get_score needs to be identified (What does it return indeed)
        node.score=score
        return (-1,score)

    (min_pos, min_score)= (-1,math.inf)
    
    state_children= get_children(state,value)
    
    for i in range (len(state_children)):
        if state_children[i] is None:
            continue

        score= maximize(state_children[i], level+1,node,PLAYER_VALUE if value ==COMPUTER_VALUE else COMPUTER_VALUE, alpha, beta)[SCORE_INDEX]

        if score < min_score:
            min_score= score
            node.score= score
            min_pos= i
        
        if alpha is not None and beta is not None:
            
            if min_score <= alpha:
                break
            if min_score < beta:
                beta= min_score

    return (min_pos,min_score) 

