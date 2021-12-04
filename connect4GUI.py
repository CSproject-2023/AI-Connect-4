import numpy as np
from numpy.core.fromnumeric import size 
import pygame
import sys
import math
ROW_COUNT=6
COLUMN_COUNT=7
BLUE=(0,0,255)
BLACK=(0,0,0)
RED=(255,0,0)
YELLOW=(255,255,0)
def create_board():
    board=np.zeros((ROW_COUNT,COLUMN_COUNT))
    return board

def drop_piece(board,col,row,piece):
    board[row][col]=piece
    pass

def is_valid_location(board,col):
    return board[ROW_COUNT-1][col]==0
def get_next_open_row(board,col):
    for r in range(ROW_COUNT):
        if board[r][col]==0:
            return r


def print_board(board):
    print(np.flip(board,0))

def winning_move(board,piece):
    #check horizontal location for win 
    for c in range (COLUMN_COUNT):
        pass

def draw_board(board):
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):
			pygame.draw.rect(screen, BLUE, (c*SQUARESIZE, r*SQUARESIZE+SQUARESIZE, SQUARESIZE, SQUARESIZE))
			pygame.draw.circle(screen, BLACK, (int(c*SQUARESIZE+SQUARESIZE/2), int(r*SQUARESIZE+SQUARESIZE+SQUARESIZE/2)), radius)
	
	for c in range(COLUMN_COUNT):
		for r in range(ROW_COUNT):		
			if board[r][c] == 1:
				pygame.draw.circle(screen, RED, (int(c*SQUARESIZE+SQUARESIZE/2), hight-int(r*SQUARESIZE+SQUARESIZE/2)), radius)
			elif board[r][c] == 2: 
				pygame.draw.circle(screen, YELLOW, (int(c*SQUARESIZE+SQUARESIZE/2), hight-int(r*SQUARESIZE+SQUARESIZE/2)), radius)
	pygame.display.update()


board=create_board()
game_over=False
turn =0

pygame.init()

SQUARESIZE=100 #size of each square =100px

width=COLUMN_COUNT*SQUARESIZE
hight=(ROW_COUNT+1)*SQUARESIZE
size=(width,hight)
radius=int(SQUARESIZE/2)
screen=pygame.display.set_mode(size)
draw_board(board)
pygame.display.update()
myfont = pygame.font.SysFont("monospace", 60)
posX= 0
while not game_over:

    if turn == 0:
        pygame.draw.circle(screen,RED,(posX, int(SQUARESIZE/2)), radius=radius)
    else :
        pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE/2)), radius)
    pygame.display.update()
    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            sys.exit()
        if event.type==pygame.MOUSEMOTION:
            pygame.display.update()
            pygame.draw.rect(screen, BLACK, (0,0, width, SQUARESIZE))
            posX=event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen,RED,(posX, int(SQUARESIZE/2)), radius=radius)
            else :
                pygame.draw.circle(screen, YELLOW, (posX, int(SQUARESIZE/2)), radius)
            
        pygame.display.update()            
 			   
        if event.type==pygame.MOUSEBUTTONDOWN:
            
            #player 1 turn 
            if turn ==0:
                posX=event.pos[0]
                col=int(math.floor(posX/SQUARESIZE))

                
                if is_valid_location(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,col,row,1)


            else :
                posX=event.pos[0]
                col=int(math.floor(posX/SQUARESIZE))
                if is_valid_location(board,col):
                    row=get_next_open_row(board,col)
                    drop_piece(board,col,row,2)


            print_board(board)
            draw_board(board)
            turn+=1
            turn =turn%2               

            #player 2 turn 

