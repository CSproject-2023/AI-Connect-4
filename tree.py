import numpy as np
import matplotlib.pyplot as plt

ROUNDING_NUM= 3
MAX_HEIGHT_TO_PRINT= 2
#Odd levels are Minimize, while Even are Maximize
class TreeNode:

    def __init__(self, score:int, parent=None):
        self.score= score
        self.parent=parent
        self.x= 0
        self.children=[]

    def __str__(self) -> str:
        return f'Score:{self.score}'
    
def set_color_on_height(height):
    return "red" if height%2 ==1 else "green"
def set_label_on_height(height):
    return "Minimize" if height%2 ==1 else "Maximize"


def draw_tree(tree_list:list): #List of levels
    #First we get maxLevel containing nodes.

    max_height= 0
    for i in range(len(tree_list)):
        print(len(tree_list[i]))
        if len(tree_list[i]):
            max_height=i
    max_height= min(max_height, MAX_HEIGHT_TO_PRINT)
    print(f'Max is {max_height}')

    ##Now we plot the bottom first
    bottom_nodes_length= len(tree_list[max_height])
    x_s= np.ones((bottom_nodes_length,2))
    index= 0
    parent= None
    currentX= 1
    for node in tree_list[max_height]:
        if parent is not None and node.parent != parent:
            currentX += 4
            parent= node.parent
        if parent is None:
            parent= node.parent
        x_s[index,0]= currentX
        node.x=currentX
        currentX+=1
        index+=1

    plt.scatter(x_s,np.ones_like(x_s), color=set_color_on_height(max_height) , label=set_label_on_height(max_height))
    count= 1
    height1= 0.8
    height2= 0.6
    switch=True
    for node in tree_list[max_height]:
        # plt.scatter(count,1, color='red')
        plt.annotate(f"{round(node.score,ROUNDING_NUM)}", (node.x-1,height1 if switch else height2 ), size=5,color='blue')
        switch= not switch
        if node.parent is not None:
            node.parent.children.append(node.x)
    ## Now next level

    for i in range(max_height-1,-1,-1):
        x_s= np.zeros(len(tree_list[i]))

        for c in range(len(tree_list[i])):
            point= np.average(tree_list[i][c].children)
            x_s[c]=point
            tree_list[i][c].x=point

            if tree_list[i][c].parent is not None:
                tree_list[i][c].parent.children.append(point)


        plt.scatter(x_s,np.ones_like(x_s) * (max_height - i +1) , color=set_color_on_height(i), label=set_label_on_height(i))

        for node in tree_list[i]:
            plt.annotate(f"{round(node.score,ROUNDING_NUM)}", (node.x,max_height - i +1),color='blue' )
            
            ##Now connect with children
            for child in node.children:
                plt.plot([node.x,child],[max_height - i +1,max_height - i ] , color='black')
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    plt.ylim((0,max_height+2))
    plt.legend()
    plt.show()

if __name__ == '__main__':
    treeList= [[] for i in range (3)]
    root= TreeNode(10)
    treeList[0].append(root)
    left= TreeNode(15,root)
    right= TreeNode(20,root)
    treeList[1].append(right)
    treeList[1].append(left)
    right_r= TreeNode(30,right)
    right_l= TreeNode(10,right)
    left_l= TreeNode(-10,left)
    left_r= TreeNode(-5, left)
    treeList[2].append(left_l)
    treeList[2].append(left_r)
    treeList[2].append(right_l)
    treeList[2].append(right_r)
    
    
    draw_tree(treeList)

    

