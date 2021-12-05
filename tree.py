import numpy as np
import matplotlib.pyplot as plt
class TreeNode:

    def __init__(self, score:int, parent=None):
        self.score= score
        self.parent=parent
        self.x= 0
        self.children=[]

    def __str__(self) -> str:
        return f'Score:{self.score}'

def draw_tree(tree_list:list): #List of levels
    #First we get maxLevel containing nodes.

    max_height= 0
    for i in range(len(tree_list)):
        print(len(tree_list[i]))
        if len(tree_list[i]):
            max_height=i
    print(f'Max is {max_height}')

    ##Now we plot the bottom first
    bottom_nodes_length= len(tree_list[max_height])
    x_s= np.arange(1,bottom_nodes_length, 1)
    plt.scatter(x_s,np.ones_like(x_s))
    count= 1
    for node in tree_list[max_height]:
        # plt.scatter(count,1, color='red')
        plt.annotate(f"{node.score}", (count, 1), color='blue')
        node.x= count
        count +=1
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


        plt.scatter(x_s,np.ones_like(x_s) * (max_height - i +1) , color='red')

        for node in tree_list[i]:
            plt.annotate(f"{node.score}", (node.x,max_height - i +1),color='blue' )
            
            ##Now connect with children
            for child in node.children:
                plt.plot([node.x,child],[max_height - i +1,max_height - i ] , color='black')
    fig = plt.gcf()
    fig.set_size_inches(18.5, 10.5)
    # plt.xlim(0,500)
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

    

