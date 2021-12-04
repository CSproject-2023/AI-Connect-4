import numpy as np


def get_children(state,value) :
    answer =[]
    temp=True
    for  i in range(8):
        child=np.copy(state)
        for  j in range(8):
            if child[i][j]==0 :
                child[i][j]= value
                temp=False
                break
        if temp==True :
            answer.append(None) 
        else :
            answer.append(child)
        temp=True  
           

    return answer

# a_2d = np.arange(64).reshape((8, 8))
# x= get_children( a_2d,10)
# print(x)

